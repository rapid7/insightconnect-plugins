import binascii

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SubmitFileInput, SubmitFileOutput, Output, Input

# Custom imports below

import base64


class SubmitFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_file",
            description="Submit file for analysis",
            input=SubmitFileInput(),
            output=SubmitFileOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        file_ = params.get(Input.FILE, {})
        optional_params = params.get(Input.OPTIONAL_PARAMS, {})
        analyzer_mode = params.get(Input.ANALYZER_MODE, "default")
        # END INPUT BINDING - DO NOT REMOVE

        file_name = file_.get("filename")
        if analyzer_mode != "default":
            optional_params["analyzer_mode"] = analyzer_mode

        try:
            file_bytes = base64.b64decode(file_.get("content"))
        except [binascii.Error, ValueError]:
            raise PluginException(preset=PluginException.Preset.BASE64_DECODE)

        mime_types, check_pass = self.connection.api.check_filetype(file_bytes)
        if check_pass:
            self.logger.info(f"File types {mime_types} found for file {file_name} and are supported by VMRay")
            resp = self.connection.api.submit_file(file_name, file_bytes, optional_params)
            clean_data = insightconnect_plugin_runtime.helper.clean(resp)
            return {Output.RESULTS: clean_data}
        else:
            raise PluginException(
                cause=f"File types, not supported by VMRay: {mime_types}",
                assistance=f"Here is a list of supported file types {self.connection.api.SUPPORTED_FILETYPES}",
                data={"errors": [{"files": f"File types found are not supported by VMRay {mime_types}"}]},
            )
