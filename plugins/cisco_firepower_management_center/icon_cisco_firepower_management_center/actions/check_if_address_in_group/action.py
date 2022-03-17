import insightconnect_plugin_runtime
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
        found = False
        object_names_to_return = []

        address_group_objects = self.connection.cisco_firepower_api.get_address_group(group_name).get("objects", [])
        for item in address_group_objects:
            if item.get("name") == address_to_check:
                object_names_to_return.append(
                    self.connection.cisco_firepower_api.get_address_object(
                        f"{item.get('type').lower()}s", item.get("id")
                    )
                )
                found = True

                return {Output.FOUND: found, Output.ADDRESS_OBJECTS: object_names_to_return}

        if params.get(Input.ENABLE_SEARCH):
            all_objects = self.connection.cisco_firepower_api.get_network_addresses()
            for group_object in address_group_objects:
                for address_object in all_objects:
                    if address_object.get("name") == group_object.get("name") and self._check_address(
                        address_object.get("value"), address_to_check
                    ):
                        object_names_to_return.append(address_object)
                        found = True

        return {Output.FOUND: found, Output.ADDRESS_OBJECTS: object_names_to_return}

    @staticmethod
    def _check_address(host_value, address_to_check):
        return (
            address_to_check == host_value
            or CheckIfAddressInGroup._check_cidr(address_to_check, host_value)
            or CheckIfAddressInGroup._check_cidr(host_value, address_to_check)
        )

    @staticmethod
    def _check_cidr(ip_address, ip_cidr):
        if not ip_address or not ip_cidr or not validators.ipv4(ip_address):
            return False

        return "/" in ip_cidr and ipaddress.IPv4Address(ip_address) in ipaddress.ip_network(ip_cidr).hosts()
