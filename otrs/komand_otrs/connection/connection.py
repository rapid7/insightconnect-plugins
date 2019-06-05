import komand
from .schema import ConnectionSchema
# Custom imports below
from pyotrs import Client


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.server = None
        self.user_login = None
        self.password = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        server = params.get('server', '')
        user_login = params.get('credentials').get('username', '')
        password = params.get('credentials').get('password', '')

        self.server = server
        self.user_login = user_login
        self.password = password

        self.client = Client(server, user_login, password)


    def test(self):
        try:
            self.client.session_create()
        except Exception as e:
            raise Exception("Unable to connect to OTRS webservice! Please check your connection information and \
            that you have properly configured OTRS webservice. Information on configuring the webservice can be found \
            in the Connection help")
        return {}