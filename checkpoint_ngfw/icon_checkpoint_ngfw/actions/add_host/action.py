import komand
from .schema import AddHostInput, AddHostOutput, Input, Output, Component
# Custom imports below


class AddHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_host',
                description=Component.DESCRIPTION,
                input=AddHostInput(),
                output=AddHostOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/add-host"
        payload = {
            "name": params.get(Input.NAME),
            "ip-address": params.get(Input.HOST_IP)
        }
        headers = self.connection.get_headers()
        discard_other_changes = params.get(Input.DISCARD_OTHER_SESSIONS)

        result = self.connection.post_and_publish(headers, discard_other_changes, payload, url)

        return {Output.HOST_OBJECT: komand.helper.clean(result.json())}
