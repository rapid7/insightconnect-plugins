import insightconnect_plugin_runtime
from .schema import CheckIfAddressObjectInGroupInput, CheckIfAddressObjectInGroupOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import ipaddress


class CheckIfAddressObjectInGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='check_if_address_object_in_group',
            description=Component.DESCRIPTION,
            input=CheckIfAddressObjectInGroupInput(),
            output=CheckIfAddressObjectInGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        address_to_check = params.get(Input.ADDRESS)
        enable_search = params.get(Input.ENABLE_SEARCH)

        found = False
        object_names_to_return = []
        if enable_search:
            object_results = self.connection.cisco_asa_api.get_objects().get('items', [])
            self.logger.info(f"Searching through {len(object_results)} address objects.")

            for item in object_results:
                if address_to_check == item.get("name") \
                        or address_to_check == item.get("objectId") \
                        or self._check_address(item.get("host", {}).get("value"), address_to_check):
                    object_names_to_return.append(item)
                    found = True
        else:
            response = self.connection.cisco_asa_api.get_group(group_name)
            ip_objects = response.get("members", [])
            self.logger.info(f"Searching through {len(ip_objects)} address objects.")
            for item in ip_objects:
                if self._check_address(item, address_to_check):
                    object_names_to_return.append(item)
                    found = True

        return {
            Output.FOUND: found,
            Output.ADDRESS_OBJECTS: object_names_to_return
        }

    @staticmethod
    def _check_address(host_value, address_to_check):
        return address_to_check == host_value \
            or ("/" in host_value and address_to_check in ipaddress.ip_network(host_value).hosts()) \
            or ("/" in address_to_check and host_value in ipaddress.ip_network(address_to_check).hosts())
