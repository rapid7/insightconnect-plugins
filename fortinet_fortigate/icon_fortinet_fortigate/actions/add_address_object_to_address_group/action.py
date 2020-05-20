import komand
from .schema import AddAddressObjectToAddressGroupInput, AddAddressObjectToAddressGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class AddAddressObjectToAddressGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_address_object_to_address_group',
                description=Component.DESCRIPTION,
                input=AddAddressObjectToAddressGroupInput(),
                output=AddAddressObjectToAddressGroupOutput())

    def run(self, params={}):
        group_name = params[Input.GROUP]
        address_name = params[Input.ADDRESS_OBJECT]

        group = self.connection.get_address_group(group_name)
        group_members = group.get("member")

        group_members.append({"name": address_name})
        group["member"] = group_members

        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{group.get('name')}"

        response = self.connection.session.put(endpoint, json=group, verify=self.connection.ssl_verify)

        try:
            response.raise_for_status()
        except Exception as e:
            json_obj = {}
            try:
                json_obj = response.json()
            except Exception as err:
                self.throw_unknown_error(err, endpoint, response)
            if json_obj.get("error", 0) == -3:
                raise PluginException(cause=f"Add address object to address group failed: {endpoint}\n",
                                      assistance="The error code returned was -3. This usually indicates"
                                                 "that the address object specified could not be found.",
                                      data=e)

            self.throw_unknown_error(e, endpoint, response)

        json_response = response.json()
        success = json_response.get("status", "").lower() == "success"

        return {Output.SUCCESS: success, Output.RESULT_OBJECT: json_response}

    def throw_unknown_error(self, e, endpoint, response):
        raise PluginException(cause=f"Add address object to address group failed: {endpoint}\n",
                              assistance=response.text,
                              data=e)
