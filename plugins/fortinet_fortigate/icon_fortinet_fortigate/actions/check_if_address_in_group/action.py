import insightconnect_plugin_runtime
from .schema import (
    CheckIfAddressInGroupInput,
    CheckIfAddressInGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import ipaddress
import validators

class CheckIfAddressInGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_if_address_in_group",
            description=Component.DESCRIPTION,
            input=CheckIfAddressInGroupInput(),
            output=CheckIfAddressInGroupOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        group_name = params.get(Input.GROUP)
        ipv6_group_name = params.get(Input.IPV6_GROUP)
        address_to_check = params.get(Input.ADDRESS)
        enable_search = params.get(Input.ENABLE_SEARCH)

        address_objects = self.connection.api.get_address_group(group_name, False).get("member")
        is_ipv6 = False
        try:
            is_ipv6 = self.connection.api.get_address_object(address_to_check)["name"] == "address6"
        except Exception:
            self.logger.info("Address not found with IPV6")
        found = False
        addresses_found = []

        if enable_search and address_objects:
            found, addresses_found = self.search_address_object_by_address(
                address_to_check, address_objects, "firewall/address"
            )
        if is_ipv6:
            ipv6_address_objects = self.connection.api.get_address_group(ipv6_group_name, True).get("member")
            if enable_search and ipv6_address_objects and not found:
                found, addresses_found = self.search_address_object_by_address(
                    address_to_check, ipv6_address_objects, "firewall/address6"
                )

        if address_objects and not found:
            found, addresses_found = self.search_address_object_by_name(address_to_check, address_objects)

        if is_ipv6 and ipv6_address_objects and not found:
            found, addresses_found = self.search_address_object_by_name(address_to_check, ipv6_address_objects)

        return {Output.FOUND: found, Output.ADDRESS_OBJECTS: addresses_found}

    @staticmethod
    def search_address_object_by_name(address_name: str, address_objects: list) -> bool:
        found = False
        addresses_found = []
        for item in address_objects:
            if address_name == item["name"]:
                addresses_found.append(item["name"])
                found = True
        return found, addresses_found

    def search_address_object_by_address(self, address: str, address_objects: list, endpoint: str) -> bool:
        found = False
        addresses_found = []
        for item in address_objects:
            item_name = item.get("name")
            if not item_name:
                continue
            try:
                results = self.connection.api.get_address_objects(
                    endpoint, params={"filter": f"name=@{item_name}"}
                ).get("results", [])
            except KeyError:
                raise PluginException(
                    cause="No results were returned by FortiGate.\n",
                    assistance="This is normally caused by an invalid address group name."
                    " Double check that the address group name is correct.",
                )
            for result in results:
                result_type = result.get("type")
                # If address_object is a IPv6
                if result_type == "ipprefix" and (validators.ipv6(address) or validators.ipv6_cidr(address)):
                    address = str(ipaddress.IPv6Network(address))
                    result_ipv6 = result.get("ip6")
                    if address == result_ipv6:
                        addresses_found.append(result_ipv6)
                        found = True
                # If address_object is a fqdn
                if result_type == "fqdn":
                    result_fqdn = result.get("fqdn")
                    if address == result_fqdn:
                        addresses_found.append(result_fqdn)
                        found = True
                # If address_object is a ipmask
                if result_type == "ipmask":
                    # Convert returned address to CIDR
                    ipmask = result.get("subnet", "").replace(" ", "/")
                    ipmask = ipaddress.IPv4Network(ipmask)
                    # Convert given address to CIDR address to CIDR
                    try:
                        address = ipaddress.IPv4Network(address)
                    except ipaddress.AddressValueError:
                        pass
                    if address == ipmask:
                        addresses_found.append(str(ipmask))
                        found = True

        return found, addresses_found
