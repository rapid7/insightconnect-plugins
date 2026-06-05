import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IsolateEndpointInput, IsolateEndpointOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IsolateEndpoint(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_endpoint",
            description=Component.DESCRIPTION,
            input=IsolateEndpointInput(),
            output=IsolateEndpointOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        endpoint_id = params.get(Input.ENDPOINT_ID)
        # END INPUT BINDING - DO NOT REMOVE

        if not endpoint_id or not endpoint_id.strip():
            raise PluginException(
                cause="Missing required input.",
                assistance="The endpoint_id field is required and cannot be empty.",
            )

        endpoint_id = endpoint_id.strip()

        success = self.connection.api.isolate_endpoint(endpoint_id=endpoint_id)

        return {
            Output.SUCCESS: success,
        }
