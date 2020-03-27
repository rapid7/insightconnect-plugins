import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from requests.packages.urllib3 import exceptions
from requests.exceptions import RequestException
from komand.exceptions import ConnectionTestException
import warnings
import requests
from icon_trendmicro_apex.util.util import create_jwt_token

warnings.simplefilter('ignore', exceptions.InsecureRequestWarning)

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.header_string = ''

    def connect(self, params):
        self.api_key = params.get(Input.API_KEY).get('secretKey')
        self.application_id = params.get(Input.APPLICATION_ID).get('secretKey')
        self.url = params.get(Input.URL)

    def create_jwt_token(self, api_path, http_method, request_body):
        jwt_token = create_jwt_token(self.application_id, self.api_key, http_method, api_path, self.header_string,
                                request_body)
        self.jwt_token = jwt_token
        self.header_dict = {'Authorization': 'Bearer ' + jwt_token, 'Content-Type': "application/json"}

    def test(self):
        # list UDSO's
        json_payload = ''
        api_path = "/WebApp/api/SuspiciousObjects/UserDefinedSO/"
        request_url = self.url + api_path
        self.create_jwt_token(api_path, 'GET', json_payload)

        response = None

        try:
            response = requests.get(request_url, headers=self.header_dict, data=json_payload, verify=False)
            response.raise_for_status()
            if response.status_code != 200:
                raise ConnectionTestException( '%s (HTTP status: %s)' % (response.text, response.status_code))

            return {"success": True}
        except RequestException as rex:
            if response:
                self.logger.error(f"Received status code: {response.status_code}")
                self.logger.error(f"Response was: {response.text}")
            raise ConnectionTestException(assistance="Please verify the connection details and input data.",
                                  cause=f"Error processing the Apex request: {rex}")

        return {"success": False}

