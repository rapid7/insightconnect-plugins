import insightconnect_plugin_runtime
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
import re
import validators
from ipaddress import ip_network, ip_address, IPv4Network, IPv6Network
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateAddressObject(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        name = params.get(Input.ADDRESS_OBJECT, params.get(Input.ADDRESS))
        address = params.get(Input.ADDRESS)
        address_type = self._determine_address_type(address)
        whitelist = params.get(Input.WHITELIST)
        zone = params.get(Input.ZONE)

        if params.get(Input.SKIP_PRIVATE_ADDRESS) and address_type != "fqdn" and self._check_if_private(address,
                                                                                                        address_type):
            raise PluginException(cause="Private address provided to be blocked.",
                                    assistance="Skip Private Address set to true but private IP: "
                                                f"{address} provided to be blocked.")

        if whitelist:
            self._match_whitelist(address, whitelist)

        self.connection.sonicwall_api.validate_if_zone_exists(zone)

        response = self.connection.sonicwall_api.create_address_object(
            address_type,
            self._create_payload(name, zone, address, address_type)
        )

        return {
            Output.STATUS: response['status']
        }

    def _create_payload(self, name: str, zone: str, address: str, address_type: str) -> dict:
        payload = {
            "name": name,
            "zone": zone
        }
        if address_type == "fqdn":
            payload["domain"] = address
            payload["dns_ttl"] = 0
        elif address_type == "cidr":
            payload["network"] = self._generate_subnet_netmask(address)
        else:
            payload["host"] = {
                "ip": address
            }

        object_type = address_type
        if address_type == "cidr":
            object_type = "ipv4"

        return {
            "address_objects": [{
                object_type: payload
            }]
        }

    def _match_whitelist(self, address: str, whitelist: str) -> bool:
        trimmed_address = re.sub(r"/32$", "", address)
        if address in whitelist:
            raise PluginException(
                cause=f"Address Object not created because the host {address} was found in the whitelist as {address}.",
                assistance=f"If you would like to block this host, remove {address} from the whitelist and try again.")
        elif '/' not in trimmed_address:
            pass

        for address_object in whitelist:
            if self._determine_address_type(address_object) == "cidr":
                net = ip_network(address_object, False)
                ip = ip_address(trimmed_address)
                if ip in net:
                    raise PluginException(
                        cause=f"Address Object not created because the host {address}"
                              f" was found in the whitelist as {address_object}.",
                        assistance="If you would like to block this host,"
                              f" remove {address_object} from the whitelist and try again.")

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
    def _generate_subnet_netmask(address: str) -> dict:
        return {
            "subnet": str(IPv4Network(address).network_address),
            "mask": str(IPv4Network(address).netmask)
        }

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
