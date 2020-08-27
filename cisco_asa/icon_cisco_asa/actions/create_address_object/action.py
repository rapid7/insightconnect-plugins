import insightconnect_plugin_runtime
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
import re
from insightconnect_plugin_runtime.exceptions import PluginException
from ipaddress import ip_network, ip_address


class CreateAddressObject(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_address_object',
            description=Component.DESCRIPTION,
            input=CreateAddressObjectInput(),
            output=CreateAddressObjectOutput())

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        name = params.get(Input.ADDRESS_OBJECT, address.replace(":", "-").replace("/", "-"))
        whitelist = params.get(Input.WHITELIST)
        skip_private = params.get(Input.SKIP_PRIVATE_ADDRESSES)

        object_type = self.determine_address_type(address)
        if skip_private and object_type != "fqdn" and self.check_if_private(address):
            raise PluginException(
                cause="Private address found.",
                assistance="Address object was RFC 1918 (private)."
            )

        if object_type != "IPv4Range" and whitelist and self.match_whitelist(address, whitelist, object_type):
            raise PluginException(
                cause="Address whitelisted.",
                assistance="Address object matched whitelist."
            )

        self.connection.cisco_asa_api.create_address_object(name, object_type, address)
        return {
            Output.SUCCESS: True
        }

    @staticmethod
    def determine_address_type(address: str) -> str:
        if ':' in address:
            return "IPv6Address"
        if '/' in address:
            return "IPv4Network"
        if re.search(r'[a-zA-Z]', address):
            return "IPv4FQDN"
        if '-' in address:
            return "IPv4Range"

        return "IPv4Address"

    def match_whitelist(self, address: str, whitelist: list, object_type: str) -> bool:
        if address in whitelist:
            self.logger.info(f"Whitelist matched\n{address} was found in whitelist")
            return True

        if object_type == "IPv4FQDN":
            return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", address)

        # IP is in CIDR - Give the user a log message
        for item in whitelist:
            if self.determine_address_type(item) == "IPv4Network":
                net = ip_network(item, False)  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    self.logger.info(f"Whitelist matched\nIP {address} was found in {item}")
                    return True

        return False

    @staticmethod
    def check_if_private(address: str) -> bool:
        if re.search('/', address):  # CIDR
            return ip_network(address, False).is_private
        elif re.search('-', address):  # IP Range
            split_ = address.split("-")
            if len(address.split("-")) != 2:  # If this isn't 2, I'm not sure what the input was
                raise PluginException(
                    cause="Wrong input",
                    assistance="Range should have one and only one dash"
                )
            return ip_address(split_[0]).is_private and ip_address(split_[1]).is_private
        try:  # Other
            if ip_address(address).is_private:
                return True
        except ValueError as _:  # This was a domain name
            pass

        return False
