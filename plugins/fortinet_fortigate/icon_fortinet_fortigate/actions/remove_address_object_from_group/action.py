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


class RemoveAddressObjectFromGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_address_object_from_group",
            description=Component.DESCRIPTION,
            input=RemoveAddressObjectFromGroupInput(),
            output=RemoveAddressObjectFromGroupOutput(),
        )

    def run(self, params={}):
        group_name = params[Input.GROUP]
        address_object = params[Input.ADDRESS_OBJECT]

        is_ipv6 = self.connection.api.get_address_object(address_object).get("name") == "address6"

        if is_ipv6:
            group_name = params.get(Input.IPV6_GROUP)
            group = self.connection.api.get_address_group(group_name, is_ipv6)
            endpoint = f"firewall/addrgrp6/{group_name}"
        else:
            group = self.connection.api.get_address_group(group_name, is_ipv6)
            endpoint = f"firewall/addrgrp/{group_name}"

        group_members = group.get("member")
        found = False
        for item in group_members:
            if "name" in item and address_object == item["name"]:
                group_members.remove(item)
                found = True

        if not found:
            return {
                Output.SUCCESS: False,
                Output.RESULT_OBJECT: {
                    "message": f"The address object {address_object} was not in the group {group_name}"
                },
            }

        group["member"] = group_members

        response = self.connection.api.modify_objects_in_group(endpoint, group)

        return {Output.SUCCESS: response.get("status", "").lower() == "success", Output.RESULT_OBJECT: response}
