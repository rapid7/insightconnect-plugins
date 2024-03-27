import insightconnect_plugin_runtime
from .schema import DeleteApiKeysInput, DeleteApiKeysOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class DeleteApiKeys(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_api_keys",
            description=Component.DESCRIPTION,
            input=DeleteApiKeysInput(),
            output=DeleteApiKeysOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        key_ids = params.get(Input.ID)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.api_key.delete(
            *key_ids,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while deleting API key.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        response = 207 if "SUCCESS" in response.result_code else 0
        return {Output.STATUS: response}
