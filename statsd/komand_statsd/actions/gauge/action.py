import komand
from .schema import GaugeInput, GaugeOutput
# Custom imports below
import socket


class Gauge(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='gauge',
                description='This action is used to set a gauge value',
                input=GaugeInput(),
                output=GaugeOutput())

    def run(self, params={}):
        instance = self.connection.instance
        stat = params.get('stat')
        value = params.get('value')
        rate = params.get('rate', 1)
        delta = params.get('delta', 1)
        instance.gauge(stat, value, rate, delta)
        return { 'stat': stat, 'value': value }

    def test(self):
        host = self.connection.host
        port = self.connection.port
        protocol = self.connection.protocol
        try:
            socket.inet_aton(host) # Check if is correct ip address
        except socket.error: # DNS
            try:
                socket.gethostbyname(host)
            except socket.error:
                self.logger.error('Hostname %s cannot be resolved by DNS' % host)
                raise
        if protocol == 'TCP':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5) # Setting 5 sec of timeout
            result = sock.connect_ex((host,port))
            if result != 0:
                self.logger.error('Port %d is not open' % port)
                raise Exception
        return { 'host': host, 'port': port, 'protocol': protocol }
