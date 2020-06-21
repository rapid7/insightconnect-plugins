import insightconnect_plugin_runtime
from .schema import CheckIfAddressInAddressGroupInput, CheckIfAddressInAddressGroupOutput, Input, Output, Component


# Custom imports below


class CheckIfAddressInAddressGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='check_if_address_in_address_group',
            description=Component.DESCRIPTION,
            input=CheckIfAddressInAddressGroupInput(),
            output=CheckIfAddressInAddressGroupOutput())

    def run(self, params={}):
        objects_matching = []
        name = params.get(Input.ADDRESS)

        # get address group and from that obtain all address object names assigned to that group
        address_group = self.connection.sonicwall_api.get_group(params.get(Input.GROUP))
        address_objects_names = []
        for ip in ['ipv4', 'ipv6']:
            address_object = address_group.get("address_group", {}).get(ip, {}).get("address_object", {})
            address_objects_names.extend(address_object.get("ipv4", []))
            address_objects_names.extend(address_object.get("ipv6", []))
            address_objects_names.extend(address_object.get("mac", []))
            address_objects_names.extend(address_object.get("fqdn", []))

        for object_from_group in address_objects_names:
            if object_from_group.get("name") == params.get(Input.ADDRESS):
                objects_matching.append(object_from_group)

        if len(objects_matching) == 0 and params.get(Input.ENABLE_SEARCH) is True:
            for object_from_group in address_objects_names:
                response = self.connection.sonicwall_api.get_address_object(object_from_group.get("name"))
                object_type = response.get("object_type", {})
                address_object = response.get("address_object", {}).get("address_object").get(object_type)
                upper_name = name.upper()
                if upper_name == address_object.get("address", "").upper()\
                        or upper_name.replace(":", "") == address_object.get("address", "").upper()\
                        or upper_name == address_object.get("host", {}).get("ip", "").upper()\
                        or upper_name == address_object.get("domain", "").upper():
                    objects_matching.append(address_object)

        return {
            Output.FOUND: len(objects_matching) > 0,
            Output.OBJECTS: objects_matching
        }
