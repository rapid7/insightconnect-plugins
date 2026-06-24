import insightconnect_plugin_runtime
from .schema import GetDeviceByIpInput, GetDeviceByIpOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
import validators

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
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        ip_address = params.get(Input.IP_ADDRESS, "")
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        if not (validators.ip_address.ipv4(ip_address) or validators.ip_address.ipv6(ip_address)):
            raise PluginException(cause="Invalid input", assistance="IP Address must be a valid IPv4 or IPv6 address")

        device = self.connection.automox_api.find_device_by_attribute(
            org_id, ["ip_addrs", "ip_addrs_private"], ip_address
        )
        return {Output.DEVICE: device}
