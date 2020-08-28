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

    def get_endpoint_id(self, entity):
        endpoint_id = None
        page_key = None

        for index in range(9999):
            get_agent = self.get_endpoints(page_key=page_key)
            page_key = get_agent.get("pages", {}).get("nextKey", None)

            for e in get_agent.get("items", []):
                if e.get("hostname") == entity:
                    endpoint_id = e.get("id")
                elif e.get("id") == entity:
                    endpoint_id = e.get("id")
                elif entity in e.get("ipv4Addresses", []):
                    endpoint_id = e.get("id")
                elif entity in e.get("macAddresses", []):
                    endpoint_id = e.get("id")
                elif entity in e.get("ipv6Addresses", []):
                    endpoint_id = e.get("id")

            if page_key is None or index > endpoint_id.get("pages", {}).get("total", 0):
                break

        if endpoint_id is None:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)

        return endpoint_id

    def tamper_status(self, endpoint_id):
        return self._make_request(
            "GET",
            f"/endpoint/v1/endpoints/{endpoint_id}/tamper-protection",
            "Tenant"
        )

    def get_blacklists(self, page: int = 1):
        return self._make_request(
            "GET",
            f"/endpoint/v1/settings/blocked-items",
            "Tenant",
            params={
                "page": page,
                "pageSize": 100,
                "pageTotal": True
            }
        )

    def unblacklist(self, uuid: str):
        return self._make_request(
            "DELETE",
            f"/endpoint/v1/settings/blocked-items/{uuid}",
            "Tenant"
        )

    def blacklist(self, hash: str, description: str):
        return self._make_request(
            "POST",
            f"/endpoint/v1/settings/blocked-items",
            "Tenant",
            json_data={
                "comment": description,
                "properties": {
                    "sha256": hash
                },
                "type": "sha256"
            }
        )

    def antivirus_scan(self, uuid: str):
        return self._make_request(
            "POST",
            f"/endpoint/v1/endpoints/{uuid}/scans",
            "Tenant",
            json_data={}
        )

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
        return self._make_request(
            "GET",
            f"/common/v1/alerts",
            "Tenant",
            params=params
        )

    def get_endpoints(self, since=None, page_key=None):
        params = {
            "pageTotal": True
        }
        if since:
            params = {
                "lastSeenAfter": since
            }
        if page_key:
            params = {
                "pageKey": page_key
            }
        return self._make_request(
            "GET",
            f"/endpoint/v1/endpoints",
            "Tenant",
            params=params
        )

    def whoami(self, access_token):
        return self._call_api(
            "GET",
            "https://api.central.sophos.com/whoami/v1",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )

    def get_access_token(self):
        token = self._call_api(
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

    def _make_request(self, method, path, key_type, params=None, json_data=None):
        access_token = self.get_access_token()
        whoami = self.whoami(access_token)

        url = None
        if self.tenant_id:
            id_ = self.tenant_id
        else:
            id_ = whoami["id"]
            url = whoami.get("apiHosts", {}).get("dataRegion")

        if not url:
            url = self.url

        return self._call_api(
            method, f"{url}{path}", params, json_data, headers={
                "Authorization": f"Bearer {access_token}",
                f"X-{key_type}-ID": id_
            }
        )

    def _call_api(self, method, url, params=None, json_data=None, data=None, headers=None):
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
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Sophos Central failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
