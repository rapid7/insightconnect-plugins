import komand
from .schema import RemoveAddressObjectFromGroupInput, RemoveAddressObjectFromGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import xmltodict

class RemoveAddressObjectFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_address_object_from_group',
                description=Component.DESCRIPTION,
                input=RemoveAddressObjectFromGroupInput(),
                output=RemoveAddressObjectFromGroupOutput())

    def run(self, params={}):
        address_object_name = params.get(Input.ADDRESS_OBJECT_NAME)
        group_name = params.get(Input.GROUP_NAME)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        xpath = f"/config/devices/entry[@name='{device_name}']/vsys/entry[@name='{virtual_system}']/address-group/entry[@name='{group_name}']"
        response = self.connection.request.get_(xpath)

        address_objects = response.get("response", {}).get("result", {}).get("entry", {}).get("static", {}).get("member")
        if not address_objects:
            raise PluginException(cause="PAN OS returned an unexpected response.",
                                  assistance=f"Could not find group {group_name}, or group was empty. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {virtual_system}",
                                  data=response)

        found = False
        names = []
        for idx, name in enumerate(address_objects):
            if type(name) == str:
                names.append(name)
            else:
                names.append(name.get("#text"))

        if address_object_name in names:
            found = True
            names.remove(address_object_name)
            xml_str = self.make_xml(names, group_name)
            self.connection.request.edit_(xpath, xml_str)

        return {Output.SUCCESS: found}

    def make_xml(self, names, group_name):
        members = ""
        for name in names:
            members += f"<member>{name}</member>"

        xml_template = f"<entry name=\"{group_name}\"><static>{members}</static></entry>"

        return xml_template

