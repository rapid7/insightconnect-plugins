import insightconnect_plugin_runtime
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component

# Custom imports below
import validators
from ipaddress import ip_network, ip_address, IPv4Network, IPv6Network
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateAddressObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_address_object",
            description=Component.DESCRIPTION,
            input=CreateAddressObjectInput(),
            output=CreateAddressObjectOutput(),
        )

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        if validators.ipv4_cidr(address):
            address = address.replace("/32", "")
        if validators.ipv6_cidr(address):
            address = address.replace("/128", "")
        address_type = self._determine_address_type(address)
        address_object_name = params.get(Input.ADDRESS_OBJECT)
        if not address_object_name:
            address_object_name = address
        whitelist = params.get(Input.WHITELIST)

        if (
            params.get(Input.SKIP_PRIVATE_ADDRESS)
            and address_type != "fqdn"
            and self._check_if_private(address, address_type)
        ):
            raise PluginException(
                cause="Private address provided to be blocked.",
                assistance=f"Skip Private Address set to true but private IP: {address} provided to be blocked.",
            )

        if whitelist and self._match_whitelist(address, whitelist, address_type):
            raise PluginException(
                cause=f"Address Object not created because the host {address} was found in the whitelist.",
                assistance="If you would like to block this host remove it from the whitelist and try again.",
            )

        return {
            Output.ADDRESS_OBJECT: self.connection.cisco_firepower_api.create_address_object(
                address_type,
                {
                    "name": address_object_name.replace("/", "-"),
                    "value": address,
                },
            )
        }

    def _match_whitelist(self, address, whitelist, object_type):
        if object_type == "fqdn":
            return address in whitelist
        if object_type in ["ipv4", "ipv6"] and address in whitelist:
            return True

        # if contains / we compare explicit matches, but not subnets in subnets
        if "/" in address:
            return address in whitelist

        # IP is in CIDR - Give the user a log message
        for address_object in whitelist:
            type_ = self._determine_address_type(address_object)
            if type_ in ["ipv4_cidr", "ipv6_cidr"]:
                net = ip_network(
                    address_object, False
                )  # False means ignore the masked bits, otherwise they need to be 0
                ip = ip_address(address)
                if ip in net:
                    return True
        return False

    @staticmethod
    def _check_if_private(address: str, address_type: str) -> bool:
        if address_type in ["ipv6", "ipv6_cidr"]:
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
        if validators.ipv4_cidr(address):
            return "ipv4_cidr"
        if validators.ipv6_cidr(address):
            return "ipv6_cidr"
        raise PluginException(
            cause="Unknown address type provided.",
            assistance=f"{address} is not one of the following: IPv4, IPv6, CIDR or domain name.",
        )
