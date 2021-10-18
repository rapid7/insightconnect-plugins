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
        name = params.get(Input.ADDRESS_OBJECT, "")
        name = name if name else host
        whitelist = params.get(Input.WHITELIST)
        skip_rfc1918 = params.get(Input.SKIP_RFC1918)
        helper = Helpers(self.logger)

        address_type = helper.determine_address_type(host)

        if address_type == "ipmask" or address_type == "ipprefix":
            host = helper.ipmask_converter(host)

        if (
            (address_type == "ipmask" or address_type == "ipprefix")
            and skip_rfc1918 is True
            and ipaddress.ip_network(host).is_private
        ):
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
