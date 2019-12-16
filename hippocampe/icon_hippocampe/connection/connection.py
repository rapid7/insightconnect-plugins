import komand
from .schema import ConnectionSchema
# Custom imports below
from icon_hippocampe.util.api import HippocampeAPI


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info('Connect: Connecting...')
        instance_url = params.get('url')
        self.api = HippocampeAPI(instance_url, self.logger)
        self.logger.info('Connect: Success')

    def test(self):
        self.api.distinct(['ip'])
