import komand
from .schema import ConnectionSchema
# Custom imports below
from komand_wordpress.util import helpers


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Discovering..")

        host = params.get('host')
        username = params.get('credentials').get('username')
        password = params.get('credentials').get('password')

        r = helpers.head_url(host)
        if not r or 'link' not in r.headers:
            raise Exception('Connect: Link header not found')

        link = r.headers.get('link')
        host = helpers.get_api_route(link)

        if not host:
            raise Exception('Connect: API route not found in Link header')

        #Replace with host info for local testing
        #if 'localhost' in host: host = 'http://192.168.145.101:8887/wp-json/'

        if not helpers.api_installed(host):
            raise Exception('Connect: APIv2 not installed')

        self.host = host
        self.username = username
        self.password = password

        self.logger.info("Connect: API root discovered at %s" % host)
