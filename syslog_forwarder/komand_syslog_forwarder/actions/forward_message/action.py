import komand
from .schema import ForwardMessageInput, ForwardMessageOutput
# Custom imports below
import re
import socket
from komand_syslog_forwarder.util import utils


class ForwardMessage(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='forward_message',
            description='Forward syslog message',
            input=ForwardMessageInput(),
            output=ForwardMessageOutput())

    def run(self, params={}):
        sock = self.connection.sock
        dsthost = self.connection.host
        port = self.connection.port
        proto = self.connection.proto
        host = params.get('host')
        msgid = params.get('msgid')
        proc = params.get('proc')
        if not host:
            host = 'komand'
        if not msgid:
            msgid = 'ACTION'
        if not proc:
            proc = 'komand-engine'

        # Add syslog header to message
        data = utils.add_header(
            params.get('msg'),
            utils.facility[params.get('facility')],
            utils.level[params.get('level')],
            host,
            msgid,
            proc
        )
        data_len = len(data)

        try:
            if proto == 'UDP':
                sent = sock.sendto(data, (dsthost, port))
            elif proto == 'TCP':
                sock.connect((dsthost, port))
                sent = sock.send(data)
            else:
                raise Exception("Error: Unhandled protocol selected! Please contact support for assistance.")

            if sent != data_len:
                self.logger.info("Run: Sent bytes didn't match input")
        finally:
            self.logger.info('Run: Message successfully sent')
            sock.close()
            return {}

    def test(self):
        sock = self.connection.sock
        dsthost = self.connection.host
        port = self.connection.port
        proto = self.connection.proto
        fail = False

        # Test Name Resolution
        r = re.search('[a-zA-Z-]', dsthost)
        if r is not None:
            self.logger.error('Test: Resolving name %s', dsthost)
            try:
                socket.gethostbyname(dsthost)
            except socket.gaierror:
                self.logger.error('Test: Resolution failed')
                fail = True

        # Test TCP Connection
        if proto == 'TCP':
            try:
                sock.connect((dsthost, port))
            except socket.timeout as err:
                self.logger.error('Test: Socket %s', err)
                fail = True
            except socket.error as err:
                self.logger.error('Test: Socket error %s', err)
                fail = True
            sock.close()
        if fail:
            raise Exception('Test: Failed')
        return {}
