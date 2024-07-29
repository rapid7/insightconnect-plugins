import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
import requests
from json import JSONDecodeError
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import time
from icon_carbon_black_cloud.util import agent_typer
from icon_carbon_black_cloud.util.constants import DEFAULT_TIMEOUT, ERROR_HANDLING
from icon_carbon_black_cloud.util.exceptions import RateLimitException, HTTPErrorException

from typing import Dict, Any
import re


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.api_id = params.get(Input.API_ID, "").strip()
        self.api_secret = params.get(Input.API_SECRET_KEY, {}).get("secretKey", "").strip()
        self.org_key = params.get(Input.ORG_KEY, "").strip()
        self.base_url = f"https://{params.get(Input.URL, '')}"
        self.x_auth_token = f"{self.api_secret}/{self.api_id}"
        self.headers = {"X-Auth-Token": self.x_auth_token, "Content-Type": "application/json"}

    def get_agent(self, agent):
        self.logger.info(f"Looking for: {agent}")
        agent_type = agent_typer.get_agent_type(agent)
        endpoint = f"appservices/v6/orgs/{self.org_key}/devices/_search"
        url = f"{self.base_url}/{endpoint}"
        payload = {"query": re.escape(agent)}
        results = self.request_api(url, payload).get("results")

        device = {}
        if agent_type == agent_typer.DEVICE_ID:
            device = next((element for element in results if str(element.get("id", "")) == agent), {})
        if agent_type == agent_typer.IP_ADDRESS:
            device = next(
                (
                    element
                    for element in results
                    if element.get("last_internal_ip_address") == agent or element.get("last_external_ip_address")
                ),
                {},
            )
        if agent_type == agent_typer.HOSTNAME:
            device = next(
                (element for element in results if str(element.get("name", "")).lower() == str(agent).lower()), {}
            )
        if agent_type == agent_typer.MAC_ADDRESS:
            device = next((element for element in results if element.get("mac_address", "") == agent), {})

        if not device:
            self.logger.error(f"Could not find any device that matched {agent}")

        return device

    def request_api(
        self,
        url: str,
        payload: Dict[str, str] = None,
        request_method: str = "POST",
        retry: bool = True,
        debug: bool = False,
    ) -> Dict[str, str]:
        payload = payload if payload else {}
        try:
            if debug:
                # start timer so we can track the duration of the request
                request_start_epoch = time.time()

            response = requests.request(
                method=request_method, url=url, headers=self.headers, json=payload, timeout=DEFAULT_TIMEOUT
            )

            if debug:
                request_end_epoch = time.time()
                request_time = request_end_epoch - request_start_epoch
                self.logger.info(f"Time elapsed for request to URL [{url}]: {round(request_time, 4)} seconds.")

            return self._handle_response(response, url, payload, retry)
        except requests.Timeout as timeout_error:
            self.logger.error(f"Hitting connection timeout on request to Carbon Black. error={timeout_error}")
            raise PluginException(preset=PluginException.Preset.TIMEOUT, data=timeout_error)

    def _handle_response(
        self, response: requests.Response, url: str, payload: Dict[str, str], retry: bool = True
    ) -> Dict[str, Any]:
        error_cause = f"Unexpected status code from API - {response.status_code}"
        error_data, error_assistance = response.text, "Unexpected response. Please contact support."
        if response.status_code == 200:
            try:
                return response.json()
            except JSONDecodeError as json_error:
                error_data = f"Invalid JSON response: {response.content}"
                error_cause = json_error
        elif response.status_code == 204:
            return {}
        elif response.status_code == 429:
            # We need to back off for 5 minutes until this period has passed but this is only implemented in task code
            self.logger.error(
                f"Received 429 status code. Retry-After header={response.headers.get('Retry-After', 'Not found')}"
            )
            error_cause = "Too many requests within a 5 minute period."
            error_assistance = (
                "Too many requests made and now rate limited. " + "Please wait 5 minutes before triggering plugin again"
            )  # this is a result of black and linter fighting against each other

            raise RateLimitException(cause=error_cause, assistance=error_assistance, data=error_data)
        elif response.status_code == 503:  # This is usually a server error, try again
            time.sleep(5)
            if retry:
                return self.request_api(url, payload, retry=False)
            self.logger.error(f"Retry on 503 failed. Response: {response.text}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)
        else:
            for status_code, exception_values in ERROR_HANDLING.items():
                if response.status_code == status_code:
                    error_cause = exception_values.get("cause")
                    error_assistance = exception_values.get("assistance")
                    break

        raise HTTPErrorException(
            cause=error_cause, assistance=error_assistance, data=error_data, status_code=response.status_code
        )

    def test(self):
        device_endpoint = "/device"
        endpoint = self.base_url + device_endpoint
        try:
            result = requests.get(endpoint, headers=self.headers, timeout=DEFAULT_TIMEOUT)
            result.raise_for_status()
        except HTTPErrorException as error:
            raise ConnectionTestException(
                cause="Connection test to Carbon Black Cloud failed.\n",
                assistance=f"{result.text}\n",
                data=str(error),
            )
        except Exception as error:
            raise ConnectionTestException(
                cause="Connection test to Carbon Black Cloud failed.\n",
                assistance="Request failed. Please see exception data for details.",
                data=str(error),
            )
        return {"success": True}
