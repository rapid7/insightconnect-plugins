import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from requests.packages.urllib3 import exceptions
from requests.exceptions import RequestException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import warnings
import requests
from icon_trendmicro_apex.util.util import create_jwt_token
from icon_trendmicro_apex.util.api import Api

warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.header_string = ""
        self.api_key = None
        self.application_id = None
        self.url = None
        self.jwt_token = None
        self.header_dict = None
        self.api = None

    def connect(self, params):
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.application_id = params.get(Input.APPLICATION_ID).get("secretKey")
        self.url = params.get(Input.URL).rstrip("/")
        self.api = Api(self)

    def create_jwt_token(self, api_path, http_method, request_body):
        jwt_token = create_jwt_token(
            self.application_id,
            self.api_key,
            http_method,
            api_path,
            self.header_string,
            request_body,
        )
        self.jwt_token = jwt_token
        self.header_dict = {
            "Authorization": "Bearer " + jwt_token,
            "Content-Type": "application/json",
        }

    def test(self):
        # list UDSO's
        json_payload = ""
        api_path = "/WebApp/api/SuspiciousObjects/UserDefinedSO/"
        self.create_jwt_token(api_path, "GET", json_payload)

        response = self.connection.api.execute("get", api_path, json_payload)

        if response.status_code != 200:
            raise ConnectionTestException(f"{response.text} (HTTP status: {response.status_code})")

        return {"success": True}
