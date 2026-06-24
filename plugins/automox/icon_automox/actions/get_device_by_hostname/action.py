import insightconnect_plugin_runtime
from .schema import GetDeviceByHostnameInput, GetDeviceByHostnameOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class GetDeviceByHostname(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device_by_hostname",
            description=Component.DESCRIPTION,
            input=GetDeviceByHostnameInput(),
            output=GetDeviceByHostnameOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        hostname = params.get(Input.HOSTNAME, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        device = self.connection.automox_api.find_device_by_attribute(org_id, ["name"], hostname)
        return {Output.DEVICE: device}
