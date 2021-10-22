import komand
from komand_carbon_black_defense.connection.schema import ConnectionSchema, Input
import insightconnect_plugin_runtime
import json
import requests
import validators
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from logging import Logger
from typing import Optional


class CarbonBlackAPI(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client_id = None
        self.client_secret = None

    def connect(self, params={}):
       self.logger.info("Connect: Connecting...")
       self.client_secret = params.get(Input.API_KEY).get("secretKey")
       self.connector = params.get(Input.CONNECTOR)
       self.org_key = params.get(Input.ORG_KEY)
       self.base_url = params.get(Input.URL, "https://defense.conferdeploy.net")
       self.base_url_clean = self.clean_base_url(self.base_url)
       self.logger.info("Creds Provided:")
       self.logger.info("client_id: " + self.connector)
       self.logger.info("client_secret: *************" + self.client_secret[-4:])
       self.logger.info(f"Base URL: {self.base_url}")

    def get_job_id(self, event_ids: str) -> Optional[str]:
            response = self.call_api(
                "POST",
                f"{self.base_url}/api/investigate/v2/orgs/{self.org_key}/enriched_events/search_jobs",
                params={
                    "event_ids": [event_ids]
                },
                data=None,
                json_data=None
            )
            if 200 <= response.status_code < 300:
                return response.json()

    def is_status_of_events_completed(self):
            response = self.call_api(
                "GET",
                f"{self.base_url}/api/investigate/v1/orgs/{self.org_key}/processes/search_jobs/{self.job_id}",
                params={},
                data=None,
                json_data=None
            )
            if response.completed == response.contacted:
                return True
            else:
                return False

    def get_enriched_event(self):
      response = self.call_api(
          "GET",
          f"{self.base_url}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/{self.job_id}",
          params={},
          data=None,
          json_data=None
      )
      if 200 <= response.status_code < 300:
          return response.json()

    def get_x_auth_token(self, client_secret: str, client_id: str) -> str:
        payload = f"client_secret={client_secret}&client_id={client_id}"
        x_auth_token = client_secret/client_id
        return x_auth_token


    def make_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        response = self.call_api(method.upper(), url, params, data, json_data,
        )

        try:
            if 200 <= response.status_code < 300:
                return insightconnect_plugin_runtime.helper.clean(json.loads(response.content))
            elif response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
            elif response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            elif response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Something unexpected occurred.",
                assistance="Check the logs and if the issue persists please contact support.",
                data=e
            )
    def get_headers(self):
        auth_token = self.get_x_auth_token(self.client_secret, self.client_id)
        headers = {
            "Content-type": "application/json",
            "Accepts": "application/json",
            "Authorization": auth_token

        }
        return headers
    def call_api(self, method: str, url: str, params: dict = None, data: str = None, json_data: object = None):
        try:
            response = requests.request(method, url, headers=self.get_headers(), params=params, data=data, json=json_data)
            if 200 <= response.status_code < 300:
                return response
        except requests.exceptions.HTTPError as e:
            raise PluginException(
                cause="Something unexpected occurred.",
                assistance="Check the logs and if the issue persists please contact support.",
                data=e
            )
