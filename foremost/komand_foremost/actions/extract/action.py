import komand
from .schema import ExtractInput, ExtractOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import os
import base64
import binascii
import tempfile


class Extract(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='extract',
            description=Component.DESCRIPTION,
            input=ExtractInput(),
            output=ExtractOutput())

    def run(self, params={}):
        _file = params.get(Input.FILE).encode('UTF-8')

        # Verify string is base64
        try:
            base64.decodebytes(_file)
        except binascii.Error as e:
            self.logger.error('Error: Invalid Base64 string')
            raise PluginException(cause='Error: Invalid Base64 string', data=e)

        # Set file path to store file
        tmp_dir = tempfile.gettempdir()
        file_name = "foremost.img"
        full_path = f"{tmp_dir}/{file_name}"

        # Set variables needed when calling foremost
        file_types = "all"
        output_dir = f"{tmp_dir}/foremost"
        binary = "/usr/bin/foremost"
        cmd = f"{binary} -t {file_types} -i {full_path} -o {output_dir}"

        # Decode bas64 string and write to file
        with open(full_path, "wb") as fh:
            fh.write(base64.decodebytes(_file))

        # Run foremost against file
        try:
            komand.helper.exec_command(cmd)
        except Exception as e:
            self.logger.error("Foremost: Unable to process image")
            raise PluginException(cause='Error: Bad image file',
                                  assistance="Foremost: Unable to process image",
                                  data=e)

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

        return {Output.FILES: files, Output.FILE_COUNT: file_count}
