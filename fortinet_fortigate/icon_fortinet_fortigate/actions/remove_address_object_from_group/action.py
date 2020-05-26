import komand
from .schema import RemoveAddressObjectFromGroupInput, RemoveAddressObjectFromGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_fortinet_fortigate.util.util import Helpers


class RemoveAddressObjectFromGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_address_object_from_group',
                description=Component.DESCRIPTION,
                input=RemoveAddressObjectFromGroupInput(),
                output=RemoveAddressObjectFromGroupOutput())

    def run(self, params={}):
        group_name = params[Input.GROUP]
        address_object = params[Input.ADDRESS_OBJECT]
        helper = Helpers(self.logger)

        group = self.connection.get_address_group(group_name)
        group_members = group.get("member")
        if {"name": address_object} in group_members:
            group_members.remove({"name": address_object})
        else:
            return {Output.SUCCESS: False, Output.RESULT_OBJECT: f"The address object {address_object} was not in the group {group_name}"}

        group["member"] = group_members

        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{group.get('name')}"

        response = self.connection.session.put(endpoint, json=group, verify=self.connection.ssl_verify)

        try:
            json_response = response.json()
        except ValueError:
            raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)
        helper.http_errors(json_response, response.status_code)

        success = json_response.get("status", "").lower() == "success"

        return {Output.SUCCESS: success, Output.RESULT_OBJECT: json_response}
