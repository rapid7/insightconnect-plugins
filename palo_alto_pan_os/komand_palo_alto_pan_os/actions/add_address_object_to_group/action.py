import komand
from .schema import AddAddressObjectToGroupInput, AddAddressObjectToGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException

class AddAddressObjectToGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_address_object_to_group',
                description=Component.DESCRIPTION,
                input=AddAddressObjectToGroupInput(),
                output=AddAddressObjectToGroupOutput())

    def run(self, params={}):
        address_object = params.get(Input.ADDRESS_OBJECT)
        group_name = params.get(Input.GROUP)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        # See if we can get the group the user is looking for:
        xpath = f"/config/devices/entry[@name='{device_name}']/vsys/entry[@name='{virtual_system}']/address-group/entry[@name='{group_name}']"
        response = self.connection.request.get_(xpath)

        address_objects = response.get("response", {}).get("result", {}).get("entry", {}).get("static", {}).get(
            "member")
        if not address_objects:
            raise PluginException(cause="PAN OS returned an unexpected response.",
                                  assistance=f"Could not find group {group_name}, or group was empty. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {virtual_system}",
                                  data=response)

        # We got the group, now pull out all the address object names
        names = []
        for name in address_objects:
            if type(name) == str:
                names.append(name)
            else:
                names.append(name.get("#text"))


        # Append the address_object
        if not address_object in names:
            names.append(address_object)
            # Rebuild the object in the way the API wants
            xml_str = self.make_xml(names, group_name)
            # Send it back ot the API
            self.connection.request.edit_(xpath, xml_str)
        else:
            self.logger.info(f"Address Object \"{address_object}\" was already in group \"{group_name}\". Skipping append.")

        return {Output.SUCCESS: True, Output.ADDRESS_OBJECTS: names}

    def make_xml(self, names, group_name):
        members = ""
        for name in names:
            members += f"<member>{name}</member>"

        xml_template = f"<entry name=\"{group_name}\"><static>{members}</static></entry>"

        return xml_template

