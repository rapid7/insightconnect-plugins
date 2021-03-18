# Custom imports below
import ipaddress

import komand
from komand.exceptions import PluginException

from icon_checkpoint_ngfw.util.utils import PublishException
from icon_checkpoint_ngfw.util.utils import check_if_ip_in_whitelist
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component


class CreateAddressObject(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_address_object",
            description=Component.DESCRIPTION,
            input=CreateAddressObjectInput(),
            output=CreateAddressObjectOutput(),
        )

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/add-host"

        user_ip_address = params.get(Input.HOST_IP)
        name = params.get(Input.NAME)
        whitelist = params.get(Input.WHITELIST)
        skip_rfc1918 = params.get(Input.SKIP_RFC1918, [])

        try:
            is_private = ipaddress.ip_address(user_ip_address).is_private
        except ValueError as e:
            # example: `ValueError: 'hello world' does not appear to be an IPv4 or IPv6 address`
            raise PluginException(cause=f"Invalid IP address provided: {user_ip_address}", assistance=e)

        if skip_rfc1918 and is_private:
            return {
                Output.HOST_OBJECT: {},
                Output.SUCCESS: False,
                Output.ERROR_MESSAGE: f"The IP address specified ({user_ip_address}) is private and will "
                f"be ignored as per the action configuration.",
            }

        try:
            if len(whitelist) > 0 and check_if_ip_in_whitelist(ip_address=user_ip_address, whitelist=whitelist):
                return {
                    Output.HOST_OBJECT: {},
                    Output.SUCCESS: False,
                    Output.ERROR_MESSAGE: f"The IP address specified ({user_ip_address}) was found within "
                    f"the whitelist.",
                }
        except ValueError as e:
            raise PluginException(
                cause="Invalid entry found in whitelist.",
                assistance="Please ensure the entries within the whitelist are valid IP "
                "addresses (IPv4 or IPv6) or CIDR IP addresses.",
                data=e,
            )

        payload = {"name": name, "ip-address": user_ip_address}

        color = params.get(Input.COLOR)

        if color:
            payload["color"] = color

        headers = self.connection.get_headers()

        try:
            result = self.connection.post_and_publish(headers, payload, url)
            return {Output.HOST_OBJECT: komand.helper.clean(result.json()), Output.SUCCESS: True}
        except PublishException as e:
            return {
                Output.HOST_OBJECT: {},
                Output.SUCCESS: False,
                Output.ERROR_MESSAGE: e.get_errors()[0],
            }
        except PluginException as e:
            if "Multiple objects have the same" in e.assistance or "More than one object named" in e.assistance:
                return {
                    Output.HOST_OBJECT: {},
                    Output.SUCCESS: False,
                    Output.ERROR_MESSAGE: "A host with the IP address or name already exists!",
                }
