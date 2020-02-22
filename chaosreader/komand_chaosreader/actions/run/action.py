import base64
import binascii
# Custom imports below
import os
import tempfile

from bs4 import BeautifulSoup

import komand
import komand.helper as helper
from komand.exceptions import PluginException
from .schema import RunInput, RunOutput, Input, Output


class Run(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='run',
            description='Run Chaosreader on a PCAP or Snoop file',
            input=RunInput(),
            output=RunOutput())

    def run(self, params={}):
        dump = params.get(Input.DUMP).encode('UTF-8')
        exclude = params.get(Input.EXCLUDE)

        # Initialize variables
        files = []
        sessions = []
        options = ''

        # Set file path to store file
        temp_dir = f"{tempfile.gettempdir()}/chaosreader"
        file_name = "chaosreader.pcap"
        full_path = f"{temp_dir}/{file_name}"

        # Set options to exclude
        if exclude == "Info":
            options = "-I"
            self.logger.info('Exluding info files')
        elif exclude == "Raw":
            options = "-R"
            self.logger.info('Exluding raw files')
        elif exclude == "TCP":
            options = "-T"
            self.logger.info('Exluding TCP traffic')
        elif exclude == "UDP":
            options = "-U"
            self.logger.info('Exluding UDP traffic')
        elif exclude == "ICMP":
            options = "-Y"
            self.logger.info('Exluding ICMP traffic')

        # Set variables needed when calling chaosreader
        binary = "/usr/bin/chaosreader"
        cmd = f"{binary} {full_path} -D {temp_dir} {options}"

        # Verify string is base64
        try:
            base64.decodebytes(dump)
        except binascii.Error as e:
            self.logger.error('Error: Invalid Base64 string')
            raise PluginException(cause=PluginException.Preset.SERVER_ERROR, assistance=str(e))

        # Create output directory
        os.makedirs(temp_dir)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
            fh.write(base64.decodebytes(dump))

        # Run chaosreader
        r = komand.helper.exec_command(cmd)

        if r['rcode'] != 0:
            raise PluginException(cause="Chaosreader was unable to process the file",
                                  assistance="Chaosreader: Unable to process file")

        # Iterate through files created by chaosreader and append as b64
        for name in os.listdir(temp_dir):
            if name != file_name:
                new_path = f"{temp_dir}/{name}"
                with helper.open_file(new_path) as fh:
                    encoded = base64.b64encode(fh.read())
                    b64_string = encoded.decode("utf-8")
                    if b64_string not in files:
                        files.append(b64_string)

        # Log if no files are returned
        if not files:
            self.logger.info("No files extracted")

        # Number of files extracted
        file_count = len(files)

        # Separate tables to parse data
        with open(f"{temp_dir}/index.html") as f:
            contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')

        session_table = soup.find_all('table')[0]
        ip_count_table = soup.find_all('table')[1]
        tcp_count_table = soup.find_all('table')[2]
        udp_count_table = soup.find_all('table')[3]
        proto_count_table = soup.find_all('table')[4]
        ethernet_count_table = soup.find_all('table')[5]

        self.logger.info(ip_count_table)

        # Define function to parse data from index.html
        def export_info(table, count_number):
            final = []
            for tr in table.find_all('tr'):
                if tr.find_all('th'):
                    continue

                proto = tr.find_all('td')[0]
                proto_str = str(proto.string)
                count = tr.find_all('td')[count_number]
                count_int = int(count.string)
                new_count = {'source': proto_str, 'count': count_int}
                final.append(new_count)

            return final

        # Extract session data
        for i in session_table.find_all('tr'):
            session = i.get_text()
            session_str = str(session.rstrip())
            session_str = session_str.replace("\n", "\\n")
            sessions.append(session_str)

        return {
            Output.FILES: files,
            Output.FILE_COUNT: file_count,
            Output.SESSIONS: sessions,
            Output.IP_COUNT: export_info(ip_count_table, 2),  # Extract IP count
            Output.TCP_COUNT: export_info(tcp_count_table, 1),  # Extract TCP count
            Output.UDP_COUNT: export_info(udp_count_table, 1),  # Extract UDP count
            Output.PROTO_COUNT: export_info(proto_count_table, 1),  # Extract proto count
            Output.ETHERNET_COUNT: export_info(ethernet_count_table, 1)  # Extract ethernet count
        }
