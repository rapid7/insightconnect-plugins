import komand
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from ipaddress import ip_network


class DeleteAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_address_object',
                description=Component.DESCRIPTION,
                input=DeleteAddressObjectInput(),
                output=DeleteAddressObjectOutput())

    def run(self, params={}):
        host = params[Input.HOST]

        # This will check if the host is an IP
        # If not it will check if the host ends with 2 chars. If this is true it is assumed to be a valid FQDN
        # Else it is assumed to be an invalid IP
        try:
            host = ip_network(host)
        except ValueError:
            if host[-1].isdigit() or host[-2].isdigit():
                raise PluginException(cause="The host input appears to be an invalid ip or domain name",
                                      assistance="Ensure that the host input is valid",
                                      data=host)
            pass

        params_payload = {
            "mkey": str(host)
        }

        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"

        response = self.connection.session.delete(endpoint, params=params_payload, verify=self.connection.ssl_verify)

        try:
            response.raise_for_status()
        except Exception as e:
            raise PluginException(cause="Delete address failed.",
                                  assistance=response.text,
                                  data=e)

        return {Output.SUCCESS: True, Output.RESPONSE_OBJECT: response.json()}
