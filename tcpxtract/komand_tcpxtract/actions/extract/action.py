import komand
from .schema import ExtractInput, ExtractOutput
# Custom imports below
import os
import base64
import binascii


class Extract(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='extract',
                description='Extract files from pcap',
                input=ExtractInput(),
                output=ExtractOutput())

    def run(self, params={}):
        _file = params.get('file').encode('UTF-8')

        # Verify string is base64
        try:
            base64.decodebytes(_file)
        except binascii.Error:
            self.logger.error('Error: Invalid Base64 string')
            raise

        # Set file path to store file
        dir = "/tmp/tcpxtract"
        file_name = "tcpxtract.pcap"
        full_path = "%s/%s" % (dir, file_name)

        # Set variables needed when calling foremost
        file_types = "all"
        binary = "/usr/sbin/tcpxtract"
        cmd = "%s -f %s -o %s" % (binary, full_path, dir)

        # Create output directory
        os.makedirs(dir)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
            fh.write(base64.decodestring(_file))

        # Run tcpxtract against pcap
        try:
            r = komand.helper.exec_command(cmd)
        except:
            self.logger.error("Tcpxtract: Unable to process pcap")
            raise

        # Initialize list to store b64 encoded files
        files = []

        # Iterate through directories created by tcpxtract and append files as b64
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

        return {"files": files, 'file_count': file_count}

    def test(self):
        # Ensure tcpxtract exists
        binary = "/usr/sbin/tcpxtract"
        if not os.path.isfile(binary):
            raise Exception('Tcpxtract not found')
        return {}
