import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from ipaddress import ip_network
from icon_fortinet_fortigate.util.util import Helpers


class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        host = params.get(Input.HOST)
        name = params.get(Input.NAME, "")
        whitelist = params.get(Input.WHITELIST)
        helper = Helpers(self.logger)

        # This will check if the host is an IP
        # If not it will check if the host ends with 2 chars. If this is true it is assumed to be a valid FQDN
        # Else it is assumed to be an invalid IP
        type_ = "ipmask"
        try:
            host = ip_network(host)
        except ValueError:
            if host[-1].isdigit() or host[-2].isdigit():
                raise PluginException(cause="The host input appears to be an invalid IP or domain name.",
                                      assistance="Ensure that the host input is a valid IP or domain.",
                                      data=host)
            type_ = "fqdn"

        found = False
        host = str(host)
        if whitelist:
            found = helper.match_whitelist(host, whitelist)
        if not found:
            payload = {
                "name": name if name else host,
                "type": type_,
                "subnet": host
                }

            endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"

            response = self.connection.session.post(endpoint, json=payload, verify=self.connection.ssl_verify)

            try:
                response.raise_for_status()
            except Exception as e:
                raise PluginException(cause=f"Create address failed with {endpoint}",
                                      assistance=response.text,
                                      data=e)

            return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: response.json()}

        return {Output.SUCCESS: False, Output.RESPONSE_OBJECT: {"message": "IP matched whitelist, skipping block action."}}
