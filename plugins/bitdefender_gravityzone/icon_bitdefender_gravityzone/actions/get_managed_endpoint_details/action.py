import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetManagedEndpointDetailsInput, GetManagedEndpointDetailsOutput, Input, Output, Component

# Custom imports below
from icon_bitdefender_gravityzone.util.helpers import clean_endpoint_id


class GetManagedEndpointDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_managed_endpoint_details",
            description=Component.DESCRIPTION,
            input=GetManagedEndpointDetailsInput(),
            output=GetManagedEndpointDetailsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        endpoint_id = params.get(Input.ENDPOINT_ID)
        include_last_logged_users = params.get(Input.INCLUDE_LAST_LOGGED_USERS)
        include_scan_logs = params.get(Input.INCLUDE_SCAN_LOGS)
        # END INPUT BINDING - DO NOT REMOVE

        endpoint_details = self.connection.api.get_managed_endpoint_details(
            endpoint_id=clean_endpoint_id(endpoint_id),
            include_scan_logs=bool(include_scan_logs),
            include_last_logged_users=bool(include_last_logged_users),
        )
        return {Output.ENDPOINT_DETAILS: endpoint_details}
