import insightconnect_plugin_runtime

# Custom imports below
from icon_servicenow.util.request_helper import RequestHelper, AuthenticationType
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        api_route = "api/now/"
        incident_table = "incident"
        vulnerability_table = "sn_vul_vulnerable_item"
        third_party_vulnerability_entry_table = "sn_vul_third_party_entry"
        security_incident_table = "sn_si_incident"

        self.base_url = f"https://{params.get(Input.INSTANCE, '')}.service-now.com/"

        username = params.get(Input.CLIENT_LOGIN, {}).get("username", "")
        password = params.get(Input.CLIENT_LOGIN, {}).get("password", "")

        oauth_client_id = params.get(Input.CLIENT_ID)
        oauth_client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey")

        if all([not username, not password, not oauth_client_id, not oauth_client_secret]):
            raise PluginException(
                cause="No credentials were provided.",
                assistance="Ensure credentials and ServiceNow endpoint are correct.",
            )

        if not oauth_client_id or not oauth_client_secret and username and password:
            self.logger.info(
                "Either client ID or client secret (or both) were not provided, using basic authentication"
            )
            authentication_type = AuthenticationType.basic
        else:
            self.logger.info("Client ID and secret were provided, using OAuth for API authentication")
            authentication_type = AuthenticationType.oauth

        self.request = RequestHelper(
            username=username,
            password=password,
            client_id=oauth_client_id,
            client_secret=oauth_client_secret,
            auth_type=authentication_type,
            base_url=self.base_url,
            logger=self.logger,
        )

        self.oauth_url = f"{self.base_url}oauth_token.do"
        self.table_url = f"{self.base_url}{api_route}table/"
        self.incident_url = f"{self.table_url}{incident_table}"
        self.security_incident_url = f"{self.table_url}{security_incident_table}"
        self.vulnerability_url = f"{self.table_url}{vulnerability_table}"
        self.third_party_vulnerability_entry_url = f"{self.table_url}{third_party_vulnerability_entry_table}"
        self.attachment_url = f"{self.base_url}{api_route}attachment"
        self.change_request_url = f"{self.base_url}api/sn_chg_rest/v1/change"
        self.timeout = params.get("timeout", 30)

    def test(self):
        url = f"{self.table_url}cmdb_ci"
        query = {"sysparm_limit": 1}
        method = "get"

        response = self.request.make_request(url, method, params=query)

        if response.get("status", 0) in range(200, 299):
            return {"success": True}
        else:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNKNOWN,
                data=f'{response.get("status", "Not available")}, ' f'{response.get("text", "Not available")}',
            )
