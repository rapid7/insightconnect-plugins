import komand
from .schema import ConnectionSchema, Input
from komand_freegeoip.util.helpers import Ipstack


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.client = Ipstack(params.get(Input.CREDENTIALS).get("secretKey"))
