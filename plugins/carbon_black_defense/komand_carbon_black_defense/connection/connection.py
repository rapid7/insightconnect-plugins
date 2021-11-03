import komand
from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

# Custom imports below
import requests
import time
from typing import Optional

class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        self.host = params.get(Input.URL)
        self.api_secret = params.get(Input.API_KEY).get("secretKey")
        self.connector = params.get(Input.CONNECTOR)
        self.org_key = params.get(Input.ORG_KEY)

        self.x_auth_token = f"{self.api_secret}/{self.connector}"
        self.headers = {"X-Auth-Token": self.x_auth_token}



    def post_to_api(self, url, payload, retry=True):
        result = requests.post(url, headers=self.headers, json=payload)
        try:
            result.raise_for_status()
        except Exception as e:
            if result.status_code == 400:
                raise PluginException(
                    cause="400 Bad Request",
                    assistance="Verify that your request adheres to API documentation.",
                    data=result.text,
                )
            if result.status_code == 401:
                raise PluginException(
                    cause="Authentication Error",
                    assistance="Please verify that your Secret Key and API ID values in the plugin connection are correct.",
                    data=result.text,
                )
            if result.status_code == 403:
                raise PluginException(
                    cause="The specified object cannot be accessed or changed.",
                    assistance="If it has a Custom access level, check it has been assigned the correct RBAC permissions. If it is an API, SIEM or LIVE_RESPONSE type key, verify it is the right key type for the API in use.",
                    data=result.text,
                )
            if result.status_code == 404:
                raise PluginException(
                    cause="The object referenced in the request cannot be found.",
                    assistance="Verify that your request contains objects that haven’t been deleted. Verify that the organization key in the URL is correct.",
                    data=result.text,
                )
            if result.status_code == 409:
                raise PluginException(
                    cause="Either the name you chose already exists, or there is an unacceptable character used.",
                    assistance="Change any spaces in the name to underscores. Look through your list of API Keys and see if there is an existing key with the same name.",
                    data=result.text,
                )
            if result.status_code == 503:  # This is usually an API limit error or server error, try again
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

    def get_job_id_for_enriched_event(self, process_name: str) -> Optional[str]:
        endpoint = f"/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs"
        url = f"{self.base_url}/{endpoint}"
        payload = {"criteria": {
            "process_name":
                [process_name]}}

        results = self.post_to_api(url, payload).get("results")
        if results and len(results) > 0:
            return results
        return None

    def get_enriched_event_status(self, get_job_id_for_enriched_event: str = None):
        endpoint = f"/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs/"
        url = f"{self.base_url}/{endpoint}"

        results = self.call_api(url, params={"cb_job_id": get_job_id_for_enriched_event})
        for key in results.items():
            if results["contacted"] == results["completed"]:
                return True
            return False

    def retrieve_results_for_enriched_event(self, get_job_id_for_enriched_event: str = None):
        endpoint = f"/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs/"
        partial_url = f"{self.base_url}/{endpoint}"
        params = {"cb_job_id": get_job_id_for_enriched_event}
        url = partial_url + params + "/results"
        return self.call_api(url, params)

    def call_api(self, url: str, params: dict = None, data: str = None):
        try:
            requests.get(url, headers=self.headers, params=params, data=data)
        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Something unexpected occurred.",
                assistance="Check the logs and if the issue persists please contact support.",
                data=e)

    def test(self):
        host = self.host
        token = self.token
        connector = self.connector
        devices = "/integrationServices/v3/device"
        headers = {"X-Auth-Token": f"{token}/{connector}"}
        url = host + devices

        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            return {"success": True}
        if result.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        raise ConnectionTestException(
            f"An unknown error occurred. Response code was: {result.status_code}"
            f" If the problem persists please contact support for help. Response was: {result.text}"
        )
