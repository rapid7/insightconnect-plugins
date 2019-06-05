import komand
from .schema import ConnectionSchema
from komand_rest.util.util import Common
# Custom imports below
import base64


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Configuring REST details")
        base_url = params.get("base_url")
        default_headers = params.get("default_headers", {})
        username = params.get('basic_auth_credentials', {}).get("username")
        password = params.get("basic_auth_credentials", {}).get('password')

        assert base_url is not None and len(base_url) > 0, \
            "Connect: Property 'base_url' was None or 0 length. Make sure it is marked required."

        if username and password:
            credentials = '{}:{}'.format(username, password).encode()
            auth = 'Basic {}'.format(base64.encodebytes(credentials).decode().replace('\n', ''))
            default_headers = Common.merge_dicts(default_headers, {'Authorization': auth})

        self.base_url = base_url
        self.default_headers = default_headers
        self.ssl_verify = params.get("ssl_verify")
        self.logger.info("Connect: Connecting..")
