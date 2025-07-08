import insightconnect_plugin_runtime
from .schema import (
    AddAddressObjectToGroupInput,
    AddAddressObjectToGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddAddressObjectToGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_address_object_to_group",
            description=Component.DESCRIPTION,
            input=AddAddressObjectToGroupInput(),
            output=AddAddressObjectToGroupOutput(),
        )

    def run(self, params={}):
        new_address_objects = params.get(Input.ADDRESS_OBJECT)
        group_name = params.get(Input.GROUP)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        # See if we can get the group the user is looking for:
        response = self.connection.request.get_address_group(
            device_name=device_name,
            virtual_system=virtual_system,
            group_name=group_name,
        )

        try:
            address_objects = (
                response.get("response")
                .get("result")
                .get("entry")
                .get("static")
                .get("member")
            )
        except AttributeError:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find group '{group_name}', or group was empty. Check the name, virtual system "
                f"name, and device name.\nDevice name: {device_name}\nVirtual system: {virtual_system}\n",
                data=response,
            )

        # We got the group, now pull out all the address object names
        names = []

        try:
            if isinstance(address_objects, list):
                for address in address_objects:
                    names.append(address.get("#text"))
            else:
                names.append(address_objects.get("#text"))
        except AttributeError:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not get the address object name. Check the group name, virtual system "
                f"name, and device name and try again.\nDevice name: {device_name}\nVirtual "
                f"system: {virtual_system}\n",
                data=address_objects,
            )

        # Append the address_objects
        for name in new_address_objects:
            if name not in names:
                names.append(name)
            else:
                self.logger.info(
                    f"Address Object '{name}' was already in group '{group_name}'. Skipping append."
                )

        # Rebuild the object in the way the API wants and send it back to the API
        self.connection.request.edit_address_group(
            device_name=device_name,
            virtual_system=virtual_system,
            group_name=group_name,
            xml_str=self.make_xml(names, group_name),
        )

        return {Output.SUCCESS: True, Output.ADDRESS_OBJECTS: names}

    @staticmethod
    def make_xml(names, group_name):
        members = "".join(f"<member>{name}</member>" for name in names)
        xml_template = f"<entry name='{group_name}'><static>{members}</static></entry>"
        return xml_template
