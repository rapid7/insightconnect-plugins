import komand
from .schema import CheckIfIpIsInAddressGroupsInput, CheckIfIpIsInAddressGroupsOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class CheckIfIpIsInAddressGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_ip_is_in_address_groups',
                description=Component.DESCRIPTION,
                input=CheckIfIpIsInAddressGroupsInput(),
                output=CheckIfIpIsInAddressGroupsOutput())

    def run(self, params={}):
        addrgrp = params.get(Input.ADDRESS_GROUP_NAME)
        ip_to_check = params.get(Input.IP_ADDRESS)
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{addrgrp}"
        result = self.connection.session.get(endpoint, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"unable to retrieve address group for {endpoint}\n",
                                  assistance=result.text,
                                  data=e)
        try:
            address_groups = result.json()
        except ValueError:
            raise PluginException(cause="data sent by Fortigate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=result.text)
        try:
            groups = address_groups["results"]
        except KeyError:
            raise PluginException(cause="No results were returned by Fortigate.\n",
                                  assistance="This is normally caused by an invalid address group name."
                                             " Double check that the address group name is correct")
        if len(groups) > 1:
            raise PluginException(cause="Fortigate returned more than one address group.\n",
                                  assistance="Contact support for help.",
                                  data=result.text)
        try:
            ips = groups[0]["member"]
        except KeyError:
            raise PluginException(cause="The address group date was malformed.\n",
                                  assistance="Contact support for help.",
                                  data=result.text)

        found = False
        for item in ips:
            if ip_to_check == item["name"]:
                found = True

        return {Output.IP_ADDRESS_FOUND: found}
