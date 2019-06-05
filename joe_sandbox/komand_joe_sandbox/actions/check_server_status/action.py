import komand
from .schema import CheckServerStatusInput, CheckServerStatusOutput, Input, Output
# Custom imports below


class CheckServerStatus(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check_server_status',
                description='Check if Joe Sandbox is online or in maintenance mode',
                input=CheckServerStatusInput(),
                output=CheckServerStatusOutput())

    def run(self, params={}):
        is_server_online = self.connection.api.server_online()
        return is_server_online
