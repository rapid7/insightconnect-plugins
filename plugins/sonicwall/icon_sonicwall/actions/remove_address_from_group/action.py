import insightconnect_plugin_runtime
from .schema import (
    RemoveAddressFromGroupInput,
    RemoveAddressFromGroupOutput,
    Input,
    Output,
    Component,
)
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Dict, Any

# Custom imports below


class RemoveAddressFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_address_from_group",
            description=Component.DESCRIPTION,
            input=RemoveAddressFromGroupInput(),
            output=RemoveAddressFromGroupOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        address_object = params.get(Input.ADDRESS_OBJECT, "")
        group_name = params.get(Input.GROUP, "")
        # END INPUT BINDING - DO NOT REMOVE

        group = self.connection.sonicwall_api.get_group(group_name)
        object_type = self.connection.sonicwall_api.get_address_object(address_object).get("object_type")
        group_object, group_type = group.get("group_object", {}), group.get("group_type")

        if not self.check_address_object_in_group(address_object, group_object, group_type):
            raise PluginException(
                cause=f"The address object: '{address_object}' does not exist in the address group.",
                assistance="Please enter valid names and try again.",
            )

        # Use CLI because an endpoint is not supported for this at the time of writing
        payload = f"""address-group {group_type} '{group_name}'
        no address-object {object_type} '{address_object}'
        exit
        commit"""

        return {Output.STATUS: self.connection.sonicwall_api.invoke_cli_command(payload)}

    def check_address_object_in_group(self, address_object: str, group_object: Dict[str, Any], group_type: str) -> bool:
        address_objects_names, address_objects = [], {}
        for value in group_object.values():
            if isinstance(value, list) and value:
                address_objects = next((element.get(group_type, {}).get("address_object", {}) for element in value), {})
            elif isinstance(value, dict):
                address_objects = value.get(group_type, {}).get("address_object", {})
            if address_object:
                break

        object_types = ("ipv4", "ipv6", "mac", "fqdn")
        for object_type in object_types:
            address_objects_names.extend(address_objects.get(object_type, []))

        for object_from_group in address_objects_names:
            if object_from_group.get("name") == address_object:
                return True
        return False
