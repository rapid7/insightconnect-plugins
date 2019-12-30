import komand
from komand.exceptions import PluginException
from .schema import RunInput, RunOutput, Input, Output
# Custom imports below
import os
import base64
import binascii
import tempfile
from bs4 import BeautifulSoup


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

        ip_count = []
        tcp_count = []
        udp_count = []
        proto_count = []
        ethernet_count = []
        files = []
        sessions = []

        temp_dir = f"{tempfile.gettempdir()}/chaosreader"
        file_name = "chaosreader.pcap"
        full_path = f"{temp_dir}/{file_name}"

        binary = "/usr/bin/chaosreader"
        cmd = f"{binary} {full_path} -D {temp_dir}"

        if exclude == "Info":
            self.logger.info('Exluding info files')
        elif exclude == "Raw":
            self.logger.info('Exluding raw files')
        elif exclude == "TCP":
            self.logger.info('Exluding TCP traffic')
        elif exclude == "UDP":
            self.logger.info('Exluding UDP traffic')
        elif exclude == "ICMP":
            self.logger.info('Exluding ICMP traffic')

        try:
            base64.decodebytes(dump)
        except binascii.Error as e:
            self.logger.error('Error: Invalid Base64 string')
            raise PluginException(cause=PluginException.Preset.SERVER_ERROR, assistance=str(e))

        os.makedirs(temp_dir)

        with open(full_path, "wb") as fh:
            fh.write(base64.decodebytes(dump))

        r = komand.helper.exec_command(cmd)

        if r['rcode'] != 0:
            raise PluginException(cause="Problem with process file", assistance="Chaosreader: Unable to process file")

        for name in os.listdir(temp_dir):
            if name != file_name:
                new_path = f"{temp_dir}/{name}"
                with open(new_path, "rb") as fh:
                    encoded = base64.b64encode(fh.read())
                    b64_string = encoded.decode("utf-8")
                    if b64_string not in files:
                        files.append(b64_string)

        if not files:
            self.logger.info("No files extracted")

        file_count = len(files)

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

        def export_info(table, final):
            for tr in table.find_all('tr'):
                proto = tr.find_all('td')[0]
                proto_str = str(proto.string)
                count = tr.find_all('td')[1]
                count_int = int(count.string)
                new_count = {'source': proto_str, 'count': count_int}
                final.append(new_count)

        for i in session_table.find_all('tr'):
            session = i.get_text()
            session_str = str(session.rstrip())
            session_str = session_str.replace("\n", "\\n")
            sessions.append(session_str)

        export_info(ip_count_table, ip_count)
        export_info(tcp_count_table, tcp_count)
        export_info(udp_count_table, udp_count)
        export_info(proto_count_table, proto_count)
        export_info(ethernet_count_table, ethernet_count)

        return {
            Output.FILES: files,
            Output.FILE_COUNT: file_count,
            Output.SESSIONS: sessions,
            Output.IP_COUNT: ip_count,
            Output.TCP_COUNT: tcp_count,
            Output.UDP_COUNT: udp_count,
            Output.PROTO_COUNT: proto_count,
            Output.ETHERNET_COUNT: ethernet_count
        }

    def test(self):
        dump = "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAfAFSWLu4BwBKAAAASgAAAAgAJ/3K6wgAJ07ZOQgARQAAPEfLQABABtroCgECBAoBAgOD8QBQL1y2bwAAAACgAnIQYcoAAAIEBbQEAggKAGvxpAAAAAABAwMHfAFSWO+4BwBKAAAASgAAAAgAJ07ZOQgAJ/3K6wgARQAAPAAAQABABiK0CgECAwoBAgQAUIPxtfoCHS9ctnCgEnEgGDcAAAIEBbQEAggKAHhDcABr8aQBAwMHfAFSWFm6BwBCAAAAQgAAAAgAJ/3K6wgAJ07ZOQgARQAANEfMQABABtrvCgECBAoBAgOD8QBQL1y2cLX6Ah6AEADlBbEAAAEBCAoAa/GkAHhDcHwBUlhrugcAkgAAAJIAAAAIACf9yusIACdO2TkIAEUAAIRHzUAAQAbangoBAgQKAQIDg/EAUC9ctnC1+gIegBgA5VkiAAABAQgKAGvxpQB4Q3BHRVQgL3Rlc3QuemlwIEhUVFAvMS4xDQpVc2VyLUFnZW50OiBjdXJsLzcuMzUuMA0KSG9zdDogMTAuMS4yLjMNCkFjY2VwdDogKi8qDQoNCnwBUlhrugcAQgAAAEIAAAAIACdO2TkIACf9yusIAEUAADRBbkAAQAbhTQoBAgMKAQIEAFCD8bX6Ah4vXLbAgBAA4xgvAAABAQgKAHhDcABr8aV8AVJYI74HAPABAADwAQAACAAnTtk5CAAn/crrCABFAAHiQW9AAEAG354KAQIDCgECBABQg/G1+gIeL1y2wIAYAOMZ3QAAAQEICgB4Q3EAa/GlSFRUUC8xLjEgMjAwIE9LDQpEYXRlOiBUaHUsIDE1IERlYyAyMDE2IDAyOjM1OjQwIEdNVA0KU2VydmVyOiBBcGFjaGUvMi40LjcgKFVidW50dSkNCkxhc3QtTW9kaWZpZWQ6IFdlZCwgMTQgRGVjIDIwMTYgMTg6NDQ6MDEgR01UDQpFVGFnOiAiYzUtNTQzYTJiODZhOWMyMCINCkFjY2VwdC1SYW5nZXM6IGJ5dGVzDQpDb250ZW50LUxlbmd0aDogMTk3DQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL3ppcA0KDQpQSwMECgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAHAB0ZXN0LnR4dFVUCQADJZJRWCWSUVh1eAsAAQQAAAAABAAAAAB0aGlzIGlzIGEgdGVzdCBmb3IgY2hhb3NyZWFkZXIKUEsBAh4DCgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAGAAAAAAAAQAAAKSBAAAAAHRlc3QudHh0VVQFAAMlklFYdXgLAAEEAAAAAAQAAAAAUEsFBgAAAAABAAEATgAAAGEAAAAAAHwBUlj+vgcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRHzkAAQAba7QoBAgQKAQIDg/EAUC9ctsC1+gPMgBAA7QOpAAABAQgKAGvxpQB4Q3F8AVJY08kHAEIAAABCAAAACAAn/crrCAAnTtk5CABFAAA0R89AAEAG2uwKAQIECgECA4PxAFAvXLbAtfoDzIARAO0DqAAAAQEICgBr8aUAeENxfAFSWGjKBwBCAAAAQgAAAAgAJ07ZOQgAJ/3K6wgARQAANEFwQABABuFLCgECAwoBAgQAUIPxtfoDzC9ctsGAEQDjGC8AAAEBCAoAeENxAGvxpXwBUlheywcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRH0EAAQAba6woBAgQKAQIDg/EAUC9ctsG1+gPNgBAA7QOmAAABAQgKAGvxpgB4Q3E=".encode('UTF-8')

        temp_dir = f"{tempfile.gettempdir()}/chaosreader"
        file_name = "chaosreader.pcap"
        full_path = f"{temp_dir}/{file_name}"
        binary = "/usr/bin/chaosreader"
        cmd = f"{binary} {full_path} -D {temp_dir}"

        os.makedirs(temp_dir)

        with open(full_path, "wb") as fh:
            fh.write(base64.decodebytes(dump))

        komand.helper.exec_command(cmd)

        for name in os.listdir(temp_dir):
            if name.endswith(".zip"):
                break
        else:
            raise PluginException(cause="Problem with process file", assistance="Chaosreader: Unable to process file")

        pass
