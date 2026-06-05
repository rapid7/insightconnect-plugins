import base64
from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class BitdefenderGravityZoneAPI:
    """Centralized API client for Bitdefender GravityZone JSON-RPC calls."""

    def __init__(self, base_url: str, api_key: str, logger: Logger):
        self.base_url = base_url.strip().rstrip("/")
        self.logger = logger

        # Bitdefender uses HTTP Basic Auth: username=api_key, password=empty
        login_string = f"{api_key.strip()}:"
        encoded_creds = base64.b64encode(login_string.encode("utf-8")).decode("utf-8")

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Basic {encoded_creds}",
                "Content-Type": "application/json",
            }
        )

    def _call(self, service: str, method: str, params: dict, request_id: str = "insightconnect") -> dict:
        """
        Execute a JSON-RPC 2.0 call against the GravityZone API.

        :param service: The API service path (e.g., "network", "incidents", "licensing")
        :param method: The JSON-RPC method name
        :param params: The method parameters
        :param request_id: Optional request ID for tracking
        :return: The 'result' field from the JSON-RPC response
        """
        url = f"{self.base_url}/api/v1.0/jsonrpc/{service}"

        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": request_id,
        }

        self.logger.info(f"Calling {method} on {service}")

        response = self._send_request(url, payload)
        self._check_status_code(response)
        response_json = self._parse_response(response)

        if "error" in response_json:
            error_obj = response_json.get("error", {})
            raise PluginException(
                cause=f"Bitdefender API error: {error_obj.get('message', 'Unknown error')} "
                f"(code: {error_obj.get('code', 'N/A')})",
                assistance="Please verify your input parameters and API key permissions.",
                data=str(error_obj),
            )

        return response_json.get("result", {})

    def _send_request(self, url: str, payload: dict) -> requests.Response:
        """Send the HTTP request, raising PluginException on transport errors."""
        try:
            return self.session.post(url, json=payload, verify=True, timeout=30)
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to the Bitdefender GravityZone API.",
                assistance="Please verify the Access URL is correct and the server is reachable.",
                data=str(error),
            )
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="The request to Bitdefender GravityZone API timed out.",
                assistance="Please verify network connectivity and try again.",
                data=str(error),
            )
        except requests.exceptions.RequestException as error:
            raise PluginException(
                cause="An error occurred communicating with the Bitdefender GravityZone API.",
                assistance="Please check your configuration and try again.",
                data=str(error),
            )

    @staticmethod
    def _check_status_code(response: requests.Response) -> None:
        """Validate the HTTP status code, raising PluginException on errors."""
        if response.status_code == 401:
            raise PluginException(
                cause="Authentication failed.",
                assistance="Please verify that your API key is valid and active.",
            )
        if response.status_code == 403:
            raise PluginException(
                cause="Authorization failed.",
                assistance="The API key does not have the required permissions for this operation.",
            )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            raise PluginException(
                cause=f"Received HTTP {response.status_code} from the GravityZone API.",
                assistance="Please check your request parameters and try again.",
                data=str(error),
            )

    @staticmethod
    def _parse_response(response: requests.Response) -> dict:
        """Parse the JSON body from the response."""
        try:
            return response.json()
        except ValueError as error:
            raise PluginException(
                cause="The GravityZone API returned a non-JSON response.",
                assistance="This may indicate a configuration issue with the Access URL.",
                data=str(error),
            )

    def test_connection(self) -> dict:
        """Validate credentials with a lightweight API call."""
        return self._call(
            service="general",
            method="getApiKeyDetails",
            params={},
            request_id="insightconnect-connection-test",
        )

    def get_endpoints_list(
        self,
        parent_id: str = None,
        is_managed: bool = None,
        page: int = 1,
        per_page: int = 30,
        name_filter: str = None,
    ) -> dict:
        """
        Retrieve a paginated list of endpoints.

        :return: Dict with keys: items, page, pagesCount, perPage, total
        """
        params = {
            "page": page,
            "perPage": per_page,
        }

        if parent_id:
            params["parentId"] = parent_id
        if is_managed is not None:
            params["isManaged"] = is_managed

        filters = {}
        if name_filter:
            filters["name"] = {"type": "String", "value": name_filter}
        if filters:
            params["filters"] = filters

        return self._call(
            service="network",
            method="getEndpointsList",
            params=params,
            request_id="insightconnect-get-endpoints",
        )

    def isolate_endpoint(self, endpoint_id: str) -> bool:
        """
        Create an isolation task for a single endpoint.

        :return: True if the task was created successfully
        """
        params = {
            "endpointId": endpoint_id,
        }

        result = self._call(
            service="incidents",
            method="createIsolateEndpointTask",
            params=params,
            request_id="insightconnect-isolate-endpoint",
        )

        # API returns True on success or a task ID
        if isinstance(result, bool):
            return result
        return True
