import komand
from .schema import ConnectionSchema
# Custom imports below
from openvas_lib import VulnscanManager, VulnscanException


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Attempting to connect to OpenVAS Server...')
        self.username = str(params.get('credentials').get('username'))
        self.password = str(params.get('credentials').get('password'))
        self.server = params.get('server', '127.0.0.1:9393')
        self.timeout = params.get('timeout', '10')
        self.ssl_verify = params.get('ssl_verify')
        try:
            self.server_host = str(self.server.split(':')[0])
            self.server_port = int(self.server.split(':')[1])
        except IndexError as e:
            self.logger.error('Error connecting to OpenVAS Server: Invalid format of server string - requires IPAddress:Port - for example, 127.0.0.1:9390')
        try:
            self.scanner = VulnscanManager(self.server_host, self.username, self.password, self.server_port, self.timeout, self.ssl_verify)
        except Exception as err:
            self.logger.error('Error connecting to OpenVAS Server: ' + str(err))
            raise Exception('Connection to OpenVAS server failed, ' + str(err))

        self.logger.info('Connected to server ' + self.server)
