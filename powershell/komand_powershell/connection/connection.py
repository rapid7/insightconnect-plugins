import komand
from .schema import ConnectionSchema


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.username = params.get('credentials').get('username')
        self.password = params.get('credentials').get('password')
        self.auth_type = params.get('auth')
        self.port = params.get('port')
        self.domain = params.get('kerberos').get('domain_name')
        self.kdc = params.get('kerberos').get('kdc')

        self.logger.info("Connect: Connecting..")
