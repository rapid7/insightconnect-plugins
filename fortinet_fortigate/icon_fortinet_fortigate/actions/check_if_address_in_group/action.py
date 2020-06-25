import komand
from .schema import CheckIfAddressInGroupInput, CheckIfAddressInGroupOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import ipaddress
from icon_fortinet_fortigate.util.util import Helpers


class CheckIfAddressInGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_if_address_in_group',
                description=Component.DESCRIPTION,
                input=CheckIfAddressInGroupInput(),
                output=CheckIfAddressInGroupOutput())

    def run(self, params={}):
        addrgrp = params.get(Input.GROUP)
        address_to_check = params.get(Input.ADDRESS)
        enable_search = params.get(Input.ENABLE_SEARCH)
        helper = Helpers(self.logger)

        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/addrgrp/{addrgrp}"
        response = self.connection.session.get(endpoint, verify=self.connection.ssl_verify)

        try:
            address_data = response.json()
        except ValueError:
            raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)

        helper.http_errors(address_data, response.status_code)

        try:
            groups = address_data["results"]
        except KeyError:
            raise PluginException(cause="No results were returned by FortiGate.\n",
                                  assistance="This is normally caused by an invalid address group name."
                                             " Double check that the address group name is correct")
        if len(groups) > 1:
            raise PluginException(cause="FortiGate returned more than one address group.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)
        try:
            address_objects = groups[0]["member"]
        except KeyError:
            raise PluginException(cause="The address group date was malformed.\n",
                                  assistance="Contact support for help.",
                                  data=response.text)

        found = False
        addresses_found = list()

        if enable_search:
            for item in address_objects:
                name = item["name"]
                endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address/{name}"
                response = self.connection.session.get(endpoint, verify=self.connection.ssl_verify)
                try:
                    address_data = response.json()
                except ValueError:
                    raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                          assistance="Contact support for help.",
                                          data=response.text)

                helper.http_errors(address_data, response.status_code)

                try:
                    results = address_data["results"]
                except KeyError:
                    raise PluginException(cause="No results were returned by FortiGate.\n",
                                          assistance="This is normally caused by an invalid address group name."
                                                     " Double check that the address group name is correct")
                for result in results:
                    # If address_object is a fqdn
                    if result["type"] == "fqdn":
                        if address_to_check == result["fqdn"]:
                            addresses_found.append(result["fqdn"])
                            found = True
                    # If address_object is a ipmask
                    if result["type"] == "ipmask":
                        # Convert returned address to CIDR
                        ipmask = result["subnet"].replace(" ", "/")
                        ipmask = ipaddress.IPv4Network(ipmask)

                        # Convert given address to CIDR address to CIDR
                        try:
                            address_to_check = ipaddress.IPv4Network(address_to_check)
                        except ipaddress.AddressValueError:
                            pass

                        if address_to_check == ipmask:
                            addresses_found.append(str(ipmask))
                            found = True
                    # This only looks for ipmasks (IP or CIDR) and FQDN's.
                    # Other address types like mac address are not searchable at present
            return {Output.FOUND: found, Output.ADDRESS_OBJECTS: addresses_found}

        for item in address_objects:
            if address_to_check == item["name"]:
                addresses_found.append(item["name"])
                found = True

        return {Output.FOUND: found, Output.ADDRESS_OBJECTS: addresses_found}
