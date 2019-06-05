import komand
from .schema import ConnectionSchema
# Custom imports below
from cortex4py.api import CortexApi


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):

        self.url = '{}://{}:{}'.format(params.get('protocol'), params.get('host'), params.get('port'))
        self.verify = params.get('verify', True)
        self.logger.info('URL: %s', self.url)

        if not params.get('proxy'):
            self.proxy = {}
        else:
            self.proxy = params.get('proxy')
            self.logger.info('Proxy specified: %s', self.proxy)

        self.logger.info("Connect: Connecting..")
        self.client = CortexApi(self.url, cert=self.verify, proxies=self.proxy)
