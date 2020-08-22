import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_ivanti_service_manager.util.api import IvantiServiceManagerAPI
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ivanti_service_manager_api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.ivanti_service_manager_api = IvantiServiceManagerAPI(
            verify_ssl=params.get(Input.SSL_VERIFY, True),
            api_key=params.get(Input.CREDENTIALS).get('secretKey'),
            url=params.get(Input.URL),
            logger=self.logger
        )

    def test(self):
        try:
            if not self.ivanti_service_manager_api.get_employees().get('value'):
                raise ConnectionTestException(
                    cause="Connection error.",
                    assistance="Problem with connecting to Ivanti Service Manager Server."
                )
        except PluginException as e:
            raise ConnectionTestException(
                cause=e.cause,
                assistance=e.assistance,
                data=e.data
            )

        return {"Success": True}
