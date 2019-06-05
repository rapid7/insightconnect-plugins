import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None
        self.token = None
        self.username = None
        self.password = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        url = params.get('url')
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        token = params.get('api_key').get('secretKey')

        self.url = url

        if token:
            self.token = token
            self.username = None
            self.password = None
            self.logger.info('Connect: Authorized Service Token will be used')
        elif not username or not password:
            raise Exception('Connect: Neither basic auth nor token supplied')
        else:
            self.token = None
            self.username = username
            self.password = password
            self.logger.info('Connect: (WARNING) Basic Auth will be used')
