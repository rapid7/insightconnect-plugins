import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_rapid7_tcell.util.api import TCell


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Connect: Connecting...')

        api_key = params.get('api_key')['secretKey']
        self.api = TCell(api_key, self.logger)

        self.logger.info('Connect: Connected successfully')

    def test(self):
        # Since `connect` tests the API when creating a TCell instance, if we
        # got to this point, the API is working and the API key is correct
        return {'Connection test successful': True}
