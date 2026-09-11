import insightconnect_plugin_runtime
from .schema import CheckIfAddressObjectInGroupInput, CheckIfAddressObjectInGroupOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_palo_alto_pan_os.util.ip_check import IpCheck
from komand_palo_alto_pan_os.util.util import extract_static_members, get_response_entry


class CheckIfAddressObjectInGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_if_address_object_in_group",
            description=Component.DESCRIPTION,
            input=CheckIfAddressObjectInGroupInput(),
            output=CheckIfAddressObjectInGroupOutput(),
        )

    def run(self, params={}):  # noqa: MC0001
        group_name = params.get(Input.GROUP)
        address_to_check = params.get(Input.ADDRESS)
        device_name = params.get(Input.DEVICE_NAME)
        virtual_system = params.get(Input.VIRTUAL_SYSTEM)
        enable_search = params.get(Input.ENABLE_SEARCH)

        response = self.connection.request.get_address_group(
            device_name=device_name, virtual_system=virtual_system, group_name=group_name
        )

        # Get the contents of the address group to check and extract all the address object names
        # Make the call and get the address group
        entry = get_response_entry(response)
        if entry is None:
            raise PluginException(
                cause="PAN OS returned an unexpected response.",
                assistance=f"Could not find group '{group_name}', or group was empty. Check the name, virtual system name, and device name.\ndevice name: {device_name}\nvirtual system: {virtual_system}",
                data=response,
            )

        # Extract all the address objects from the address group
        ip_object_names = extract_static_members(entry, group_name)
        self.logger.info(f"Searching through {len(ip_object_names)} address objects.")

        # If enable search is false, we just want to see if the address to check matches an address object
        # If enable search is true, we have to look in each address object for address to check
        if not enable_search:
            for name in ip_object_names:
                if name == address_to_check:
                    return {Output.FOUND: True, Output.ADDRESS_OBJECTS: [name]}
        else:  # enable_search is false
            # This is a helper to check addresses against address objects
            ip_checker = IpCheck()

            # This goes out and gets each address object by name, and attempts to pull the actual
            # IP, CIDR, or domain out of the return.
            #
            # The response format changes depending on the type of address object, and we need to handle
            # all of that
            object_names_to_return = []
            found = False
            for name in ip_object_names:
                # For each name, go and grab the Address Object
                object_result = self.connection.request.get_address_object(
                    device_name=device_name, virtual_system=virtual_system, object_name=name
                )

                get_entry = get_response_entry(object_result)
                if get_entry is None:
                    raise PluginException(
                        cause="PAN OS returned an unexpected response.",
                        assistance=f"Address object '{name}' was not found. Check the name and try again.",
                        data=object_result,
                    )

                # Now try and deal with that address object
                if get_entry:
                    # Find an entry that's either ip-something or fqdn
                    key_to_get = list(filter(lambda x: (x.startswith("ip-") or x == "fqdn"), list(get_entry.keys())))[0]
                    address_object = get_entry.get(key_to_get)

                    # Depending on how PAN OS is feeling on a given day, it will either have a string or list returned
                    # in the XML for the key we just found
                    if isinstance(address_object, str):
                        if ip_checker.check_address_against_object(address_object, address_to_check):
                            object_names_to_return.append(name)
                            found = True
                    else:
                        if ip_checker.check_address_against_object(address_object.get("#text", ""), address_to_check):
                            object_names_to_return.append(name)
                            found = True

            if found:
                return {Output.FOUND: True, Output.ADDRESS_OBJECTS: object_names_to_return}

        # That was a lot of work for nothing...bail out
        return {Output.FOUND: False, Output.ADDRESS_OBJECTS: []}
