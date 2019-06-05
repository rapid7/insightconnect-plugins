import komand
from .schema import SubmitFileInput, SubmitFileOutput
# Custom imports below

import base64


class SubmitFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_file',
                description='Submit file for analysis',
                input=SubmitFileInput(),
                output=SubmitFileOutput())

    def run(self, params={}):
        file_ = params.get('file', None)
        file_name = file_.get("filename")
        optional_params = params.get("optional_params")
        analyzer_mode = params.get("analyzer_mode")
        if analyzer_mode != "default":
            optional_params["analyzer_mode"] = analyzer_mode

        try:
            file_bytes = base64.b64decode(file_.get("content"))
        except:
            raise Exception("Error decoding base64, contents of the file must be encoded with base64!")

        mime_types, check_pass = self.connection.api.check_filetype(file_bytes)
        if check_pass:
            self.logger.info(f"File types {mime_types} found for file {file_name} and are supported by VMRay")
            resp = self.connection.api.submit_file(file_name, file_bytes, optional_params)
            clean_data = komand.helper.clean(resp)
            return {"results": clean_data}
        else:
            self.logger.error(f"File types, not supported by VMRay: {mime_types}")
            self.logger.error(f"Here is a list of supported file types {self.connection.api.SUPPORTED_FILETYPES}")
            return {"results":
                        {"errors":
                             [{"files":f"File types found are not supported by VMRay {mime_types}"}]}}
