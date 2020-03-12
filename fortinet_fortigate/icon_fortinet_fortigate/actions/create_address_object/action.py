import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException

class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        ip = params[Input.IP]
        cidr = params[Input.CIDR]

        address = f"{ip}/{cidr}"

        payload = {
            "name": ip,
            "type": "ipmask",
            "subnet": address
        }

        endpoint = f"https://{self.connection.host}/api/v2/cmdb/firewall/address"

        response = self.connection.session.post(endpoint, json=payload, verify=self.connection.ssl_verify)

        try:
            response.raise_for_status()
        except Exception as e:
            raise PluginException(cause="Create address failed.",
                                  assistance=response.text,
                                  data=e)

        return {Output.SUCCESS:True, Output.RESPONSE_OBJECT: response.json()}
