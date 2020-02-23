import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
# Custom imports below
from komand_wordpress.util import helpers


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.host = None
        self.username = None
        self.password = None

    def connect(self, params):
        self.logger.info("Connect: Discovering..")
        host = params.get(Input.HOST)
        username = params.get(Input.CREDENTIALS).get('username')
        password = params.get(Input.CREDENTIALS).get('password')

        r = helpers.head_url(host)
        if not r or 'link' not in r.headers:
            raise ConnectionTestException(cause='Server header error',
                                          assistance='Connect: Link header not found')

        link = r.headers.get('link')
        host = helpers.get_api_route(link)

        if not host:
            raise ConnectionTestException(cause='Server header error',
                                          assistance='Connect: API route not found in Link header')

        if not helpers.api_installed(host):
            raise ConnectionTestException(cause='API error',
                                          assistance='Connect: APIv2 not installed')

        self.host = host
        self.username = username
        self.password = password

        self.logger.info(f"Connect: API root discovered at {host}")

    def test(self):
        credentials = helpers.encode_creds(self.username, self.password)

        if not helpers.test_auth(self.logger, self.host, credentials):
            raise ConnectionTestException(cause='Test error', assistance='Test: Failed authentication')

        return {}
