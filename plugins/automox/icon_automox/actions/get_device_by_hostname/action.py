import insightconnect_plugin_runtime
from .schema import GetDeviceByHostnameInput, GetDeviceByHostnameOutput, Input, Output, Component

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
        device = self.connection.automox_api.find_device_by_attribute(
            params.get(Input.ORG_ID), ["name"], params.get(Input.HOSTNAME)
        )
        return {Output.DEVICE: device}
