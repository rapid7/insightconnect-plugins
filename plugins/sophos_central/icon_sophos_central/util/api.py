import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json


class SophosCentralAPI:
    def __init__(self, url, client_id, client_secret, tenant_id, version, logger):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.version = version
        self.logger = logger

    def get_endpoint_id(self, entity):
        endpoint_id = None
        page_key = None

        for index in range(9999):
            get_agent = self.get_endpoints(page_key=page_key)
            pages = get_agent.get("pages", {})
            page_key = pages.get("nextKey", None)
            total_pages = pages.get("total", 0)

            for item in get_agent.get("items", []):
                if item.get("hostname") == entity:
                    endpoint_id = item.get("id")
                elif item.get("id") == entity:
                    endpoint_id = item.get("id")
                elif entity in item.get("ipv4Addresses", []):
                    endpoint_id = item.get("id")
                elif entity in item.get("macAddresses", []):
                    endpoint_id = item.get("id")
                elif entity in item.get("ipv6Addresses", []):
                    endpoint_id = item.get("id")
            if page_key is None or index > total_pages:
                break

        if endpoint_id is None:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)

        return endpoint_id

    def tamper_status(self, endpoint_id):
        return self._make_request("GET", f"/endpoint/v1/endpoints/{endpoint_id}/tamper-protection", "Tenant")

    def get_blacklists(self, page: int = 1):
        return self._make_request(
            "GET",
            "/endpoint/v1/settings/blocked-items",
            "Tenant",
            params={"page": page, "pageSize": 100, "pageTotal": True},
        )

    def unblacklist(self, uuid: str):
        return self._make_request("DELETE", f"/endpoint/v1/settings/blocked-items/{uuid}", "Tenant")

    def blacklist(self, hash_: str, description: str):
        return self._make_request(
            "POST",
            "/endpoint/v1/settings/blocked-items",
            "Tenant",
            json_data={"comment": description, "properties": {"sha256": hash_}, "type": "sha256"},
        )

    def antivirus_scan(self, uuid: str):
        return self._make_request("POST", f"/endpoint/v1/endpoints/{uuid}/scans", "Tenant", json_data={})

    def get_alerts(self, since: str = None, key: str = None):
        params = {"pageTotal": True}
        if since:
            params = {"from": since}
        if key:
            params = {"pageFromKey": key}
        return self._make_request("GET", "/common/v1/alerts", "Tenant", params=params)

    def get_endpoints(self, since=None, page_key=None):
        params = {"pageTotal": True}
        if since:
            params = {"lastSeenAfter": since}
        if page_key:
            params = {"pageKey": page_key}
        return self._make_request("GET", "/endpoint/v1/endpoints", "Tenant", params=params)

    def get_blocked_items(self, params: dict) -> dict:
        return self._make_request("GET", "/endpoint/v1/settings/blocked-items", "Tenant", params=params)

    def add_blocked_item(self, item_data: dict) -> dict:
        return self._make_request("POST", "/endpoint/v1/settings/blocked-items", "Tenant", json_data=item_data)

    def remove_blocked_item(self, item_id: str) -> bool:
        self._make_request("DELETE", f"/endpoint/v1/settings/blocked-items/{item_id}", "Tenant")
        return True

    def get_endpoint_groups(self, params: dict = {}) -> dict:
        return self._make_request("GET", "/endpoint/v1/endpoint-groups", "Tenant", params=params)

    def get_allowed_items(self, params: dict = {}) -> dict:
        return self._make_request("GET", "/endpoint/v1/settings/allowed-items", "Tenant", params=params)

    def add_allowed_item(self, item_data: dict = {}) -> dict:
        return self._make_request("POST", "/endpoint/v1/settings/allowed-items", "Tenant", json_data=item_data)

    def remove_allowed_item(self, allowed_item_id: str = None) -> dict:
        return self._make_request("DELETE", f"/endpoint/v1/settings/allowed-items/{allowed_item_id}", "Tenant")

    def isolate_endpoint(self, json_data: dict) -> dict:
        return self._make_request("POST", "/endpoint/v1/endpoints/isolation", "Tenant", json_data=json_data)

    def add_endpoint_group(self, json_data: dict) -> dict:
        return self._make_request("POST", "/endpoint/v1/endpoint-groups", "Tenant", json_data=json_data)

    def get_endpoint_group(self, group_id: str) -> dict:
        return self._make_request("GET", f"/endpoint/v1/endpoint-groups/{group_id}", "Tenant")

    def add_endpoint_to_group(self, group_id: str, json_data: dict) -> dict:
        return self._make_request(
            "POST", f"/endpoint/v1/endpoint-groups/{group_id}/endpoints", "Tenant", json_data=json_data
        )

    def remove_endpoint_from_group(self, group_id: str, parameters: dict) -> dict:
        return self._make_request(
            "DELETE", f"/endpoint/v1/endpoint-groups/{group_id}/endpoints", "Tenant", params=parameters
        )

    def get_endpoints_in_group(self, group_id: str, parameters: dict) -> dict:
        return self._make_request(
            "GET", f"/endpoint/v1/endpoint-groups/{group_id}/endpoints", "Tenant", params=parameters
        )

    def whoami(self, access_token):
        return self._call_api(
            "GET",
            "https://api.central.sophos.com/whoami/v1",
            headers={"Authorization": f"Bearer {access_token}"},
        )

    def get_access_token(self):
        token = self._call_api(
            method="POST",
            url="https://id.sophos.com/api/v2/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "token",
            },
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
            method,
            f"{url}{path}",
            params,
            json_data,
            headers={"Authorization": f"Bearer {access_token}", f"X-{key_type}-ID": id_},
        )

    def _call_api(self, method, url, params=None, json_data=None, data=None, headers=None):  # noqa: C901
        response = {"text": ""}
        if not headers:
            headers = {}
        headers["User-Agent"] = f"Rapid7 InsightConnect, Sophos Central:{self.version}"

        try:
            response = requests.request(method, url, json=json_data, data=data, params=params, headers=headers)

            if response.status_code == 400:
                raise PluginException(
                    cause="Bad request.", assistance="The API client sent a malformed request.", data=response.text
                )
            if response.status_code == 401:
                raise PluginException(
                    cause="Unauthorized.",
                    assistance="The client needs to authenticate before making the API call. "
                    "Either your credentials are invalid or blacklisted,"
                    " or your JWT authorization token has expired.",
                )
            if response.status_code == 403:
                raise PluginException(
                    cause="Forbidden.",
                    assistance="The client has authenticated but doesn't have permission "
                    "to perform the operation via the API.",
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Not found.",
                    assistance="The requested resource wasn't found. The resource ID provided may be invalid, "
                    "or the resource may have been deleted, or is no longer addressable.",
                )
            if response.status_code == 409:
                raise PluginException(
                    cause="Conflict.",
                    assistance="Request made conflicts with an existing resource. Please check the API documentation "
                    "or contact Support.",
                    data=response.text,
                )
            if response.status_code == 451:
                raise PluginException(
                    cause="Unavailable for Legal Reasons",
                    assistance="An example of a legal reason we can't serve an API is that the caller is located "
                    "in a country where United States export control restrictions apply, "
                    "and we are required by law not to handle such API calls.",
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
