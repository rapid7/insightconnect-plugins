import komand
from socket import *
from .schema import KnockInput, KnockOutput


class Knock(komand.Action):

    __IP_HOST = None

    # Use as an enum
    class PacketType:
        TCP = "TCP"
        UDP = "UDP"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='knock',
                description='Knocks the specified ports on a host',
                input=KnockInput(),
                output=KnockOutput())

    def run(self, params={}):
        self.__IP_HOST = params.get("host")
        port_pairs = params.get("ports")

        for port_pair in port_pairs:
            split_pair = port_pair.partition("/")
            port, protocol = int(split_pair[0]), split_pair[2].upper()

            if protocol == self.PacketType.TCP:
                self.tcp_knock(port)
            elif protocol == self.PacketType.UDP:
                self.udp_knock(port)
            else:
                raise Exception("Invalid packet type passed in")

        return {}

    def tcp_knock(self, port):
        self.logger.info("TCP Knock: Using TCP for packet type")

        try:
            s = socket()
            s.settimeout(1)
            self.logger.info("TCP Knock: Knocking {ip}:{port}".format(ip=self.__IP_HOST, port=port))
            s.connect((self.__IP_HOST, port))
            s.shutdown(1)
            s.close()
        except error:
            self.logger.info("TCP Knock: No response from server (this does not mean a failed knock)")

    def udp_knock(self, port):
        self.logger.info("UDP Knock: Using UDP for packet type")

        try:
            s = socket(AF_INET, SOCK_DGRAM)
            s.sendto(bytes("1", "utf-8"), (self.__IP_HOST, port))
        except error:
            self.logger.info("UDP Knock: No response from server (this does not mean a failed knock)")

    def test(self):
        """TODO: Test action"""
        return {}
