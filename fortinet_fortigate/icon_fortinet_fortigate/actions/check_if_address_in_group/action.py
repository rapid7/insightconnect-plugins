import komand
from .schema import CheckIfAddressInGroupInput, CheckIfAddressInGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class CheckIfAddressInGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_address_in_group',
                description=Component.DESCRIPTION,
                input=CheckIfAddressInGroupInput(),
                output=CheckIfAddressInGroupOutput())

    def run(self, params={}):
        addrgrp = params.get(Input.GROUP)
        ip_to_check = params.get(Input.ADDRESS)
        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{addrgrp}"
        result = self.connection.session.get(endpoint, verify=self.connection.ssl_verify)

        try:
            result.raise_for_status()
        except Exception as e:
            raise PluginException(cause=f"Unable to retrieve address group for {endpoint}\n",
                                  assistance=result.text,
                                  data=e)
        try:
            address_groups = result.json()
        except ValueError:
            raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=result.text)
        try:
            groups = address_groups["results"]
        except KeyError:
            raise PluginException(cause="No results were returned by FortiGate.\n",
                                  assistance="This is normally caused by an invalid address group name."
                                             " Double check that the address group name is correct")
        if len(groups) > 1:
            raise PluginException(cause="FortiGate returned more than one address group.\n",
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

        return {Output.FOUND: found}
