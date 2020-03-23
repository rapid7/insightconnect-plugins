import komand
from .schema import ConnectionSchema
# Custom imports below
import jenkins


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        host = params.get('host')

        self.logger.info("Connect: Connecting...")

        self.server = jenkins.Jenkins(host, username=username, password=password)

    def test(self):
        user = self.server.get_whoami()
        return {'user': user}

