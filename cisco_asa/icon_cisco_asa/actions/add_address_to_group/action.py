import insightconnect_plugin_runtime
from .schema import AddAddressToGroupInput, AddAddressToGroupOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import validators


class AddAddressToGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_address_to_group',
                description=Component.DESCRIPTION,
                input=AddAddressToGroupInput(),
                output=AddAddressToGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        group = self.connection.cisco_asa_api.get_group(group_name)
        address = params.get(Input.ADDRESS)
        if not group:
            raise PluginException(cause=f"The group {group} does not exist in Cisco ASA.",
                                  assistance="Please enter valid name and try again.")

        object_id = group.get("objectID")
        all_members = group.get("members")
        found = False
        for member in all_members:
            if member.get("value") == address:
                found = True
                break

        if not found:
            all_members.append({
                "kind": self._get_kind(address),
                "value": address
            })

            self.connection.cisco_asa_api.add_to_group(object_id, group_name, all_members)

        return {
            Output.SUCCESS: True
        }

    @staticmethod
    def _get_kind(address: str):
        if validators.ipv4(address):
            return "IPv4Address"
        elif validators.ipv6(address):
            return "IPv6Address"
        elif validators.ipv4_cidr(address):
            return "IPv4Network"

        raise PluginException(
            cause=f"Kind not detected from address: {address}",
            assistance="Check address input and try again. Allowed kind are: "
                       "IPv4Address, IPv6Address, IPv4Network."
        )
