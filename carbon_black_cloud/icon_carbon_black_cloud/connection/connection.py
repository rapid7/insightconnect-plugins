import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import urllib.parse

class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_id = params.get(Input.API_ID)
        self.api_secret = params.get(Input.API_SECRET_KEY).get("secretKey")

        self.base_url = params.get(Input.URL)
        self.base_url = self.base_url.rstrip("/")

        self.x_auth_token = f"{self.api_secret}/{self.api_id}"
        self.headers = {
            "X-Auth-Token": self.x_auth_token
        }

    def get_from_api(self, endpoint, payload):
        url = self.base_url + endpoint
        result = requests.get(url, headers=self.headers, json=payload)

        try:
            result.raise_for_status()
        except Exception as e:
            if result.status_code == 400:
                raise PluginException(cause="400 Bad Request",
                                      assistance="Verify that your request adheres to API documentation.",
                                      data=result.text)
            if result.status_code == 401:
                raise PluginException(cause="Authentication Error",
                                      assistance="Please verify that your secret_key and api_id values are correct.",
                                      data=result.text)
            if result.status_code == 403:
                raise PluginException(cause="The specified object cannot be accessed or changed.",
                                      assistance="If it has a Custom access level, check it has been assigned the correct RBAC permissions. If it is an API, SIEM or LIVE_RESPONSE type key, verify it is the right key type for the API in use.",
                                      data=result.text)
            if result.status_code == 404:
                raise PluginException(cause="The object referenced in the request cannot be found.",
                                      assistance="Verify that your request contains objects that haven’t been deleted. Verify that the org_key in the URL is correct.",
                                      data=result.text)
            if result.status_code == 409:
                raise PluginException(cause="Either the name you chose already exists, or there is an unacceptable character used.",
                                      assistance="Change any spaces in the name to underscores. Look through your list of API Keys and see if there is an existing key with the same name.",
                                      data=result.text)
            if result.status_code == 503:
                raise PluginException(cause="Cannot return object at this moment because service is unavailable.",
                                      assistance="This can happen if too many file downloads are happening at the same time. You can try later.",
                                      data=result.text)
            self.logger.error(f"Exception was:\n{e}")
            self.logger.error(f"Result text was:\n{result.text}")
            raise PluginException(PluginException.Preset.UNKNOWN)

        return result.json()


    def test(self):
        device_endpoint = "/device"
        endpoint = self.base_url + device_endpoint

        self.logger.info(endpoint)
        result = requests.get(endpoint, headers=self.headers)
        try:
            result.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause="Connection test to Carbon Black Cloud failed.\n",
                                          assistance=f"{result.text}\n",
                                          data=str(e))

        return({"success": True})



