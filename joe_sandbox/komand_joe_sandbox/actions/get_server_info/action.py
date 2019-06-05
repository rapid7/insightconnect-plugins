import komand
from .schema import GetServerInfoInput, GetServerInfoOutput, Input, Output
# Custom imports below


class GetServerInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_server_info',
                description='Query information about the server',
                input=GetServerInfoInput(),
                output=GetServerInfoOutput())

    def run(self, params={}):
        server_info = self.connection.api.server_info()
        return server_info
