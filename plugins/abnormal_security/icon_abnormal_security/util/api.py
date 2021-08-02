from insightconnect_plugin_runtime.helper import clean
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from logging import Logger
from urllib.parse import urlsplit
import dateparser


class AbnormalSecurityAPI:
    def __init__(self, url: str, api_key: str, logger: Logger):
        self.api_version = "v1"
        self.base_url = f"{self.split_url(url)}/{self.api_version}"
        self.headers = {"authorization": f"Bearer {api_key}"}
        self.logger = logger

    def test_api(self):
        return self.send_request("GET", "/threats")

    def get_threats(self, from_date: str = None, to_date: str = None):
        return self.send_request("GET", "/threats", params=self.generate_filter_params(from_date, to_date)).get(
            "threats"
        )

    def get_threat_details(self, threat_guid):
        return self.send_request("GET", f"/threats/{threat_guid}")

    def get_cases(self, from_date: str = None, to_date: str = None) -> dict:
        return self.send_request("GET", "/cases", params=self.generate_filter_params(from_date, to_date)).get("cases")

    def get_case_details(self, case_guid: str) -> dict:
        return self.send_request("GET", f"/cases/{case_guid}")

    def manage_threat(self, threat_id: str, action: str) -> dict:
        return self.send_request("POST", f"/threats/{threat_id}", payload={"action": action})

    def manage_case(self, case_id: str, action: str) -> dict:
        results = self.send_request("POST", f"/cases/{case_id}", payload={"action": action})
        if isinstance(results.get("statusUrl"), dict):
            if results.get("statusUrl"):
                results["statusUrl"] = str(results.get("statusUrl"))
            else:
                results["statusUrl"] = ""
        return results

    # pylint: disable=inconsistent-return-statements
    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        try:
            response = requests.request(
                method.upper(),
                f"{self.base_url}{path}",
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                try:
                    error_message = response.json()["message"]
                except Exception:
                    raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
                raise PluginException(
                    cause="Abnormal Security API returned an error message.",
                    assistance=f"The error message was: {error_message}.",
                )
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
                return clean(response.json())

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def generate_filter_params(self, from_date: str = None, to_date: str = None) -> dict:
        params = {}
        if from_date or to_date:
            params = {"filter": "receivedTime"}
            if from_date:
                params["filter"] = params["filter"] + f" gte {self.parse_date(from_date)}"
            if to_date:
                params["filter"] = params["filter"] + f" lte {self.parse_date(to_date)}"
        return params

    @staticmethod
    def parse_date(date: str) -> str:
        try:
            parsed_date = dateparser.parse(date)
            if not parsed_date.tzinfo:
                return parsed_date.isoformat() + "Z"
            return parsed_date.isoformat()
        except Exception:
            raise PluginException(
                cause=f"Date '{date}' is not a valid date.",
                assistance="Please verify the date and try again.",
            )

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
        return f"{scheme}://{netloc}"
