import insightconnect_plugin_runtime
from .schema import GetApiKeyInput, GetApiKeyOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetApiKey(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_api_key",
            description=Component.DESCRIPTION,
            input=GetApiKeyInput(),
            output=GetApiKeyOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        key_id = params.get(Input.ID)
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.api_key.get(
            key_id=key_id,
        )
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while getting API key.",
                assistance="Please check your inputs and try again.",
                data=response.error,
            )
        # Return results
        self.logger.info("Returning Results...")
        data = response.response.data
        return {
            Output.ETAG: response.response.etag,
            Output.NAME: data.name,
            Output.ID: data.id,
            Output.ROLE: data.role,
            Output.STATUS: data.status,
            Output.DESCRIPTION: data.description,
            Output.EXPIRED_DATE_TIME: data.expired_date_time,
            Output.LAST_USED_DATE_TIME: data.last_used_date_time,
        }
