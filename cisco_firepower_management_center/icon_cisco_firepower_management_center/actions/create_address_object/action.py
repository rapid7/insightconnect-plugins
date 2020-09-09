import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
import re
import validators
from ipaddress import ip_network, ip_address, IPv4Network, IPv6Network
from komand.exceptions import PluginException


class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        address_type = self._determine_address_type(address)
        whitelist = params.get(Input.WHITELIST)

        if params.get(Input.SKIP_PRIVATE_ADDRESS) and address_type != "fqdn" and self._check_if_private(address,
                                                                                                        address_type):
            raise PluginException(cause="Private address provided to be blocked.",
                                    assistance="Skip Private Address set to true but private IP: "
                                                f"{address} provided to be blocked.")

        if whitelist:
            self._match_whitelist(address, whitelist, address_type)

        return {
            Output.ADDRESS_OBJECT: self.connection.cisco_firepower_api.create_address_object(
                address_type,
                {
                    "name": params.get(Input.ADDRESS_OBJECT, params.get(Input.ADDRESS)),
                    "value": address
                }
            )
        }
         
    
    def _match_whitelist(self, address, whitelist, object_type):
        if object_type == "fqdn":
            if address in whitelist:
                raise PluginException(
                    cause=f"Address Object not created because the host {address} was found in the whitelist.",
                    assistance="If you would like to block this host remove it from the whitelist and try again.")
            else:
                return False

        # if 1.1.1.1/32 - remove /32
        trimmed_address = re.sub(r"/32$", "", address)

        # if contains / we compare explicit matches, but not subnets in subnets
        if '/' in trimmed_address:
            return address in whitelist

        # IP is in CIDR - Give the user a log message
        for object in whitelist:
            type = self._determine_address_type(object)
            if type == "cidr":
                net = ip_network(object, False) # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(trimmed_address)
                if ip in net:
                    raise PluginException(
                        cause=f"Address Object not created because the host {address}"
                              f" was found in the whitelist as {object}.",
                        assistance="If you would like to block this host,"
                                   f" remove {object} from the whitelist and try again.")

        return False

    @staticmethod
    def _check_if_private(address: str, address_type: str) -> bool:
        if address_type == "ipv6":
            ip_list = [str(ip) for ip in IPv6Network(address)]
        else:
            ip_list = [str(ip) for ip in IPv4Network(address)]

        if ip_address(ip_list[0]).is_private and ip_address(ip_list[-1]).is_private:
            return True
        return False

    @staticmethod
    def _determine_address_type(address: str) -> str:
        if validators.ipv4(address):
            return "ipv4"
        if validators.ipv6(address):
            return "ipv6"
        if validators.domain(address):
            return "fqdn"
        if re.search('/', address):
            return "cidr"
        raise PluginException(cause="Unknown address type provided.",
                              assistance=f"{address} is not one of the following: IPv4, IPv6, CIDR or domain name.")
