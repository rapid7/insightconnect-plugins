import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
import ipaddress
from icon_fortinet_fortigate.util.util import Helpers


class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        host = params.get(Input.ADDRESS)
        name = params.get(Input.ADDRESS_OBJECT, "")
        whitelist = params.get(Input.WHITELIST)
        skip_rfc1918 = params.get(Input.SKIP_RFC1918)
        helper = Helpers(self.logger)

        type_ = helper.determine_address_type(host)
        if type_ == "ipmask":
            host = helper.ipmaskConverter(host)
        # White_list expects a IP rather than a CIDR, The rest of this action requires a CIRD
        # whitelist_ref will save a version of the host without the CIRD
        whitelist_ref = host
        if host.endswith("/32"):
            whitelist_ref = host[:-3]

        if type_ == "ipmask" and skip_rfc1918 is True and ipaddress.ip_network(host).is_private:
            return {Output.SUCCESS: False,
                    Output.RESPONSE_OBJECT: {"message": f"The IP address specified ({host}) is private and will be ignored as per "
                                                        f"the action configuration."}}

        found = False
        if whitelist:
            found = helper.match_whitelist(whitelist_ref, whitelist)
        if not found:
            payload = {
                "name": name if name else host,
                "type": type_,
                "subnet": host
                }

            endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"

            response = self.connection.session.post(endpoint, json=payload, verify=self.connection.ssl_verify)
            try:
                json_response = response.json()
            except ValueError:
                raise PluginException(cause="Data sent by FortiGate was not in JSON format.\n",
                                      assistance="Contact support for help.",
                                      data=response.text)
            helper.http_errors(json_response, response.status_code)

            return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: json_response}

        return {Output.SUCCESS: False, Output.RESPONSE_OBJECT: {"message": "IP matched whitelist, skipping block action."}}
