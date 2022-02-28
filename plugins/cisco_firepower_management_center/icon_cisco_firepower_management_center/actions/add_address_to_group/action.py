import insightconnect_plugin_runtime
from .schema import AddAddressToGroupInput, AddAddressToGroupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddAddressToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_address_to_group",
            description=Component.DESCRIPTION,
            input=AddAddressToGroupInput(),
            output=AddAddressToGroupOutput(),
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
                self._generate_payload(address_object, address_group)
            )
        }

    @staticmethod
    def _generate_payload(address_object: dict, address_group: dict) -> dict:
        new_address_object = {}
        required_field = ["type", "id", "name"]
        for field in required_field:
            new_address_object[field] = address_object.get(field)

        address_group["objects"].append(new_address_object)
        address_group.pop("links", None)

        return address_group
