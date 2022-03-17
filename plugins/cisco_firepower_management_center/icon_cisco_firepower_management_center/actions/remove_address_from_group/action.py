import insightconnect_plugin_runtime
from .schema import (
    RemoveAddressFromGroupInput,
    RemoveAddressFromGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class RemoveAddressFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_address_from_group",
            description=Component.DESCRIPTION,
            input=RemoveAddressFromGroupInput(),
            output=RemoveAddressFromGroupOutput(),
        )

    def run(self, params={}):
        address = params.get(Input.ADDRESS)
        group = params.get(Input.GROUP)
        address_object = self.connection.cisco_firepower_api.find_network_object(address)
        address_group = self.connection.cisco_firepower_api.get_address_group(group)

        if not address_group or not address_object:
            raise PluginException(
                cause=f"The address {address} or group {group} does not exist in Cisco Firepower.",
                assistance="Please enter valid names and try again.",
            )

        return {
            Output.NETWORK_GROUP: self.connection.cisco_firepower_api.update_address_group(
                self._generate_payload(address, address_object, address_group)
            )
        }

    @staticmethod
    def _generate_payload(address: str, address_object: dict, address_group: dict) -> dict:
        found = False
        for address_group_object in address_group.get("objects"):
            if address_group_object.get("name") == address_object.get("name") or address_group_object.get(
                "value"
            ) == address_object.get("value"):
                address_group.get("objects").remove(address_group_object)
                found = True

        if not found:
            raise PluginException(
                cause=f"The address {address} does not exist in the address group.",
                assistance="Please enter valid name and try again.",
            )

        address_group.pop("links", None)

        return address_group
