import komand
from komand.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input
# Custom imports below
import requests
import time


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.O365_AUTH_ENDPOINT = "https://login.microsoftonline.com/{}/oauth2/token"
        self.SCOPE = "https://graph.microsoft.com"

        self.tenant = ""
        self.app_secret = ""

        # Auth tokens expire after 1 hour. Only make that call if we need to
        self.time_ago = 0  # Jan 1, 1970
        self.time_now = time.time()  # More than 1 hour since 1978

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        self.tenant = params.get(Input.TENANT_ID)
        self.app_id = params.get(Input.APP_ID)
        self.app_secret = params.get(Input.APP_SECRET).get("secretKey")
        self.auth_token = self.get_auth_token()

    def get_auth_token(self):
        tenant_id = self.tenant
        client_id = self.app_id
        client_secret = self.app_secret

        self.time_now = time.time()
        if (self.time_now - self.time_ago) < 3500:  # 1 hour in seconds
            return self.auth_token

        self.logger.info("Updating auth token...")

        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'resource': self.SCOPE,
            'client_secret': client_secret,
        }

        formatted_endpoint = self.O365_AUTH_ENDPOINT.format(tenant_id)
        self.logger.info("Getting token from: " + formatted_endpoint)

        request = requests.post(formatted_endpoint, data=data)
        self.logger.info("Authentication request status: " + str(request.status_code))

        if request.status_code is not 200:
            self.logger.error(request.text)
            raise PluginException(cause="Unable to authorize against Microsoft graph API.",
                                  assistance="The application may not be authorized to connect "
                                             "to the Microsoft Graph API. Please contact your "
                                             "Azure administrator.",
                                  data=request.text)

        token = request.json().get('access_token')

        self.time_ago = time.time()
        self.auth_token = token

        self.logger.info(f"Authentication Token: ****************{self.auth_token[-5:]}")

        return token

    @staticmethod
    def get_headers(auth_token):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + auth_token
        }
        return headers

    def test(self):
        if not self.auth_token:
            raise ConnectionTestException(cause="Unable to authorize against Microsoft graph API.",
                                          assistance="The application may not be authorized to connect "
                                                     "to the Microsoft Graph API. Please contact your "
                                                     "Azure administrator.")
