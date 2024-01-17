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
        file_name = params.get(Input.FILE_NAME)
        description = params.get(Input.DESCRIPTION, "")
        # Choose enum
        if "bash" in file_type:
            file_type = pytmv1.FileType.BASH
        elif "powershell" in file_type:
            file_type = pytmv1.FileType.POWERSHELL
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.update_custom_script(
            script_id=script_id,
            file=b64decode(file.get("content")),
            file_name=file.get("filename"),
            file_type=file_type,
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
        self.logger.info("Did this really work?!")
        return response
        # return {
        #     Output.ARGUMENTS: response.response.dict().get("arguments", ""),
        #     Output.DIGEST: response.response.dict().get("digest", {}),
        #     Output.ID: response.response.dict().get("id", ""),
        # }
