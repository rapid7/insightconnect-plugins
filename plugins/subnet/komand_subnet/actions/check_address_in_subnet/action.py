import insightconnect_plugin_runtime
from .schema import CheckAddressInSubnetInput, CheckAddressInSubnetOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import ipcalc
import validators


class CheckAddressInSubnet(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_address_in_subnet",
            description=Component.DESCRIPTION,
            input=CheckAddressInSubnetInput(),
            output=CheckAddressInSubnetOutput(),
        )

    def run(self, params={}):
        ip = params.get(Input.IP_ADDRESS)
        subnet = params.get(Input.SUBNET)
        if not validators.ipv4(ip):
            raise PluginException(
                cause="Invalid IP address.",
                assistance="Please check that the provided IP address is correct and try again.",
            )
        try:
            return {Output.FOUND: ip in ipcalc.Network(subnet)}
        except ValueError:
            raise PluginException(
                cause="Invalid subnet.", assistance="Please check that the provided subnet is correct and try again."
            )
