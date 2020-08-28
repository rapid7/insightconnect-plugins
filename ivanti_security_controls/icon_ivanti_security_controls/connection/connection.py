import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_ivanti_security_controls.util.api import IvantiSecurityControlsAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ivanti_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)
        username = params.get(Input.CREDENTIALS).get('username')
        password = params.get(Input.CREDENTIALS).get('password')
        ssl_verify = params.get(Input.SSL_VERIFY)

        self.ivanti_api = IvantiSecurityControlsAPI(host, port, ssl_verify, username, password, self.logger)

    def test(self):
        try:
            # Search for single host with unexpected name; any response means success even if not found
            self.ivanti_api.get_agents(count=1, name="insightconnecttest")
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)

        return {}
