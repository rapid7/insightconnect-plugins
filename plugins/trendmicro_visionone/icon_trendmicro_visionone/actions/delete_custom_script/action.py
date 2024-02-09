import insightconnect_plugin_runtime
from .schema import (
    DeleteCustomScriptInput,
    DeleteCustomScriptOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class DeleteCustomScript(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_custom_script",
            description=Component.DESCRIPTION,
            input=DeleteCustomScriptInput(),
            output=DeleteCustomScriptOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        script_id = params.get(Input.SCRIPT_ID)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.script.delete(
            script_id=script_id,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while deleting a custom script.",
                assistance="Please check the provided script id and try again.",
                data=response,
            )
        # Return results
        self.logger.info("Returning Results...")
        return {Output.RESULT_CODE: response.result_code}
