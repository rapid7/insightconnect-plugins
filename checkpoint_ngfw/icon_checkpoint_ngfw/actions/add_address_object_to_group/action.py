import komand
from .schema import AddAddressObjectToGroupInput, AddAddressObjectToGroupOutput, Input, Output, Component
# Custom imports below


class AddAddressObjectToGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_address_object_to_group',
                description=Component.DESCRIPTION,
                input=AddAddressObjectToGroupInput(),
                output=AddAddressObjectToGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP)
        host_name = params.get(Input.ADDRESS_OBJECT)

        url = f"{self.connection.server_and_port}/web_api/set-group"
        payload = {
            "name": group_name,
            "members": {
                "add": host_name
            }
        }
        headers = self.connection.get_headers()

        self.connection.post_and_publish(headers, payload, url)

        # There's no message to check on the return...if no exceptions are thrown
        # it succeeded
        return {Output.SUCCESS: True}
