# Custom imports below
import base64

from komand_rest.util.util import Common

import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.base_url = None
        self.default_headers = None
        self.ssl_verify = None

    def connect(self, params):
        self.logger.info("Connect: Configuring REST details")
        base_url = params.get(Input.BASE_URL)
        default_headers = params.get(Input.DEFAULT_HEADERS, {})
        username = params.get(Input.BASIC_AUTH_CREDENTIALS, {}).get("username")
        password = params.get(Input.BASIC_AUTH_CREDENTIALS, {}).get('password')

        if base_url is None or len(base_url) <= 0:
            raise ConnectionTestException(
                cause='Input error',
                assistance="Connect: Property 'base_url' was None or 0 length. Make sure it is marked required.")

        if username and password:
            credentials = f'{username}:{password}'.encode()
            base64_credentials = base64.encodebytes(credentials).decode().replace('\n', '')
            auth = f'Basic {base64_credentials}'
            default_headers = Common.merge_dicts(default_headers, {'Authorization': auth})

        self.base_url = base_url
        self.default_headers = default_headers
        self.ssl_verify = params.get(Input.SSL_VERIFY)
        self.logger.info("Connect: Connecting..")
