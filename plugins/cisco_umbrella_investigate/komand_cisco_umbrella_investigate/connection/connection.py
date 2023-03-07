import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
import requests
from komand_cisco_umbrella_investigate.investigate import investigate
import re


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.test_url = "https://investigate.api.umbrella.com/domains/score/example.com"
        # self.test_url = 'https://investigate.api.umbrella.com/domains/categorization'

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")
        self.key = params.get("api_key").get("secretKey")
        self.investigate = investigate.Investigate(self.key, self.logger)

    def test(self):
        # Check key format
        pattern = re.compile("^[A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12}$")
        if not pattern.match(self.key):
            raise ConnectionTestException(
                cause="Invalid API key.",
                assistance="The API key is a UUID-v4 key. For more information, see: https://developer.cisco.com/docs/cloud-security/#!umbrella-legacy-authentication/prerequisites",
            )

        # Authenticate to API
        # Modified from https://github.com/opendns/investigate-examples/blob/master/scripts.py
        headers = {"Authorization": "Bearer " + self.key}
        response = requests.get(self.test_url, headers=headers)

        # https://docs.umbrella.com/investigate-api/docs/error-handling-1
        if 200 <= response.status_code < 300:
            return {"success": True}
        elif response.status_code == 403:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        elif response.status_code == 404:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.NOT_FOUND)
        elif response.status_code == 429:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.RATE_LIMIT)
        elif response.status_code == 500:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR)
        elif response.status_code == 503:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        else:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNKNOWN, data=response.text)
