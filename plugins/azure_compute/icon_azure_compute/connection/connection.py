import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
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
            response = requests.post(endpoint, data=payload).json()  # noqa
            return response["access_token"]
        except Exception as error:
            self.logger.error(f"Cannot request get access token : {error}")
            return ""

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get(Input.HOST, "https://management.azure.com")
        api_version = params.get(Input.API_VERSION, "2016-04-30-preview")
        client_id = params.get(Input.CLIENT_ID, "")
        client_secret = params.get(Input.CLIENT_SECRET, {}).get("secretKey", "")
        tenant_id = params.get(Input.TENANT_ID, "")

        endpoint = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token/"

        access_token = self.get_token_from_client_credentials(
            endpoint=endpoint, client_id=client_id, client_secret=client_secret
        )

        if access_token == "":  # noqa: B105
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
        url = server + f"/subscriptions?api-version={version}"

        # Call request test authentication
        response = requests.request(
            http_method,
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )

        if response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        if response.status_code != 200:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN)

        return {"status_code": response.status_code}
