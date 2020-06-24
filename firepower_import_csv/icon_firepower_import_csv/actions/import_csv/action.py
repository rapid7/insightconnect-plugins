import insightconnect_plugin_runtime
from .schema import ImportCsvInput, ImportCsvOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_firepower_import_csv.util.commands import generate_set_os_command, generate_add_host_command, \
    generate_add_result_command, generate_set_source_command
from io import StringIO
from paramiko import SSHClient
from bs4 import BeautifulSoup
import csv
import base64
import os
import paramiko


class ImportCsv(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='import_csv',
                description=Component.DESCRIPTION,
                input=ImportCsvInput(),
                output=ImportCsvOutput())

    def run(self, params={}):
        csv_encoded = params.get(Input.CSV)

        try:
            csv_string = base64.b64decode(csv_encoded).decode("utf-8")
        except Exception as e:
            self.logger.error(str(e))
            raise PluginException(PluginException.Preset.BASE64_DECODE)

        headers, vuln_list = self.read_csv(csv_string)

        #################
        # Remove duplicates
        #################
        self.logger.info(f"Number of records found: {len(vuln_list)}")
        vuln_list = [dict(t) for t in {tuple(d.items()) for d in vuln_list}]
        self.logger.info(f"Duplicates removed, Number of records found: {len(vuln_list)}")

        vuln_objects = self.convert_csv_to_scan_results(vuln_list)
        self.logger.info(f"Number of records to process: {len(vuln_objects)}")

        ################
        #  Write CSV File
        ################
        self.logger.info("Building payload file...")
        cvs_file_string = ""
        for vuln in vuln_objects:
            ip = vuln.get("host", {}).get("ip_address")
            if ip:
                command = self.create_scan_result(ip, vuln)
                cvs_file_string += command
            else:
                self.logger.warning("Vulnerability found without an IP address, skipping. Vulnerability follows")
                self.logger.warning(f"{vuln}")

        firepower_filename = "firepower_import.csv"
        f = open(firepower_filename, "w")
        firepower_fullpath = os.path.realpath(f.name)
        f.write(cvs_file_string)
        f.close()
        self.logger.info("Building payload file complete.")

       ################
        #  Copy files to Server
        ################
        self.logger.info("Copying payload file to server...")
        scp_command_firepower = f"sshpass -p {self.connection.password} scp -o StrictHostKeyChecking=no {firepower_fullpath} {self.connection.username}@{self.connection.host}:/Volume/home/admin/{firepower_filename}"
        stream = os.popen(scp_command_firepower)
        output = stream.read()
        if output:
            raise PluginException(cause="Could not copy payload file to the firepower server",
                                  assistance=output)
        stream.close()
        self.logger.info("Copy complete.")

        ################
        #  Cleanup local files
        ################
        self.logger.info("Starting local cleanup...")
        rm_stream1 = os.popen(f"rm {firepower_fullpath}")
        rm_stream1.close()
        self.logger.info("Local cleanup complete.")

        ################
        #  SSH to server and run nmimport.pl on the csv file
        ################
        self.logger.info("Running nmimport.pl on server...")
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh connect
        ssh.connect(self.connection.host,
                    username=self.connection.username,
                    password=self.connection.password,
                    look_for_keys=False,
                    timeout=60)

        # ssh and run nmimport.pl
        nmimport_command = f"sudo /usr/local/sf/bin/nmimport.pl /Volume/home/admin/{firepower_filename}"
        stdin, stdout, stderr = ssh.exec_command(nmimport_command)

        # This will hang if the output is excessive. Around 1000 records is the limit this will reasonablly read back from.
        stdout_str = stdout.read(1000)
        stderr_str = stderr.read(1000)

        ssh.close()

        ####################
        # Check results and return
        ####################
        self.logger.info("Running nmimport.pl on server complete.")
        self.logger.info("Checking results.")
        if "Done processing" in str(stdout_str):
            return {
                Output.RESULT: stdout_str.decode("utf-8").strip(),
                Output.SUCCESS: True
            }

        raise PluginException(cause="Firepower failed to process input file.",
                              assistance=f"Error: {stderr_str}\nOutput: {stdout_str}")

    # This converts the decoded CSV into objects we can process
    def convert_csv_to_scan_results(self, vuln_list):
        scan_results = []
        for vuln in vuln_list:
            description = vuln.get("description", "")
            if description:
                description = BeautifulSoup(description, features="html.parser").get_text()

            scan_result = \
            {
                "host": {
                    "ip_address": vuln.get("ip_address", ""),
                    "operating_system": {
                        "name": vuln.get("name", ""),
                        "vendor": vuln.get("vendor", ""),
                        "version": vuln.get("version", ""),
                    },
                },
                "scan_result_details": {
                    "source_id": "InsightVM", # application
                    "port": vuln.get("port", ""),
                    "protocol_id": vuln.get("protocol_id", ""),
                    "scanner_id": "InsightVM",
                    "vulnerability_id": vuln.get("vulnerability_id", ""),
                    "description": description,
                    "vulnerability_title": vuln.get("title", ""),
                    "cve_ids": "", # Space-separated list of CVE vulnerability IDs
                    "bugtraq_ids": "", # Space-separated list of BugTraq vulnerability IDs
                }
            }

            scan_results.append(scan_result)
        return scan_results

    # This will generate a set of commands from a given vulnerability.
    # ex:
    # AddHost,1.2.3.5
    # AddScanResult,1.2.3.5,"Qualys",82003,,,"ICMP Timestamp Request","ICMP (Internet Control and Error Message Protocol) is a protocol encapsulated in IP packets. Its principal purpose is to provide a protocol layer able to inform gateways of the inter-connectivity and accessibility of other gateways or hosts. ping is a well-known program for determining if a host is up or down. It uses ICMP echo packets. ICMP timestamp packets are used to synchronize clocks between hosts.","cve_ids: CVE-1999-0524","bugtraq_ids:"
    # ScanUpdate
    def create_scan_result(self, address, scan_result):
        # Operations
        # - ScanUpdate - This will append results to a host
        # - ScanFlush - This will clear all results on a host and then add results

        # new_host = False
        added_hosts = {}
        command = ""

        details = scan_result.get('scan_result_details', {})
        source_id = details.get('source_id', '')
        command += generate_set_source_command(source_id)

        # See if we need to add a new host
        if not added_hosts.get(address):
            # new_host = True
            host = scan_result.get('host', {})
            command += generate_add_host_command(address)
            if len(host.get("operating_system", {})):
                command += generate_set_os_command(host, address)
            added_hosts[address] = True

        command += generate_add_result_command(details, address)
        command = command.strip() + "\n"
        command += "ScanUpdate\n"
        return command

    # Read a CSV and return the headers list and each row as a dictionary
    # The dictionaries will look like dict['header_name'] = column_value
    def read_csv(self, csv_string):
        f = StringIO(csv_string)
        reader = csv.DictReader(f)

        fields = reader.fieldnames
        out_dict = []
        for row in reader:
            out_dict.append(row)

        return fields, out_dict
