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
from komand_palo_alto_pan_os.util.util import extract_static_members, get_response_entry


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
            device_name=device_name, virtual_system=virtual_system, group_name=group_name
        )

        entry = get_response_entry(response)
        if entry is None:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find group '{group_name}', or group was empty. Check the name, virtual system "
                f"name, and device name.\nDevice name: {device_name}\nVirtual system: {virtual_system}\n",
                data=response,
            )

        # We got the group, now pull out all the address object names
        names = extract_static_members(entry, group_name)

        # Only the address objects that are not in the group yet are sent, so that adding one object
        # cannot disturb the ones that are already there
        members_to_add = []
        for name in new_address_objects:
            if name in names or name in members_to_add:
                self.logger.info(f"Address Object '{name}' was already in group '{group_name}'. Skipping append.")
            else:
                members_to_add.append(name)

        if members_to_add:
            self.connection.request.add_address_group_members(
                device_name=device_name,
                virtual_system=virtual_system,
                group_name=group_name,
                members=members_to_add,
            )
        else:
            self.logger.info(f"Group '{group_name}' already held every address object given. Nothing was changed.")

        return {Output.SUCCESS: True, Output.ADDRESS_OBJECTS: names + members_to_add}
