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

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        api_key = params.get(Input.API_KEY, {}).get("secretKey", "")
        username = params.get(Input.CREDENTIALS, {}).get("username", "")
        password = params.get(Input.CREDENTIALS, {}).get("password", "")

        # In case no authentication method is provided, raise an exception
        if not api_key and not username and not password:
            raise ConnectionTestException(
                cause="No authentication credentials provided in the connection.",
                assistance="Configure the connection with either an API key or username and password and try again.",
            )

        # In case multiple authentication methods are provided, raise an exception
        if api_key and username and password:
            raise ConnectionTestException(
                cause="Multiple authentication methods provided.",
                assistance="Use a single credential method in the connnection, set either API key or username and password and try again.",
            )

        # Prepare the authorization header based on the provided authentication method
        if api_key:
            authorization = f"API-Key {api_key}"
        else:
            authorization = f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode('utf-8')}"

        self.any_run_api = AnyRunAPI({"Authorization": authorization.rstrip()}, self.logger)

    def test(self):
        try:
            self.any_run_api.get_history(False, 0, 1)
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error)
