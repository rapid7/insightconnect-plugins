import komand
from .schema import CreateAddressObjectInput, CreateAddressObjectOutput, Input, Output, Component
# Custom imports below


class CreateAddressObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_address_object',
                description=Component.DESCRIPTION,
                input=CreateAddressObjectInput(),
                output=CreateAddressObjectOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/add-host"

        ip_address = params.get(Input.HOST_IP)
        name = params.get(Input.NAME)
        whitelist = params.get(Input.WHITELIST)
        skip_rfc1918 = params.get(Input.SKIP_RFC1918)



        payload = {
            "name": name,
            "ip-address": ip_address
        }

        color = params.get(Input.COLOR)

        if color:
            payload["color"] = color

        headers = self.connection.get_headers()
        result = self.connection.post_and_publish(headers, payload, url)

        return {Output.HOST_OBJECT: komand.helper.clean(result.json())}
