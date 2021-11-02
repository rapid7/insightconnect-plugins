import komand
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ConnectionSchema, Input
from komand.exceptions import ConnectionTestException

# Custom imports below
import requests
from typing import Optional
import json


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        self.host = params.get(Input.URL)
        self.token = params.get(Input.API_KEY).get("secretKey")
        self.org_key = params.get(Input.ORG_KEY)
        self.connector = params.get(Input.CONNECTOR)

    def get_job_id_for_detail_search(self, event_id: str) -> Optional[str]:
        response = self.make_request("POST", f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs",
                                     params={"event_ids": [event_id]}).get("response")
        if response and len(response) > 0:
            self.logger.info(response.json)
            return response
        return None

    def check_status_of_detail_search(self, get_job_id_for_detail_search: str = None):
        response = self.make_request("GET", f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/{self.job_id}",
                                     params={"job_id": get_job_id_for_detail_search})
        self.logger.info(response.json)
        for data in response.json()['items']:
            if data['contacted'] == data['completed']:
                return True
            return False

    def retrieve_results_for_detail_search(self):
        results = self.make_request("GET",
                                     f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/{self.job_id}/results",
                                     params={"job_id": self.get_job_id_for_detail_search})
        self.logger.info(results.json)
        return results

    def make_request(self, method: str, url: str, params: dict = None, data: str = None, json_data: object = None):
        try:
            response = self.call_api(method, url, params, data, json_data)

            if response.status_code == 201 or response.status_code == 204:
                return {}
            if 200 <= response.status_code < 300:
                return response.json()
        except json.decoder.JSONDecodeError as e:
            raise PluginException(
                cause="Received an unexpected response from the server.",
                assistance="(non-JSON or no response was received).",
                data=e
            )

    def call_api(self, method: str, url, params: dict = None, data: str = None, json_data: object = None):
        try:
            response = requests.request(method, url, headers=self.get_headers(), params=params, data=data,
                                        json=json_data)
            self.raise_for_status_code(response)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(
                cause="Something unexpected occurred.",
                assistance="Check the logs and if the issue persists please contact support.",
                data=response.text
            )
        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Something unexpected occurred.",
                assistance="Check the logs and if the issue persists please contact support.",
                data=e
            )

    def test(self):
        host = self.host
        token = self.token
        connector = self.connector
        devices = "/appservices/v6/orgs/" + {self.org_key} + "/devices/_search"
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
