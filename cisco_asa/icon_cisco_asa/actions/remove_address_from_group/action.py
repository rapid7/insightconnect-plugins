import insightconnect_plugin_runtime
from .schema import RemoveAddressFromGroupInput, RemoveAddressFromGroupOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class RemoveAddressFromGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_address_from_group',
                description=Component.DESCRIPTION,
                input=RemoveAddressFromGroupInput(),
                output=RemoveAddressFromGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        group = self.connection.cisco_asa_api.get_group(group_name)
        address = params.get(Input.ADDRESS)
        if not group:
            raise PluginException(cause=f"The group {group_name} does not exist in Cisco ASA.",
                                  assistance="Please enter valid name and try again.")

        object_id = group.get("objectId")
        all_members = group.get("members")
        new_members = []
        for member in all_members:
            if member.get("value") == address:
                continue

            new_members.append(member)

        if len(new_members) == len(all_members):
            raise PluginException(cause=f"The address {address} does not exist in Cisco ASA in provided group.",
                                  assistance="Please enter valid address and try again.")

        self.connection.cisco_asa_api.update_group(object_id, group_name, new_members)

        return {
            Output.SUCCESS: True
        }
