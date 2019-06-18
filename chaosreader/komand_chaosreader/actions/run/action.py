import komand
from .schema import RunInput, RunOutput
# Custom imports below
import os
import base64
import binascii
from bs4 import BeautifulSoup


class Run(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Run Chaosreader on a PCAP or Snoop file',
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        dump = params.get('dump').encode('UTF-8')
        exclude = params.get('exclude')

        # Initialize variables
        options = []
        ip_count = []
        tcp_count = []
        udp_count = []
        proto_count = []
        ethernet_count = []
        files = []
        sessions = []

        # Set file path to store file
        dir = "/tmp/chaosreader"
        file_name = "chaosreader.pcap"
        full_path = "%s/%s" % (dir, file_name)

        # Set variables needed when calling chaosreader
        binary = "/usr/bin/chaosreader"
        if options:
          cmd = "%s %s -D %s %s" % (binary, full_path, dir, options)
        else:
          cmd = "%s %s -D %s" % (binary, full_path, dir)

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

        # Verify string is base64
        try:
          base64.decodestring(dump)
        except binascii.Error:
          self.logger.error('Error: Invalid Base64 string')
          raise

        # Create output directory
        os.makedirs(dir)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
          fh.write(base64.decodestring(dump))

        # Run chaosreader
        r = komand.helper.exec_command(cmd)
        
        if r['rcode'] != 0:
          raise Exception("Chaosreader: Unable to process file")

        # Iterate through files created by chaosreader and append as b64
        for name in os.listdir(dir):
          if name != file_name:
            new_path = "%s/%s" % (dir, name)
            with open(new_path, "rb") as fh:
              encoded = base64.b64encode(fh.read())
              b64_string = encoded.decode("utf-8")
              # Append to list only if it is unique
              if b64_string not in files:
                files.append(b64_string)

        # Log if no files are returned
        if not files:
          self.logger.info("No files extracted")

        # Number of files extracted
        file_count = len(files)

        # Separate tables to parse data
        with open("%s/index.html" % dir) as f:
          contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        session_table = soup.find_all('table')[0]
        ipcount_table = soup.find_all('table')[1]
        tcpcount_table = soup.find_all('table')[2]
        udpcount_table = soup.find_all('table')[3]
        protocount_table = soup.find_all('table')[4]
        ethernetcount_table = soup.find_all('table')[5]

        # Define function to parse data from index.html
        def export_info(table, final):
          for i in table.find_all('tr'):
            proto = i.find_all('td')[0]
            proto_str = str(proto.string)
            count = i.find_all('td')[1]
            count_int = int(count.string)
            new_count = {'source': proto_str, 'count': count_int}
            final.append(new_count)

        # Extract session data
        for i in session_table.find_all('tr'):
          session = i.get_text()
          session_str = str(session.rstrip())
          session_str = session_str.replace("\n", "\\n")
          sessions.append(session_str)

        # Extract IP count
        export_info(ipcount_table, ip_count)

        # Extract TCP count
        export_info(tcpcount_table, tcp_count)

        # Extract UDP count
        export_info(udpcount_table, udp_count)

        # Extract proto count
        export_info(protocount_table, proto_count)

        # Extract ethernet count
        export_info(ethernetcount_table, ethernet_count)

        return {'files': files,
          'file_count': file_count,
          'sessions': sessions,
          'ip_count': ip_count,
          'tcp_count': tcp_count,
          'udp_count': udp_count,
          'proto_count': proto_count,
          'ethernet_count': ethernet_count}

    def test(self):
        dump = "1MOyoQIABAAAAAAAAAAAAP//AAABAAAAfAFSWLu4BwBKAAAASgAAAAgAJ/3K6wgAJ07ZOQgARQAAPEfLQABABtroCgECBAoBAgOD8QBQL1y2bwAAAACgAnIQYcoAAAIEBbQEAggKAGvxpAAAAAABAwMHfAFSWO+4BwBKAAAASgAAAAgAJ07ZOQgAJ/3K6wgARQAAPAAAQABABiK0CgECAwoBAgQAUIPxtfoCHS9ctnCgEnEgGDcAAAIEBbQEAggKAHhDcABr8aQBAwMHfAFSWFm6BwBCAAAAQgAAAAgAJ/3K6wgAJ07ZOQgARQAANEfMQABABtrvCgECBAoBAgOD8QBQL1y2cLX6Ah6AEADlBbEAAAEBCAoAa/GkAHhDcHwBUlhrugcAkgAAAJIAAAAIACf9yusIACdO2TkIAEUAAIRHzUAAQAbangoBAgQKAQIDg/EAUC9ctnC1+gIegBgA5VkiAAABAQgKAGvxpQB4Q3BHRVQgL3Rlc3QuemlwIEhUVFAvMS4xDQpVc2VyLUFnZW50OiBjdXJsLzcuMzUuMA0KSG9zdDogMTAuMS4yLjMNCkFjY2VwdDogKi8qDQoNCnwBUlhrugcAQgAAAEIAAAAIACdO2TkIACf9yusIAEUAADRBbkAAQAbhTQoBAgMKAQIEAFCD8bX6Ah4vXLbAgBAA4xgvAAABAQgKAHhDcABr8aV8AVJYI74HAPABAADwAQAACAAnTtk5CAAn/crrCABFAAHiQW9AAEAG354KAQIDCgECBABQg/G1+gIeL1y2wIAYAOMZ3QAAAQEICgB4Q3EAa/GlSFRUUC8xLjEgMjAwIE9LDQpEYXRlOiBUaHUsIDE1IERlYyAyMDE2IDAyOjM1OjQwIEdNVA0KU2VydmVyOiBBcGFjaGUvMi40LjcgKFVidW50dSkNCkxhc3QtTW9kaWZpZWQ6IFdlZCwgMTQgRGVjIDIwMTYgMTg6NDQ6MDEgR01UDQpFVGFnOiAiYzUtNTQzYTJiODZhOWMyMCINCkFjY2VwdC1SYW5nZXM6IGJ5dGVzDQpDb250ZW50LUxlbmd0aDogMTk3DQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL3ppcA0KDQpQSwMECgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAHAB0ZXN0LnR4dFVUCQADJZJRWCWSUVh1eAsAAQQAAAAABAAAAAB0aGlzIGlzIGEgdGVzdCBmb3IgY2hhb3NyZWFkZXIKUEsBAh4DCgAAAAAAE5WOSbFVXfQfAAAAHwAAAAgAGAAAAAAAAQAAAKSBAAAAAHRlc3QudHh0VVQFAAMlklFYdXgLAAEEAAAAAAQAAAAAUEsFBgAAAAABAAEATgAAAGEAAAAAAHwBUlj+vgcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRHzkAAQAba7QoBAgQKAQIDg/EAUC9ctsC1+gPMgBAA7QOpAAABAQgKAGvxpQB4Q3F8AVJY08kHAEIAAABCAAAACAAn/crrCAAnTtk5CABFAAA0R89AAEAG2uwKAQIECgECA4PxAFAvXLbAtfoDzIARAO0DqAAAAQEICgBr8aUAeENxfAFSWGjKBwBCAAAAQgAAAAgAJ07ZOQgAJ/3K6wgARQAANEFwQABABuFLCgECAwoBAgQAUIPxtfoDzC9ctsGAEQDjGC8AAAEBCAoAeENxAGvxpXwBUlheywcAQgAAAEIAAAAIACf9yusIACdO2TkIAEUAADRH0EAAQAba6woBAgQKAQIDg/EAUC9ctsG1+gPNgBAA7QOmAAABAQgKAGvxpgB4Q3E=".encode('UTF-8')

        # Set file path to store file
        dir = "/tmp/chaosreader"
        file_name = "chaosreader.pcap"
        full_path = "%s/%s" % (dir, file_name)

        # Set variables needed when calling chaosreader
        binary = "/usr/bin/chaosreader"
        cmd = "%s %s -D %s" % (binary, full_path, dir)               
                                                                       
        # Create output directory                                      
        os.makedirs(dir)                                               
                                                                       
        # Decode bas64 string and write to file                        
        with open(full_path, "wb") as fh:                              
          fh.write(base64.decodestring(dump))                          
                                                                       
        # Run chaosreader                                              
        r = komand.helper.exec_command(cmd) 

        # Check that file was extracted
        for name in os.listdir(dir):
          if name.endswith(".zip"):
            break
        else:
          raise Exception("Chaosreader: Unable to process file")

        return {}
