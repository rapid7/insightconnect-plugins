import base64
import binascii

import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SubmitInput, SubmitOutput, Component, Input, Output


class Submit(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit", description=Component.DESCRIPTION, input=SubmitInput(), output=SubmitOutput()
        )
        self.environment_mapping = {
            "Windows 10 64 bit": 160,
            "Windows 11 64 bit": 140,
            "Windows 7 32 bit": 100,
            "Windows 7 32 bit (HWP Support)": 110,
            "Windows 7 64 bit": 120,
            "Mac Catalina 64 bit (x86)": 400,
            "Android Static Analysis": 200,
        }

    def run(self, params={}):
        params = insightconnect_plugin_runtime.helper.clean_dict(params)
        if Input.ENVIRONMENT_ID in params.keys():
            params.update({Input.ENVIRONMENT_ID: self.environment_mapping.get(params.get(Input.ENVIRONMENT_ID))})

        file_info = params.get(Input.FILE, None)
        try:
            file_bytes = base64.b64decode(file_info.get("content"))
        except binascii.Error:
            raise PluginException(
                cause="Unable to decode base64.",
                assistance="Contents of the file must be base64-encoded!",
            )
        response_json = self.connection.api.submit(files={"file": (file_info.get("filename"), file_bytes)}, data=params)

        return {
            Output.JOB_ID: response_json.get(Output.JOB_ID),
            Output.SUBMISSION_ID: response_json.get(Output.SUBMISSION_ID),
            Output.ENVIRONMENT_ID: response_json.get(Output.ENVIRONMENT_ID),
            Output.SHA256: response_json.get(Output.SHA256),
        }
