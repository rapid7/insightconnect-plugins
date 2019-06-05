import komand
from .schema import ConnectionSchema
# Custom imports below
import socket


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.proto, self.host, self.port, self.sock = None, None, None, None

    def connect(self, params):
        self.port = params.get('port', 514)
        self.host = params.get('host')
        self.proto = params.get('transport')

        if self.proto == 'TCP':
            self.logger.info('Connect: TCP socket requested')
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif self.proto == 'UDP':
            self.logger.info('Connect: UDP socket requested')
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            raise Exception("Error: Unhandled protocol selected! Please contact support for assistance.")

        if type(self.sock) is socket.socket:
            self.logger.info("Connect: Created socket object")
            self.sock.settimeout(10)
            self.logger.info("Connect: Setting socket timeout to 10 seconds")