import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class SophosCentralAPI:
    def __init__(self, url, client_id, client_secret, tenant_id, logger):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.logger = logger

    def get_alerts(self, since: str = None, key: str = None):
        params = {
            "pageTotal": True
        }
        if since:
            params = {
                "from": since
            }
        if key:
            params = {
                "pageFromKey": key
            }
        return self._call_api(
            "GET",
            f"{self.url}/common/v1/alerts",
            "Tenant",
            params=params
        )

    def download_hashes(self):
        return self._make_request(
            "GET",
            f"https://api3.central.sophos.com/gateway/migration-tool/v1/download/hashes",
            headers={
                "x-api-key": self.client_id,
                "Authorization": f"Basic {self.client_secret}"
            }
        )

    def get_endpoints(self, since):
        params = {}
        if since:
            params = {
                "lastSeenAfter": since
            }
        return self._call_api(
            "GET",
            f"{self.url}/endpoint/v1/endpoints",
            "Tenant",
            params=params
        )

    def whoami(self, access_token):
        return self._make_request(
            "GET",
            "https://api.central.sophos.com/whoami/v1",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

    def get_access_token(self):
        token = self._make_request(
            method="POST",
            url="https://id.sophos.com/api/v2/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "token"
            }
        )

        return token.get("access_token")

    def _call_api(self, method, url, key_type, params=None, json_data=None):
        access_token = self.get_access_token()

        if self.tenant_id:
            id_ = self.tenant_id
        else:
            id_ = self.whoami(access_token)["id"]

        return self._make_request(
            method, url, params, json_data, headers={
                "Authorization": f"Bearer {access_token}",
                f"X-{key_type}-ID": id_
            }
        )

    def _make_request(self, method, url, params=None, json_data=None, data=None, headers=None):
        response = {"text": ""}
        try:
            response = requests.request(
                method,
                url,
                json=json_data,
                data=data,
                params=params,
                headers=headers
            )

            if response.status_code == 400:
                raise PluginException(cause="Bad request.",
                                      assistance="The API client sent a malformed request.")
            if response.status_code == 401:
                raise PluginException(cause="Unauthorized.",
                                      assistance="The client needs to authenticate before making the API call. "
                                                 "Either your credentials are invalid or blacklisted,"
                                                 " or your JWT authorization token has expired.")
            if response.status_code == 403:
                raise PluginException(
                    cause="Forbidden.",
                    assistance="The client has authenticated but doesn't have permission "
                               "to perform the operation via the API."
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Not found.",
                    assistance="The requested resource wasn't found. The resource ID provided may be invalid, "
                               "or the resource may have been deleted, or is no longer addressable."
                )
            if response.status_code == 409:
                raise PluginException(
                    cause="Conflict.",
                    assistance="Request made conflicts with an existing resource. Please check the API documentation "
                               "or contact Support."
                )
            if response.status_code == 451:
                raise PluginException(
                    cause="Unavailable for Legal Reasons",
                    assistance="An example of a legal reason we can't serve an API is that the caller is located "
                               "in a country where United States export control restrictions apply, "
                               "and we are required by law not to handle such API calls."
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if 200 <= response.status_code < 300:
                if response.text:
                    return response.json()
                return {}

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid json: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Sophos Central failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
