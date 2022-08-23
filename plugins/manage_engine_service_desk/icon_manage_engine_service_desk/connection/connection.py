import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from icon_manage_engine_service_desk.util.api import ManageEngineServiceDeskAPI
from .schema import ConnectionSchema, Input


# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        self.api_client = ManageEngineServiceDeskAPI(
            api_key=params.get(Input.API_KEY).get("secretKey"),
            sdp_base_url=params.get(Input.SDP_BASE_URL),
            ssl_verify=params.get(Input.SSL_VERIFY),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_requests_list()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please make sure that your API key and Sdp Base URL are correct",
            )
        return {"status": "Success"}
