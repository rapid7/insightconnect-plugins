import komand
from .schema import AddHostToNetworkGroupInput, AddHostToNetworkGroupOutput, Input, Output, Component
# Custom imports below


class AddHostToNetworkGroup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_host_to_network_group',
                description=Component.DESCRIPTION,
                input=AddHostToNetworkGroupInput(),
                output=AddHostToNetworkGroupOutput())

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        host_name = params.get(Input.HOST_NAME)
        discard_other_sessions = params.get(Input.DISCARD_OTHER_SESSIONS)

        url = f"{self.connection.server_and_port}/web_api/set-group"
        payload = {
            "name": group_name,
            "members": {
                "add": host_name
            }
        }
        headers = self.connection.get_headers()

        self.connection.post_and_publish(headers, discard_other_sessions, payload, url)

        # There's no message to check on the return...if no exceptions are thrown
        # it succeeded
        return {Output.SUCCESS: True}
