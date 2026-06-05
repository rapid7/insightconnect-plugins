import insightconnect_plugin_runtime
from .schema import GetDeviceSoftwareInput, GetDeviceSoftwareOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetDeviceSoftware(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device_software",
            description=Component.DESCRIPTION,
            input=GetDeviceSoftwareInput(),
            output=GetDeviceSoftwareOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        device_id = params.get(Input.DEVICE_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        device_software = self.connection.automox_api.get_device_software(org_id, device_id)
        return {Output.SOFTWARE: device_software}
