import insightconnect_plugin_runtime
from .schema import (
    RemoveAddressObjectFromGroupInput,
    RemoveAddressObjectFromGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_palo_alto_pan_os.util.util import extract_static_members, get_response_entry


class RemoveAddressObjectFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_address_object_from_group",
            description=Component.DESCRIPTION,
            input=RemoveAddressObjectFromGroupInput(),
            output=RemoveAddressObjectFromGroupOutput(),
        )

    def run(self, params={}):
        address_object_name = params.get(Input.ADDRESS_OBJECT)
        group_name = params.get(Input.GROUP)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        response = self.connection.request.get_address_group(
            device_name=device_name, virtual_system=virtual_system, group_name=group_name
        )

        entry = get_response_entry(response)
        if entry is None:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find group '{group_name}', or group was empty. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {virtual_system}",
                data=response,
            )

        names = extract_static_members(entry, group_name)

        if address_object_name not in names:
            self.logger.info(f"Address object '{address_object_name}' was not in group '{group_name}'.")
            return {Output.SUCCESS: False}

        self.connection.request.remove_address_group_member(
            device_name=device_name,
            virtual_system=virtual_system,
            group_name=group_name,
            member=address_object_name,
        )

        return {Output.SUCCESS: True}
