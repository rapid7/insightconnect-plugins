import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from ipaddress import ip_network


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

        # This will check if the host is an IP
        # If not it will check if the host ends with 2 chars. If this is true it is assumed to be a valid FQDN
        # Else it is assumed to be an invalid IP
        fqdn = False
        try:
            host = ip_network(host)
        except ValueError:
            if host[-1].isdigit() or host[-2].isdigit():
                raise PluginException(cause="The host input appears to be an invalid ip or domain name",
                                      assistance="Ensure that the host input is valid",
                                      data=host)
            fqdn = True

        if fqdn:
            payload = {
                "name": name if name else host,
                "type": "fqdn",
                "subnet": str(host)
            }
        else:
            payload = {
                "name": name if name else host,
                "type": "ipmask",
                "subnet": str(host)
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
