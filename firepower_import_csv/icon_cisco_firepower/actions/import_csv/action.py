import insightconnect_plugin_runtime
from .schema import ImportCsvInput, ImportCsvOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cisco_firepower.util.commands import generate_set_os_command, generate_add_host_command, \
    generate_add_result_command, generate_set_source_command
from io import StringIO
from paramiko import SSHClient
import csv
import base64
import os
import paramiko
import time
from OpenSSL import crypto
import subprocess


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

        vuln_objects = self.convert_csv_to_scan_results(vuln_list)
        operation = "ScanUpdate" # This tells Firepower to update host vulnerabilities with new results. ScanFlush will remove existing results

        ################
        #  Write CSV File
        ################
        cvs_file_string = ""
        for vuln in vuln_objects:
            ip = vuln.get("host", {}).get("ip_address")
            if ip:
                command = self.create_scan_result(ip, vuln, operation)
                cvs_file_string += command
            else:
                self.logger.warning("Vulnerability found without an IP address, skipping. Vulnerability follows")
                self.logger.warning(f"{vuln}")

        firepower_filename = "firepower_import.csv"
        f = open(firepower_filename, "w")
        filename = os.path.realpath(f.name)
        f.write(cvs_file_string)
        f.close()


        ################
        #  Copy CSV to Server
        ################
        scp_command = f"sshpass -p {self.connection.password} scp {filename} {self.connection.username}@{self.connection.host}:/Volume/home/admin/{firepower_filename}"
        stream = os.popen(scp_command)
        output = stream.read()
        if output:
            raise PluginException(cause="Could not copy payload file to the firepower server",
                                  assistance=output)
        stream.close()


        ################
        #  SSH to server and run nmimport.pl on the csv file
        ################
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh connect
        ssh.connect(self.connection.host,
                    username=self.connection.username,
                    password=self.connection.password,
                    look_for_keys=False,
                    timeout=60)

        # ssh and run nmimport.pl
        # nmimport_command = f"sudo -S -p \"{self.connection.password}\n\" /usr/local/sf/bin/nmimport.pl /Volume/home/admin/{firepower_filename}"
        nmimport_command = f"echo {self.connection.password} | sudo -S /usr/local/sf/bin/nmimport.pl /Volume/home/admin/firepower_import.csv"
        stdin, stdout, stderr = ssh.exec_command(nmimport_command)
        stdout_str = stdout.read()
        stderr_str = stderr.read()
        ssh.close()

        if "Done processing" in str(stdout_str):
            return {
                Output.RESULT: stdout_str.decode("utf-8"),
                Output.SUCCESS: True
            }

        raise PluginException(cause="Firepower failed to process input file.",
                              assistance=f"Error: {stderr_str}\nOutput: {stdout_str}")



    # This converts the decoded CSV into objects we can process
    def convert_csv_to_scan_results(self, vuln_list):
        scan_results = []
        for vuln in vuln_list:
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
                    "description": vuln.get("description", ""),
                    "vulnerability_title": vuln.get("title", ""),
                    "cve_ids": "", # Space-separated list of CVE vulnerability IDs
                    "bugtraq_ids": "", # Space-separated list of BugTraq vulnerability IDs
                }
            }

            scan_results.append(scan_result)
        return scan_results

    # This will generate a set of commands from a given vulnerability.
    # ex
    # AddHost,1.2.3.5
    # AddScanResult,1.2.3.5,"Qualys",82003,,,"ICMP Timestamp Request","ICMP (Internet Control and Error Message Protocol) is a protocol encapsulated in IP packets. Its principal purpose is to provide a protocol layer able to inform gateways of the inter-connectivity and accessibility of other gateways or hosts. ping is a well-known program for determining if a host is up or down. It uses ICMP echo packets. ICMP timestamp packets are used to synchronize clocks between hosts.","cve_ids: CVE-1999-0524","bugtraq_ids:"
    def create_scan_result(self, address, scan_result, operation):
        # Operation
        # - ScanUpdate
        # - ScanFlush

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
        # if not new_host:
        #     command += "ScanUpdate"
        # else:
        #     command += operation
        #     command += "\n"
        command += "ScanUpdate\n"
        return command

    # Read a CSV and return the headers list and each row as a dictionary
    def read_csv(self, csv_string):
        f = StringIO(csv_string)
        reader = csv.DictReader(f)

        fields = reader.fieldnames
        out_dict = []
        for row in reader:
            out_dict.append(row)

        return fields, out_dict
