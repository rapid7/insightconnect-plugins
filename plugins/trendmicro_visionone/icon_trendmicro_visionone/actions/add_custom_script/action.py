import insightconnect_plugin_runtime
from .schema import (
    AddCustomScriptInput,
    AddCustomScriptOutput,
    Input,
    Output,
    Component,
)

from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
from base64 import b64decode


class AddCustomScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_custom_script",
            description=Component.DESCRIPTION,
            input=AddCustomScriptInput(),
            output=AddCustomScriptOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        file = params.get(Input.FILE)
        file_type = params.get(Input.FILE_TYPE)
        description = params.get(Input.DESCRIPTION, "")
        # Choose enum
        if "bash" in file_type:
            file_type = pytmv1.ScriptType.BASH
        elif "powershell" in file_type:
            file_type = pytmv1.ScriptType.POWERSHELL
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.script.create(
            script_type=file_type,
            script_name=file.get("filename"),
            script_content=b64decode(file.get("content")).decode("utf-8"),
            description=description,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while uploading a custom script.",
                assistance="Please check the provided inputs and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.SCRIPT_ID: response.response.script_id}
