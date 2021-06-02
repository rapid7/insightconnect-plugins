import komand
from .schema import (
    AddAddressObjectToAddressGroupInput,
    AddAddressObjectToAddressGroupOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from komand.exceptions import PluginException
from icon_fortinet_fortigate.util.util import Helpers


class AddAddressObjectToAddressGroup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_address_object_to_address_group",
            description=Component.DESCRIPTION,
            input=AddAddressObjectToAddressGroupInput(),
            output=AddAddressObjectToAddressGroupOutput(),
        )

    def run(self, params={}):
        group_name = params[Input.GROUP]
        address_name = params[Input.ADDRESS_OBJECT]
        helper = Helpers(self.logger)

        is_ipv6 = self.connection.get_address_object(address_name)["name"] == "address6"

        group = self.connection.get_address_group(group_name, is_ipv6)
        group_members = group.get("member")

        group_members.append({"name": address_name})
        group["member"] = group_members

        endpoint = self._determine_endpoint(is_ipv6, group_name)

        response = self.connection.session.put(endpoint, json=group, verify=self.connection.ssl_verify)

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(
                cause="Data sent by FortiGate was not in JSON format.\n",
                assistance="Contact support for help.",
                data=response.text,
            )

        if json_response.get("error", 0) == -3:
            raise PluginException(
                cause=f"Add address object to address group failed: {endpoint}\n",
                assistance="The error code returned was -3. This usually indicates"
                "that the address object specified could not be found.",
                data=response.text,
            )
        helper.http_errors(json_response, response.status_code)

        success = json_response.get("status", "").lower() == "success"

        return {Output.SUCCESS: success, Output.RESULT_OBJECT: json_response}

    def _determine_endpoint(self, is_ipv6, group_name):
        if is_ipv6:
            return f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp6/{group_name}"

        return f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{group_name}"
