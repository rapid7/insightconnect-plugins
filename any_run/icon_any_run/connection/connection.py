import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
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

        if not api_key and not credentials:
            raise ConnectionTestException(
                cause='No authentication credentials provided in the connection',
                assistance='Configure the connection with either an API key or username and password and try again.'
            )

        if api_key and api_key.get("secretKey") and credentials and credentials.get('username'):
            raise ConnectionTestException(
                cause='Multiple authentication methods provided.',
                assistance='Use a single credential method in the connnection, set either API key or username and password and try again.'
            )

        if api_key and api_key.get("secretKey"):
            authorization = f'API-Key {api_key.get("secretKey")}'
        else:
            authorization = 'Basic ' + base64.encodebytes(
                (credentials.get('username') +
                 ":" +
                 credentials.get('password')).encode()
            ).decode("utf-8")

        self.any_run_api = AnyRunAPI({
            'Authorization': authorization.rstrip()
        }, self.logger)

    def test(self):
        try:
            self.any_run_api.get_history(False, 0, 1)
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)

        return {}
