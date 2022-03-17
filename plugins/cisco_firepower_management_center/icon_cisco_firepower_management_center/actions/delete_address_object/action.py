import insightconnect_plugin_runtime
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DeleteAddressObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_address_object",
            description=Component.DESCRIPTION,
            input=DeleteAddressObjectInput(),
            output=DeleteAddressObjectOutput(),
        )

    def run(self, params={}):
        object_info = self._find_object_type_id(params.get(Input.ADDRESS_OBJECT))

        return {
            Output.ADDRESS_OBJECT: self.connection.cisco_firepower_api.delete_address_object(
                object_info.get("object_type"), object_info.get("object_id")
            )
        }

    def _find_object_type_id(self, name: str) -> dict:
        object_types = ["hosts", "fqdns", "networks", "ranges"]

        for object_type in object_types:
            objects = self.connection.cisco_firepower_api.get_address_objects(object_type).get("items")
            if objects:
                for item in objects:
                    if item.get("name") == name:
                        return {"object_type": object_type, "object_id": item.get("id")}

        raise PluginException(
            cause=f"The address object {name} does not exist in Cisco Firepower.",
            assistance="Please enter valid name and try again.",
        )
