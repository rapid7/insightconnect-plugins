import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_mimecast.util.util import Authentication


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        # set Variables
        self.url = params.get('url')
        self.username = params.get('credentials').get('username')
        self.password = params.get('credentials').get('password')
        self.app_id = params.get('app_id')
        self.auth_type = params.get('auth_type')
        self.app_key = params.get('app_key').get('secretKey')
        self.logger.info("Connect: Connecting...")

        # Create Connection
        connection = Authentication()
        keys = connection.login(url=self.url, username=self.username, password=self.password,
                                auth_type=self.auth_type, app_id=self.app_id)

        # Export keys
        try:
            self.access_key = keys['access_key']
            self.secret_key = keys['secret_key']
        except KeyError:
            raise Exception('An unknown authentication error has occurred. If the issue persists, please contact support')

    def test(self):
            logout = Authentication()
            logout.logout(url=self.url, username=self.username,
                          password=self.password, auth_type=self.auth_type,
                          access_key=self.access_key,
                          secret_key=self.secret_key, app_id=self.app_id,
                          app_key=self.app_key)
            return {'connection': 'successful'}
