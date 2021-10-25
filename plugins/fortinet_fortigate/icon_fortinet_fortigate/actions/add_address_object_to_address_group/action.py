import insightconnect_plugin_runtime
from .schema import (
    AddAddressObjectToAddressGroupInput,
    AddAddressObjectToAddressGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddAddressObjectToAddressGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_address_object_to_address_group",
            description=Component.DESCRIPTION,
            input=AddAddressObjectToAddressGroupInput(),
            output=AddAddressObjectToAddressGroupOutput(),
        )

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        ipv6_group_name = params.get(Input.IPV6_GROUP)
        address_name = params.get(Input.ADDRESS_OBJECT)

        is_ipv6 = self.connection.api.get_address_object(address_name)["name"] == "address6"

        if is_ipv6:
            group = self.connection.api.get_address_group(ipv6_group_name, is_ipv6)
            endpoint = f"firewall/addrgrp6/{ipv6_group_name}"
        else:
            group = self.connection.api.get_address_group(group_name, is_ipv6)
            endpoint = f"firewall/addrgrp/{group_name}"

        group_members = group.get("member")
        group_members.append({"name": address_name})
        group["member"] = group_members

        response = self.connection.api.modify_objects_in_group(endpoint, group)

        return {Output.SUCCESS: response.get("status", "").lower() == "success", Output.RESULT_OBJECT: response}
