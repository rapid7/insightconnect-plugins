import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import RestoreEndpointInput, RestoreEndpointOutput, Input, Output, Component

# Custom imports below
from icon_bitdefender_gravityzone.util.helpers import clean_endpoint_id


class RestoreEndpoint(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="restore_endpoint",
            description=Component.DESCRIPTION,
            input=RestoreEndpointInput(),
            output=RestoreEndpointOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        endpoint_id = params.get(Input.ENDPOINT_ID)
        # END INPUT BINDING - DO NOT REMOVE

        # Raises PluginException unless GravityZone confirms that the restore task was created
        self.connection.api.restore_endpoint(clean_endpoint_id(endpoint_id))
        return {Output.SUCCESS: True}
