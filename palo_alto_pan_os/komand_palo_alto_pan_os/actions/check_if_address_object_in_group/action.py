import komand
from .schema import CheckIfAddressObjectInGroupInput, CheckIfAddressObjectInGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from komand_palo_alto_pan_os.util.ip_check import IpCheck

class CheckIfAddressObjectInGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_address_object_in_group',
                description=Component.DESCRIPTION,
                input=CheckIfAddressObjectInGroupInput(),
                output=CheckIfAddressObjectInGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        address_to_check = params.get(Input.ADDRESS)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)

        xpath = f"/config/devices/entry[@name='{device_name}']/vsys/entry[@name='{virtual_system}']/address-group/entry[@name='{group_name}']"
        response = self.connection.request.get_(xpath)

        # Get the contents of the address group to check and extract all the address object names
        # Make the call and get the address group
        ip_objects = response.get("response", {}).get("result", {}).get("entry", {}).get("static")
        if not ip_objects:
            raise PluginException(cause="PAN OS returned an unexpected response.",
                                  assistance=f"Could not find group {group_name}, or group was empty. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {virtual_system}",
                                  data=response)

        # Extract all the address objects from the address group
        self.logger.info(f"Searching through {len(ip_objects)} address objects.")
        ip_object_names = []
        for member in ip_objects.get("member", {}):
            object_name = member.get("#text", "")
            if object_name:
                ip_object_names.append(object_name)

        # This is a helper to check addresses against address objects
        ip_checker = IpCheck()

        # This goes out and gets each address object by name, and attempts to pull the actual
        # IP, CIDR, or domain out of the return.
        #
        # The response format changes depending on the type of address object, and we need to handle
        # all of that
        for name in ip_object_names:
            # For each name, go and grab the Address Object
            object_xpath = f"/config/devices/entry[@name='{device_name}']/vsys/entry[@name='{virtual_system}']/address/entry[@name='{name}']"
            object_result = self.connection.request.get_(object_xpath)
            get_entry = object_result.get("response", {}).get("result", {}).get("entry", {})

            # Now try and deal with that address object
            if get_entry:
                # Find an entry that's either ip-something or fqdn
                key_to_get = list(filter(lambda x: (x.startswith("ip-") or x == "fqdn"), list(get_entry.keys())))[0]
                address_object = get_entry.get(key_to_get)

                # Depending on how PAN OS is feeling on a given day, it will either have a string or list returned
                # in the XML for the key we just found
                if type(address_object) is str:
                    if ip_checker.check_address_against_object(address_object, address_to_check):
                        return {Output.FOUND: True}
                else:
                    if ip_checker.check_address_against_object(address_object.get("#text", ""), address_to_check):
                        return {Output.FOUND: True}

        # That was a lot of work for nothing...bail out
        return {Output.FOUND: False}
