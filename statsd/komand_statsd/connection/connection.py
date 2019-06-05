import komand
from .schema import ConnectionSchema
# Custom imports below
import statsd


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")

        host = params.get('host')
        port = params.get('port')
        prefix = params.get('prefix', None)
        protocol = params.get('protocol')

        self.host = host
        self.port = port
        self.protocol = protocol

        if protocol == 'TCP':
            timeout = params.get('tcp', None)['timeout']
            timeout = None if timeout == 0 else timeout
            self.instance = statsd.TCPStatsClient(host, port, prefix, timeout)
        elif protocol == 'UDP':
            maxudpsize = params.get('udp', 512)
            if maxudpsize is not None:
                maxudpsize = maxudpsize['maxudpsize']
            self.instance = statsd.StatsClient(host, port, prefix, maxudpsize)
