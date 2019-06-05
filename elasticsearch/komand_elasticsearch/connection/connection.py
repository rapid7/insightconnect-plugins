import komand
from .schema import ConnectionSchema
# Custom imports below


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        url = params.get('url')
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        authentication = params.get('use_authentication')

        self.elastic_host = url
        if not authentication:
            self.logger.info('Connect: Warning, No Auth Provided')
            self.username = None
            self.password = None
        else:
            self.username = username
            self.password = password
