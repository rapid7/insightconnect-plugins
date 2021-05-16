from insightconnect_plugin_runtime.helper import clean
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from logging import Logger
from urllib.parse import urljoin
from datetime import datetime


class AbnormalSecurityAPI:
    def __init__(self, url: str, api_key: str, logger: Logger):
        self.api_version = "v1"
        # self.base_url = f"https://{url}/{self.api_version}"
        self.base_url = f"https://{url}"
        # self.headers = {"authorization": f"Bearer {api_key}"}
        self.headers = {"authorization": f"Bearer {api_key}", "x-mock-match-request-headers": "authorization"}
        self.logger = logger

    def test_api(self):
        return self.send_request("GET", "/threats")

    def get_threats(self, from_date: str = None, to_date: str = None):
        return self.send_request(
            "GET",
            "/threats",
            params=self.generate_filter_params(from_date, to_date)
        ).get("threats")

    def get_threat_details(self, threat_guid):
        return self.send_request("GET", f"/threats/{threat_guid}")

    def get_cases(self, from_date: str = None, to_date: str = None):
        return self.send_request(
            "GET",
            "/cases",
            params=self.generate_filter_params(from_date, to_date)
            ).get("cases")

    def get_case_details(self, case_guid):
        return self.send_request("GET", f"/cases/{case_guid}")

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        try:
            response = requests.request(
                method.upper(),
                urljoin(self.base_url, path),
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                try:
                    error_message = response.json().get('message')
                except:
                    raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
                raise PluginException(cause="Abnormal Security API returned an error message.",
                                      assistance=f"The error message was: {error_message}.")
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def generate_filter_params(self, from_date: str = None, to_date: str = None) -> dict:
        params = {}
        if from_date or to_date:
            params = {"filter": "receivedTime"}
            if from_date and self.validate_iso8601(from_date):
                params["filter"] = params["filter"] + f" gte {from_date}"
            if to_date and self.validate_iso8601(to_date):
                params["filter"] = params["filter"] + f" lte {to_date}"
        return params

    @staticmethod
    def validate_iso8601(dt_string):
        try:
            datetime.fromisoformat(dt_string)
        except ValueError:
            try:
                datetime.fromisoformat(dt_string.replace("Z", "+00:00"))
            except ValueError:
                raise PluginException(
                    cause=f"Date: {dt_string} is not a valid ISO8601 date.",
                    assistance="Please update the date to match ISO8601 format (YYYY-MM-DDTHH:MM:SSZ).",
                )
        return True
