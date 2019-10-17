import komand
from .schema import ConnectionSchema

# Custom imports below
import requests
from komand.exceptions import ConnectionTestException


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def get_token_from_client_credentials(self, endpoint, client_id, client_secret):
        try:
            payload = {
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "resource": "https://management.azure.com/",
            }
            response = requests.post(endpoint, data=payload).json()
            return response["access_token"]
        except Exception as e:
            self.logger.error("Cannot request get access token : %s", e)
            return ""

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get("host", "https://management.azure.com")
        api_version = params.get("api_version", "2016-04-30-preview")
        client_id = params.get("client_id", "")
        client_secret = params.get("client_secret").get("privateKey")
        tenant_id = params.get("tenant_id", "")

        endpoint = "https://login.microsoftonline.com/%s/oauth2/token/" % tenant_id

        access_token = self.get_token_from_client_credentials(
            endpoint=endpoint, client_id=client_id, client_secret=client_secret
        )

        if access_token == "":
            self.logger.info("Connect: Unauthenticated API will be used")

        self.server = server
        self.token = access_token
        self.api_version = api_version

    def test(self):
        http_method = "GET"
        server = self.server
        token = self.token
        version = "2017-03-01"

        # URL test authentication
        url = server + "/subscriptions?api-version=%s" % version

        # Call request test authentication
        response = requests.request(
            http_method,
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer %s" % token,
            },
        )

        if response.status_code == 401:
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNAUTHORIZED
            )
        if response.status_code != 200:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN)

        return {"status_code": response.status_code}
