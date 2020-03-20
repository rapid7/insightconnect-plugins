import komand
from .schema import DeleteAddressObjectInput, DeleteAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class DeleteAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_address_object',
                description=Component.DESCRIPTION,
                input=DeleteAddressObjectInput(),
                output=DeleteAddressObjectOutput())

    def run(self, params={}):
        ip = params[Input.IP]
        cidr = params[Input.CIDR]

        address = f"{ip}/{cidr}"

        params_payload = {
            "mkey": address
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
