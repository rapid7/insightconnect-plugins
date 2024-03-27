import insightconnect_plugin_runtime
from .schema import UpdateCustomScriptInput, UpdateCustomScriptOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1
from base64 import b64decode


class UpdateCustomScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_custom_script",
            description=Component.DESCRIPTION,
            input=UpdateCustomScriptInput(),
            output=UpdateCustomScriptOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        script_id = params.get(Input.SCRIPT_ID)
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
        response = client.script.update(
            script_id=script_id,
            script_content=b64decode(file.get("content")).decode("utf-8"),
            script_name=file.get("filename"),
            script_type=file_type,
            description=description,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while updating a custom script.",
                assistance="Please check the provided inputs and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.RESULT_CODE: response.result_code}
