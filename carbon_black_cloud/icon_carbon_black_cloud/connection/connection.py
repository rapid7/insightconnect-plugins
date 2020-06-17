import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import time
import icon_carbon_black_cloud.util.agent_typer as agent_typer
import urllib.parse

class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_id = params.get(Input.API_ID)
        self.api_secret = params.get(Input.API_SECRET_KEY).get("secretKey")

        base_url = params.get(Input.URL)
        self.base_url = urllib.parse.urlparse(base_url).hostname
        self.base_url = f"https://{self.base_url}"

        self.org_key = params.get(Input.ORG_KEY)

        self.x_auth_token = f"{self.api_secret}/{self.api_id}"
        self.headers = {
            "X-Auth-Token": self.x_auth_token
        }

    def get_agent(self, agent):
        self.logger.info(f"Looking for: {agent}")
        agent_type = agent_typer.get_agent_type(agent)
        endpoint = f"appservices/v6/orgs/{self.org_key}/devices/_search"
        url = f"{self.base_url}/{endpoint}"
        payload = {
            "query": agent
        }

        self.logger.info(f"Searching at {url}")
        results = self.post_to_api(url, payload).get("results")

        device = None
        if agent_type == agent_typer.DEVICE_ID:
            device = next((x for x in results if str(x.get("id","")) == agent), None)
        if agent_type == agent_typer.IP_ADDRESS:
            device = next((x for x in results if x.get("last_internal_ip_address") == agent or
                                                 x.get("last_external_ip_address")), None)
        if agent_type == agent_typer.HOSTNAME:
            device = next((x for x in results if x.get("name", "") == agent), None)
        if agent_typer == agent_typer.MAC_ADDRESS:
            device = next((x for x in results if x.get("mac_address", "") == agent), None)

        if not device:
            self.logger.error(f"Could not find any device that matched {agent}")

        return device

    def post_to_api(self, url, payload, retry=True):
        result = requests.post(url, headers=self.headers, json=payload)

        try:
            result.raise_for_status()
        except Exception as e:
            if result.status_code == 400:
                raise PluginException(cause="400 Bad Request",
                                      assistance="Verify that your request adheres to API documentation.",
                                      data=result.text)
            if result.status_code == 401:
                raise PluginException(cause="Authentication Error",
                                      assistance="Please verify that your Secret Key and API ID values in the plugin connection are correct.",
                                      data=result.text)
            if result.status_code == 403:
                raise PluginException(cause="The specified object cannot be accessed or changed.",
                                      assistance="If it has a Custom access level, check it has been assigned the correct RBAC permissions. If it is an API, SIEM or LIVE_RESPONSE type key, verify it is the right key type for the API in use.",
                                      data=result.text)
            if result.status_code == 404:
                raise PluginException(cause="The object referenced in the request cannot be found.",
                                      assistance="Verify that your request contains objects that haven’t been deleted. Verify that the organization key in the URL is correct.",
                                      data=result.text)
            if result.status_code == 409:
                raise PluginException(cause="Either the name you chose already exists, or there is an unacceptable character used.",
                                      assistance="Change any spaces in the name to underscores. Look through your list of API Keys and see if there is an existing key with the same name.",
                                      data=result.text)
            if result.status_code == 503: # This is usually an API limit error or server error, try again
                time.sleep(5)
                if retry:
                    return self.post_to_api(url, payload, False)

                self.logger.error("Retry on 503 failed.")
                self.logger.error(str(e))
                self.logger.error(result.text)
                raise PluginException(PluginException.Preset.UNKNOWN)

        if result.status_code != 204:
            return result.json()
        else:
            return {}


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

