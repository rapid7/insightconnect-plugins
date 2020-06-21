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

        # get address group and from that obtain all address object names assigned to that group
        address_group = self.connection.sonicwall_api.get_address_group(params.get(Input.GROUP))
        address_objects_names = []
        for address_group in address_group.get("address_groups", []):
            for ip in ['ipv4', 'ipv6']:
                address_object = address_group.get(ip, {}).get("address_object", {})
                address_objects_names.extend(address_object.get("ipv4", []))
                address_objects_names.extend(address_object.get("ipv6", []))
                address_objects_names.extend(address_object.get("mac", []))
                address_objects_names.extend(address_object.get("fqdn", []))

        for adr_obj in address_objects_names:
            if adr_obj.get("name") == params.get(Input.ADDRESS):
                objects_matching.append(adr_obj)

        if len(objects_matching) == 0 and params.get(Input.ENABLE_SEARCH) is True:
            objects_matching.append(self.connection.sonicwall_api.get_address_object(params.get(Input.ADDRESS)))

        return {
            Output.FOUND: len(objects_matching) > 0,
            Output.OBJECTS: objects_matching
        }
