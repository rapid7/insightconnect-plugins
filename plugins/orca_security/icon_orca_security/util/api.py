from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from urllib.parse import urlsplit
import requests
import json
import base64

from icon_orca_security.util.endpoints import (
    ALERT_ENDPOINT,
    ALERTS_ENDPOINT,
    ALERTS_SCHEMA_ENDPOINT,
    ASSET_ENDPOINT,
    ASSETS_ENDPOINT,
    DOWNLOAD_MALICIOUS_FILE_ENDPOINT,
    ORGANIZATION_USERS_ENDPOINT,
    QUERY_ALERTS_ENDPOINT,
    RBAC_ROLE_ENDPOINT,
    RBAC_ROLES_ENDPOINT,
    UPDATE_ALERT_SEVERITY_ENDPOINT,
    UPDATE_ALERT_STATUS_ENDPOINT,
    USER_SESSION_ENDPOINT,
    VERIFY_ALERT_ENDPOINT,
)


class OrcaSecurityAPI:
    def __init__(self, url: str, api_token: str, logger):
        self.base_url = f"{self.split_url(url)}/api"
        self._api_token = api_token
        self.logger = logger

    def get_headers(self) -> dict:
        return {"accept": "application/json", "Authorization": f"Token {self._api_token}"}

    def get_asset_by_id(self, asset_id: str) -> dict:
        return self.make_request(path=ASSET_ENDPOINT.format(asset_id=asset_id), headers=self.get_headers())

    def get_assets(self, parameters: dict) -> dict:
        return self.make_request(path=ASSETS_ENDPOINT, params=parameters, headers=self.get_headers())

    def get_alert_by_id(self, alert_id: str) -> dict:
        return self.make_request(path=ALERT_ENDPOINT.format(alert_id=alert_id), headers=self.get_headers())

    def get_alerts(self, parameters: dict) -> dict:
        return self.make_request(path=ALERTS_ENDPOINT, params=parameters, headers=self.get_headers())

    def get_alerts_scheme(self) -> dict:
        return self.make_request(path=ALERTS_SCHEMA_ENDPOINT, headers=self.get_headers())

    def query_alerts(self, parameters: dict) -> dict:
        return self.make_request(path=QUERY_ALERTS_ENDPOINT, params=parameters, headers=self.get_headers())

    def update_alert_status(self, alert_id: str, status: str) -> dict:
        return self.make_request(
            path=UPDATE_ALERT_STATUS_ENDPOINT.format(alert_id=alert_id, status=status),
            method="PUT",
            headers=self.get_headers(),
        )

    def update_alert_severity(self, alert_id: str, data: dict) -> dict:
        return self.make_request(
            path=UPDATE_ALERT_SEVERITY_ENDPOINT.format(alert_id=alert_id),
            method="PUT",
            data=data,
            headers=self.get_headers(),
        )

    def download_malicious_file(self, alert_id: str) -> str:
        link = self.make_request(
            path=DOWNLOAD_MALICIOUS_FILE_ENDPOINT.format(alert_id=alert_id), headers=self.get_headers()
        ).get("link")
        content = requests.get(link).content
        return str(base64.b64encode(content), "utf-8")

    def verify_alert(self, alert_id: str) -> dict:
        return self.make_request(
            path=VERIFY_ALERT_ENDPOINT.format(alert_id=alert_id), method="PUT", headers=self.get_headers()
        )

    def get_users(self):
        return self.make_request(path=ORGANIZATION_USERS_ENDPOINT, headers=self.get_headers())

    def add_user(self, data: dict) -> dict:
        return self.make_request(path=ORGANIZATION_USERS_ENDPOINT, method="POST", data=data, headers=self.get_headers())

    def delete_user(self, data: dict) -> dict:
        return self.make_request(
            path=ORGANIZATION_USERS_ENDPOINT, method="DELETE", data=data, headers=self.get_headers()
        )

    def get_roles(self, parameters: dict) -> dict:
        return self.make_request(path=RBAC_ROLES_ENDPOINT, params=parameters, headers=self.get_headers())

    def get_role_by_id(self, role_id: dict) -> dict:
        return self.make_request(path=RBAC_ROLE_ENDPOINT.format(role_id=role_id), headers=self.get_headers())

    def make_request(  # noqa: C901
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        headers: dict = None,
    ) -> dict:
        try:
            response = requests.request(
                method=method.upper(),
                url=f"{self.base_url}{path}",
                json=json_data,
                params=params,
                data=data,
                headers=headers,
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Verify your input is correct and not malformed and try again. If the issue persists, "
                    "please contact support.",
                    data=response.text,
                )
            if 400 < response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                if ("alert_id" and "does not exist") in response.text:
                    raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code < 300:
                return clean(response.json())

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def split_url(url: str) -> str:
        scheme, netloc, paths, queries, fragments = urlsplit(url.strip())  # pylint: disable=unused-variable
        return f"{scheme}://{netloc}"
