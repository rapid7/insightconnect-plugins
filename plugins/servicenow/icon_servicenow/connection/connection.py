import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests
from requests.auth import HTTPBasicAuth
from icon_servicenow.util.request_helper import RequestHelper
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        api_route = "api/now/"
        incident_table = "incident"
        vulnerability_table = "sn_vul_app_vulnerable_item"

        self.base_url = f"https://{params.get(Input.INSTANCE, '')}.service-now.com/"

        username = params[Input.CLIENT_LOGIN].get("username", "")
        password = params[Input.CLIENT_LOGIN].get("password", "")

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, password)
        self.request = RequestHelper(self.session, self.logger)

        self.table_url = f"{self.base_url}{api_route}table/"
        self.incident_url = f"{self.table_url}{incident_table}"
        self.vulnerability_url = f"{self.table_url}{vulnerability_table}"
        self.attachment_url = f"{self.base_url}{api_route}attachment"
        self.change_request_url = f"{self.base_url}api/sn_chg_rest/v1/change"
        self.timeout = params.get("timeout", 30)

    def test(self):
        url = f"{self.table_url}cmdb_ci"
        query = {"sysparm_limit": 1}
        method = "get"

        request = RequestHelper(self.session, self.logger)
        response = request.make_request(url, method, params=query)

        if response.get("status", 0) in range(200, 299):
            return {"success": True}
        else:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNKNOWN,
                data=f'{response.get("status", "Not available")}, ' f'{response.get("text", "Not available")}',
            )
