import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import base64
from icon_any_run.util.api import AnyRunAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.authentication_header = None
        self.any_run_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        api_key = params.get(Input.API_KEY)
        credentials = params.get(Input.CREDENTIALS)

        self.logger.info(f'api_key: {api_key.get("secretKey")}')

        if not api_key and not credentials:
            raise ConnectionTestException(
                cause='Invalid API key provided.',
                assistance='One credential method is mandatory'
            )

        if api_key and credentials:
            raise ConnectionTestException(
                cause='Invalid API key provided.',
                assistance='Only one credential method should be used'
            )

        if api_key:
            authorization = f'API-Key {api_key.get("secretKey")}'
        else:
            authorization = 'Basic ' + base64.encodebytes(
                credentials.get('username') +
                ":" +
                credentials.get('password')
            )

        self.any_run_api = AnyRunAPI({
            'Authorization': authorization
        }, self.logger)

    def test(self):
        pass
