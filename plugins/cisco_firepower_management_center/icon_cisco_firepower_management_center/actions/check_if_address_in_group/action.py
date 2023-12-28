import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import (
    CheckIfAddressInGroupInput,
    CheckIfAddressInGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
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

    def run(self, params={}):
        address_to_check = params.get(Input.ADDRESS)
        group_name = params.get(Input.GROUP)
        object_names_to_return, literals_to_return = [], []
        found = False

        group_object = self.connection.cisco_firepower_api.get_address_group(group_name)
        address_group_objects, literal_group_objects = group_object.get("objects", []), group_object.get("literals", [])
        for item in address_group_objects:
            if item.get("name") == address_to_check:
                object_names_to_return.append(
                    self.connection.cisco_firepower_api.get_address_object(
                        f"{item.get('type').lower()}s", item.get("id")
                    )
                )
                found = True
                break
        for item in literal_group_objects:
            if item.get("value") == address_to_check:
                literals_to_return.append(item)
                found = True
                break
        if params.get(Input.ENABLE_SEARCH, False) and not object_names_to_return:
            all_objects = self.connection.cisco_firepower_api.get_network_addresses()
            for group_object in address_group_objects:
                for address_object in all_objects:
                    if address_object.get("name") == group_object.get("name") and self._check_address(
                        address_object.get("value"), address_to_check
                    ):
                        object_names_to_return.append(address_object)
                        found = True
        return {
            Output.FOUND: found,
            Output.ADDRESS_OBJECTS: object_names_to_return,
            Output.LITERAL_OBJECTS: literals_to_return,
        }

    @staticmethod
    def _check_address(host_value: str, address_to_check: str) -> bool:
        return (
            address_to_check == host_value
            or CheckIfAddressInGroup._check_cidr(address_to_check, host_value)
            or CheckIfAddressInGroup._check_cidr(host_value, address_to_check)
        )

    @staticmethod
    def _check_cidr(ip_address: str, ip_cidr: str) -> bool:
        try:
            if not ip_address or not ip_cidr or not validators.ipv4(ip_address):
                return False
            ip_address = ip_address if "/" not in ip_address else ip_address[: ip_address.index("/")]
            return "/" in ip_cidr and ipaddress.IPv4Address(ip_address) in ipaddress.ip_network(ip_cidr).hosts()
        except ValueError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
