import komand
from .schema import ConnectionSchema
# Custom imports below
import ipahttp


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        server = params.get('server')
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')

        self.ipa = ipahttp.ipa(server)
        self.ipa.login(username, password)
        self.logger.info("Connect: Connecting...")
