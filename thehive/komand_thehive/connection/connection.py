import komand
from .schema import ConnectionSchema
# Custom imports below
from thehive4py.api import TheHiveApi
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.password = None
        self.username = None
        self.verify = None
        self.client = None
        self.proxy = None

    def connect(self, params):
        url = '{}://{}:{}'.format(params.get('protocol'), params.get('host').rstrip('/'), params.get('port'))
        self.password = params.get('credentials').get('password')
        self.username = params.get('credentials').get('username')
        self.verify = params.get('verify', True)
        self.logger.info('URL: %s', url)

        if not params.get('proxy'):
            self.proxy = {}
        else:
            self.proxy = params.get('proxy')
            self.logger.info('Proxy specified: %s', self.proxy)

        self.logger.info("Connect: Connecting...")
        self.logger.info("SSL Verify: %s" % str(self.verify))
        self.client = TheHiveApi(url=url,
                                 principal=self.username,
                                 password=self.password,
                                 proxies=self.proxy,
                                 cert=self.verify)

    def test(self):
        client = self.client
        try:
            user = client.get_current_user()
        except requests.exceptions.HTTPError:
            self.logger.error('Test failed')
            raise
        return user.json()