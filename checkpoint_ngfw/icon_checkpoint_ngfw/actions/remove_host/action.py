import komand
from .schema import RemoveHostInput, RemoveHostOutput, Input, Output, Component
# Custom imports below


class RemoveHost(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_host',
                description=Component.DESCRIPTION,
                input=RemoveHostInput(),
                output=RemoveHostOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/delete-host"
        payload = {
            "name": params.get(Input.NAME),
        }
        headers = self.connection.get_headers()
        discard_other_changes = params.get(Input.DISCARD_OTHER_SESSIONS)

        result = self.connection.post_and_publish(headers, discard_other_changes, payload, url)

        return {Output.MESSAGE: result.json().get("message"),
                Output.SUCCESS: True}
