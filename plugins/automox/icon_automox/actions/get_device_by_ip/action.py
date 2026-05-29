import insightconnect_plugin_runtime
from .schema import GetDeviceByIpInput, GetDeviceByIpOutput, Input, Output, Component

# Custom imports below


class GetDeviceByIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_device_by_ip",
            description=Component.DESCRIPTION,
            input=GetDeviceByIpInput(),
            output=GetDeviceByIpOutput(),
        )

    def run(self, params={}):
        device = self.connection.automox_api.find_device_by_attribute(
            params.get(Input.ORG_ID), ["ip_addrs", "ip_addrs_private"], params.get(Input.IP_ADDRESS)
        )
        return {Output.DEVICE: device}
