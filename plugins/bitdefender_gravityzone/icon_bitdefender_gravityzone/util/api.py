import json
import time
import uuid
from logging import Logger
from typing import Any, Dict, List, Optional

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

API_VERSION = "v1.0"
NETWORK_API = "network"
INCIDENTS_API = "incidents"

REQUEST_TIMEOUT = 30  # seconds, applied to every request
MAX_RATE_LIMIT_RETRIES = 3
DEFAULT_RETRY_AFTER = 1  # seconds, used when HTTP 429 carries no usable Retry-After header
MAX_RETRY_AFTER = 60  # seconds; a longer Retry-After is not waited out
MAX_ERROR_BODY_LENGTH = 1000
MAX_PER_PAGE = 100  # upper limit of getEndpointsList in API v1.0

STATUS_CODE_ERRORS = {
    401: (
        "GravityZone rejected the API key (HTTP 401).",
        "Check that the API key in the connection is correct and active.",
    ),
    403: (
        "The API key is not allowed to use this GravityZone API (HTTP 403).",
        "Enable the Network API and the Incidents API for the API key in GravityZone Control Center.",
    ),
    404: (
        "The GravityZone API was not found at the configured URL (HTTP 404).",
        "Check that the URL in the connection is the Control Center URL, for example "
        "https://cloud.gravityzone.bitdefender.com.",
    ),
    429: (
        "GravityZone rate limit exceeded (HTTP 429).",
        "Wait before running the step again, or reduce how often workflows call GravityZone with this API key.",
    ),
}

API_ERROR_ASSISTANCE = {
    -32001: "Check that the API key is valid, that it has the Network API and the Incidents API enabled, and that "
    "the GravityZone license covers this operation.",
    -32002: "Check that the endpoint ID is correct and belongs to an endpoint that the API key can access.",
    -32602: "Check the action input: GravityZone rejected one of the parameters.",
}
DEFAULT_API_ERROR_ASSISTANCE = "Check the action input and the API key permissions, then try again."


def normalize_base_url(url: str) -> str:
    """Return the Control Center URL without a trailing slash or a trailing /api."""
    base_url = url.strip().rstrip("/")
    if base_url.lower().endswith("/api"):
        base_url = base_url[: -len("/api")].rstrip("/")
    return base_url


class BitdefenderGravityZoneAPI:
    """Client for the GravityZone JSON-RPC 2.0 public API."""

    def __init__(self, url: str, api_key: str, logger: Logger) -> None:
        self.base_url = normalize_base_url(url)
        self.logger = logger
        self.session = requests.Session()
        # GravityZone uses HTTP Basic authentication: the API key is the username and the password is empty
        self.session.auth = (api_key.strip(), "")
        self.session.headers.update({"Content-Type": "application/json", "Accept": "application/json"})

    def test_connection(self) -> None:
        self.get_endpoints_list(page=1, per_page=1)

    def get_endpoints_list(
        self,
        parent_id: Optional[str] = None,
        is_managed: Optional[bool] = None,
        page: int = 1,
        per_page: int = 30,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"page": page, "perPage": per_page}
        if parent_id:
            params["parentId"] = parent_id
        if is_managed is not None:
            params["isManaged"] = is_managed
        if filters:
            params["filters"] = filters
        return self._call(NETWORK_API, "getEndpointsList", params) or {}

    def get_managed_endpoints_by_name(self, name: str) -> List[Dict[str, Any]]:
        """
        Return every managed endpoint, in any group, whose name starts with the given value, reading all pages.
        The GravityZone name filter is a prefix match, so the caller must still compare the results exactly.
        """
        filters = {"details": {"name": name}, "depth": {"allItemsRecursively": True}}
        endpoints: List[Dict[str, Any]] = []
        page = 1
        while True:
            result = self.get_endpoints_list(is_managed=True, page=page, per_page=MAX_PER_PAGE, filters=filters)
            items = result.get("items") or []
            endpoints.extend(items)
            pages_count = result.get("pagesCount")
            is_last_page = page >= pages_count if isinstance(pages_count, int) else len(items) < MAX_PER_PAGE
            if not items or is_last_page:
                return endpoints
            page += 1

    def get_managed_endpoint_details(
        self, endpoint_id: str, include_scan_logs: bool = False, include_last_logged_users: bool = False
    ) -> Dict[str, Any]:
        params = {
            "endpointId": endpoint_id,
            "options": {"includeScanLogs": include_scan_logs, "includeLastLoggedUsers": include_last_logged_users},
        }
        return self._call(NETWORK_API, "getManagedEndpointDetails", params) or {}

    def isolate_endpoint(self, endpoint_id: str) -> None:
        self._create_endpoint_task("createIsolateEndpointTask", endpoint_id, "isolation")

    def restore_endpoint(self, endpoint_id: str) -> None:
        self._create_endpoint_task("createRestoreEndpointFromIsolationTask", endpoint_id, "restore")

    def _create_endpoint_task(self, method: str, endpoint_id: str, task_name: str) -> None:
        # In API v1.0 these methods return true once the task is created, so any other result is a failure
        result = self._call(INCIDENTS_API, method, {"endpointId": endpoint_id})
        if result is not True:
            raise PluginException(
                cause=f"GravityZone did not confirm that the {task_name} task was created.",
                assistance="Check that the endpoint ID belongs to a managed endpoint that supports this action, "
                "then try again.",
                data=f"{method} returned {json.dumps(result)}",
            )

    def _call(self, service: str, method: str, params: Dict[str, Any]) -> Any:
        url = f"{self.base_url}/api/{API_VERSION}/jsonrpc/{service}"
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": str(uuid.uuid4())}
        self.logger.info(f"Calling GravityZone method {method} on the {service} API")
        response_json = self._parse_response(self._post(url, payload))
        self._check_api_error(response_json)
        return response_json.get("result")

    def _post(self, url: str, payload: Dict[str, Any]) -> requests.Response:
        """Send the request, waiting and retrying while GravityZone answers HTTP 429."""
        response = self._send(url, payload)
        retries = 0
        while response.status_code == 429 and retries < MAX_RATE_LIMIT_RETRIES:
            retry_after = self._get_retry_after(response)
            if retry_after > MAX_RETRY_AFTER:
                break
            retries += 1
            self.logger.info(
                f"GravityZone rate limit reached. Retrying in {retry_after} seconds ({retries}/{MAX_RATE_LIMIT_RETRIES})"
            )
            time.sleep(retry_after)
            response = self._send(url, payload)
        self._check_status_code(response)
        return response

    def _send(self, url: str, payload: Dict[str, Any]) -> requests.Response:
        try:
            return self.session.post(url, json=payload, timeout=REQUEST_TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="The request to GravityZone timed out.",
                assistance="Check that GravityZone is reachable from the orchestrator, then try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to GravityZone.",
                assistance="Check the URL in the connection and that GravityZone is reachable from the orchestrator.",
                data=str(error),
            ) from error
        except requests.exceptions.RequestException as error:
            raise PluginException(
                cause="The request to GravityZone failed.",
                assistance="Check the URL in the connection, for example https://cloud.gravityzone.bitdefender.com.",
                data=str(error),
            ) from error

    @staticmethod
    def _get_retry_after(response: requests.Response) -> int:
        try:
            return max(int(response.headers.get("Retry-After", "")), 0)
        except ValueError:
            return DEFAULT_RETRY_AFTER

    def _check_status_code(self, response: requests.Response) -> None:
        status_code = response.status_code
        if 200 <= status_code < 300:
            return
        cause, assistance = STATUS_CODE_ERRORS.get(
            status_code,
            (
                f"GravityZone returned HTTP {status_code}.",
                "Check the URL in the connection and try again. If the problem continues, contact Bitdefender "
                "support with the response below.",
            ),
        )
        raise PluginException(cause=cause, assistance=assistance, data=self._body_excerpt(response))

    def _parse_response(self, response: requests.Response) -> Dict[str, Any]:
        try:
            response_json = response.json()
        except ValueError as error:
            raise PluginException(
                cause="GravityZone returned a response that is not JSON.",
                assistance="Check that the URL in the connection is the Control Center URL, for example "
                "https://cloud.gravityzone.bitdefender.com.",
                data=self._body_excerpt(response),
            ) from error
        if not isinstance(response_json, dict):
            raise PluginException(
                cause="GravityZone returned a response that is not a JSON-RPC object.",
                assistance="Check that the URL in the connection is the Control Center URL, for example "
                "https://cloud.gravityzone.bitdefender.com.",
                data=self._body_excerpt(response),
            )
        return response_json

    @staticmethod
    def _check_api_error(response_json: Dict[str, Any]) -> None:
        """Raise the JSON-RPC error that GravityZone reports with HTTP 200."""
        error = response_json.get("error")
        if not error:
            return
        if not isinstance(error, dict):
            error = {"message": str(error)}
        code = error.get("code")
        message = str(error.get("message") or "Unknown error").rstrip(".")
        raise PluginException(
            cause=f"GravityZone API error {code}: {message}.",
            assistance=API_ERROR_ASSISTANCE.get(code, DEFAULT_API_ERROR_ASSISTANCE),
            data=json.dumps(error),
        )

    @staticmethod
    def _body_excerpt(response: requests.Response) -> str:
        body = response.text or ""
        if len(body) > MAX_ERROR_BODY_LENGTH:
            return f"{body[:MAX_ERROR_BODY_LENGTH]}... (truncated, {len(body)} characters in total)"
        return body
