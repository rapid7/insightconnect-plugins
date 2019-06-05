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
                description='Extract files from image',
                input=ExtractInput(),
                output=ExtractOutput())

    def run(self, params={}):
        _file = params.get('file').encode('UTF-8')

        # Verify string is base64
        try:
          base64.decodestring(_file)
        except binascii.Error:
          self.logger.error('Error: Invalid Base64 string')
          raise Exception('Error: Invalid Base64 string')

        # Set file path to store file
        dir = "/tmp"
        file_name = "foremost.img"
        full_path = "%s/%s" % (dir, file_name)

        # Set variables needed when calling foremost
        file_types = "all"
        output_dir = "%s/foremost" % dir
        binary = "/usr/bin/foremost"
        cmd = "%s -t %s -i %s -o %s" % (binary, file_types, full_path, output_dir)

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
          fh.write(base64.decodestring(_file))

        # Run foremost against file
        try:
          r = komand.helper.exec_command(cmd)
        except:
          self.logger.error("Foremost: Unable to process image")
          raise Exception('Error: Bad image file')

        # Initialize list to store b64 encoded files
        files = []

        # Iterate through directories created by foremost and append files as b64
        for root, dirs, file_names in os.walk(output_dir, topdown=False):
          for name in file_names:
            # Audit.txt does not need to be returned
            if name != "audit.txt":
              with open(os.path.join(root, name), "rb") as fh:
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
        cmd = '/usr/bin/foremost'
        r = komand.helper.exec_command(cmd)
        if r['rcode'] != 0:
          raise Exception('Foremost returned with non-zero status')
        return {}