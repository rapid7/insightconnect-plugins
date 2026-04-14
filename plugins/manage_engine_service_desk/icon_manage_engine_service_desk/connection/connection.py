import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from icon_manage_engine_service_desk.util.api import ManageEngineServiceDeskAPI
from icon_manage_engine_service_desk.util.constants import ConnectionType
from .schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        connection_type = params.get(Input.CONNECTION_TYPE)

        if connection_type == ConnectionType.ON_PREM:
            self._validate_on_prem_params(params)
            self.api_client = ManageEngineServiceDeskAPI(
                connection_type=connection_type,
                logger=self.logger,
                api_key=params.get(Input.API_KEY, {}).get("secretKey"),
                sdp_base_url=params.get(Input.SDP_BASE_URL),
                ssl_verify=params.get(Input.SSL_VERIFY, True),
            )
        else:
            self._validate_cloud_params(params)
            self.api_client = ManageEngineServiceDeskAPI(
                connection_type=connection_type,
                logger=self.logger,
                client_id=params.get(Input.CLIENT_ID),
                client_secret=params.get(Input.CLIENT_SECRET, {}).get("secretKey"),
                refresh_token=params.get(Input.REFRESH_TOKEN, {}).get("secretKey"),
                portal_name=params.get(Input.PORTAL_NAME),
                data_center=params.get(Input.DATA_CENTER),
            )

    def test(self):
        try:
            self.api_client.get_requests_list()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection test failed.",
                assistance="Please verify your connection settings and try again.",
            )
        return {"status": "Success"}

    @staticmethod
    def _validate_on_prem_params(params: dict) -> None:
        missing = []
        if not params.get(Input.SDP_BASE_URL):
            missing.append("Service Desk Plus Base URL")
        if not params.get(Input.API_KEY, {}).get("secretKey"):
            missing.append("API Key")
        if missing:
            raise ConnectionTestException(
                cause=f"On-Prem connection is missing required fields: {', '.join(missing)}.",
                assistance="Please provide the Service Desk Plus Base URL and API Key for On-Prem connections.",
            )

    @staticmethod
    def _validate_cloud_params(params: dict) -> None:
        missing = []
        if not params.get(Input.CLIENT_ID):
            missing.append("Client ID")
        if not params.get(Input.CLIENT_SECRET, {}).get("secretKey"):
            missing.append("Client Secret")
        if not params.get(Input.REFRESH_TOKEN, {}).get("secretKey"):
            missing.append("Refresh Token")
        if not params.get(Input.PORTAL_NAME):
            missing.append("Portal Name")
        if not params.get(Input.DATA_CENTER):
            missing.append("Data Center")
        if missing:
            raise ConnectionTestException(
                cause=f"Cloud connection is missing required fields: {', '.join(missing)}.",
                assistance="Please provide the Client ID, Client Secret, Refresh Token, Portal Name, and Data Center for Cloud connections.",
            )
