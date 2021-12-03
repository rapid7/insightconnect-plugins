import insightconnect_plugin_runtime
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import ipaddress
from icon_fortinet_fortigate.util.util import Helpers


class CreateAddressObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_address_object",
            description=Component.DESCRIPTION,
            input=CreateAddressObjectInput(),
            output=CreateAddressObjectOutput(),
        )

    def run(self, params={}):
        host = params.get(Input.ADDRESS)
        name = params.get(Input.ADDRESS_OBJECT) or host
        whitelist = params.get(Input.WHITELIST)
        skip_rfc1918 = params.get(Input.SKIP_RFC1918)
        helper = Helpers(self.logger)

        address_type = helper.determine_address_type(host)

        if address_type in ("ipmask", "ipprefix"):
            host = helper.ipmask_converter(host)

        # skip private addresses - first we check if the given address is IPv4(ipmask) or IPv6(ipprefix), then we check
        # if we want to skip private addresses(skip_rfc1918), and finally if the given address is private
        if address_type in ("ipmask", "ipprefix") and skip_rfc1918 is True and ipaddress.ip_network(host).is_private:
            return {
                Output.SUCCESS: False,
                Output.RESPONSE_OBJECT: {
                    "message": f"The IP address specified ({host}) is private and will be ignored as per "
                    f"the action configuration."
                },
            }

        found = False
        if whitelist:
            found = helper.match_whitelist(host, whitelist)
        if not found:
            return {
                Output.SUCCESS: True,
                Output.RESPONSE_OBJECT: self.connection.api.create_address_object(name, host, address_type),
            }

        return {
            Output.SUCCESS: False,
            Output.RESPONSE_OBJECT: {"message": "Host matched whitelist, skipping creating an address object."},
        }
