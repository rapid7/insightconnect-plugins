import insightconnect_plugin_runtime
from .schema import CreateApiKeysInput, CreateApiKeysOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_trendmicro_visionone.util.constants import API_KEY_EXPIRATION
from icon_trendmicro_visionone.util.constants import API_KEY_STATUS

# Custom imports below
import pytmv1


class CreateApiKeys(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_api_keys",
            description=Component.DESCRIPTION,
            input=CreateApiKeysInput(),
            output=CreateApiKeysOutput(),
        )

    def run(self, params={}):
        # Get Connection Client
        client = self.connection.client
        # Get Action Parameters
        api_key_objects = params.get(Input.API_KEYS_OBJECTS)
        api_keys_request = []
        for api_key_object in api_key_objects:
            months_to_expiration = API_KEY_EXPIRATION.get(api_key_object.get("months_to_expiration", "1"))
            status = API_KEY_STATUS.get(api_key_object.get("status", "enabled"))
            api_keys_request.append(
                pytmv1.ApiKeyRequest(
                    name=api_key_object.get("name"),
                    role=api_key_object.get("role"),
                    months_to_expiration=months_to_expiration,
                    description=api_key_object.get("description", ""),
                    status=status,
                )
            )
        # Make Action API Call
        self.logger.info("Making API Call...")
        response = client.api_key.create(*api_keys_request)
        if "error" in response.result_code.lower():
            raise PluginException(
                cause="An error occurred while creating API key.",
                assistance="Please check your inputs and try again.",
                data=response.errors,
            )
        # Return results
        self.logger.info("Returning Results...")
        api_keys_response = []
        for item in response.response.items:
            api_keys_response.append(item.__dict__)
        return {Output.API_KEYS_RESP: api_keys_response}
