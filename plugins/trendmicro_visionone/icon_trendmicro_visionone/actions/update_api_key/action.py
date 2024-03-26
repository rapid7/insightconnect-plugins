import insightconnect_plugin_runtime
from .schema import UpdateApiKeyInput, UpdateApiKeyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import pytmv1


class UpdateApiKey(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_api_key",
            description=Component.DESCRIPTION,
            input=UpdateApiKeyInput(),
            output=UpdateApiKeyOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        id = params.get(Input.ID)
        if_match = params.get(Input.IF_MATCH, "")
        name = params.get(Input.NAME)
        status = params.get(Input.STATUS)
        role = params.get(Input.ROLE)
        description = params.get(Input.DESCRIPTION, "")
        # Choose enum
        if "enabled" in status:
            status = pytmv1.ApiStatus.ENABLED
        elif "disabled" in status:
            status = pytmv1.ApiStatus.DISABLED
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.api_key.update(
            key_id=id,
            etag=if_match,
            name=name,
            status=status,
            role=role,
            description=description,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while updating API key.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        response = 204 if "SUCCESS" in response.result_code else 0
        return {Output.STATUS: response}
