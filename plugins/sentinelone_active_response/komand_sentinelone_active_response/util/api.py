import requests
from json import JSONDecodeError
from logging import Logger

from insightconnect_plugin_runtime.exceptions import PluginException

from .constants import TIMEOUT, API_VERSION, HTTP_ERROR_MAP
from .endpoints import VIEWER_AUTH_CHECK, SEARCH_AGENTS, DISCONNECT_AGENTS, CONNECT_AGENTS


class SentinelOneAPI:
    """
    Handles all HTTP communication with SentinelOne REST API v2.1.

    Methods:
    - test_connection() -> dict
    - search_agents(query_params: dict) -> list[dict]
    - disconnect_agents(agent_ids: list[str]) -> dict
    - connect_agents(agent_ids: list[str]) -> dict
    - get_agent_by_id(agent_id: str) -> dict
    """

    def __init__(self, base_url: str, api_key: str, logger: Logger):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.logger = logger

    def test_connection(self) -> dict:
        """Validate credentials via GET /web/api/v2.1/users/viewer-auth-check."""
        return self._make_request("GET", VIEWER_AUTH_CHECK)

    def search_agents(self, query_params: dict) -> list:
        """Search agents with the given query parameters. Returns the data list from the response."""
        response = self._make_request("GET", SEARCH_AGENTS, params=query_params)
        return response.get("data", [])

    def disconnect_agents(self, agent_ids: list) -> dict:
        """Disconnect (contain) agents by their IDs."""
        return self._make_request("POST", DISCONNECT_AGENTS, json={"filter": {"ids": agent_ids}})

    def connect_agents(self, agent_ids: list) -> dict:
        """Connect (uncontain) agents by their IDs."""
        return self._make_request("POST", CONNECT_AGENTS, json={"filter": {"ids": agent_ids}})

    def get_agent_by_id(self, agent_id: str) -> dict:
        """Retrieve a single agent by its ID. Returns the agent dict or empty dict if not found."""
        agents = self.search_agents({"ids": agent_id})
        if agents:
            return agents[0]
        return {}

    def _make_request(self, method: str, endpoint: str, **kwargs) -> dict:
        """
        Central request method with error handling.

        Constructs the full URL, sets authorization headers, and handles
        HTTP errors, timeouts, connection errors, and JSON decode failures.
        """
        url = f"{self.base_url}/web/api/v{API_VERSION}/{endpoint}"
        headers = {
            "Authorization": f"APIToken {self.api_key}",
            "Content-Type": "application/json",
        }

        kwargs.setdefault("timeout", TIMEOUT)
        kwargs["headers"] = headers

        try:
            response = requests.request(method, url, **kwargs)  # pylint: disable=missing-timeout
            self._raise_for_status(response)
            return response.json()
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Request timed out.",
                assistance=f"The request to {endpoint} exceeded the {TIMEOUT}s timeout. Try again later.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to SentinelOne.",
                assistance=f"Verify the instance URL is correct and reachable: {self.base_url}",
                data=str(error),
            ) from error
        except JSONDecodeError as error:
            raise PluginException(
                cause="Received an unexpected response from SentinelOne.",
                assistance="The response could not be parsed as JSON. This may indicate an issue with the SentinelOne service.",
                data=str(error),
            ) from error

    @staticmethod
    def _raise_for_status(response: requests.Response) -> None:
        """Check HTTP status and raise PluginException using HTTP_ERROR_MAP for known error codes."""
        status_code = response.status_code
        if 200 <= status_code < 300:
            return

        error_info = HTTP_ERROR_MAP.get(status_code)
        if error_info:
            raise PluginException(
                cause=error_info["cause"],
                assistance=error_info["assistance"],
                data=response.text,
            )

        # Fallback for unmapped error codes
        raise PluginException(
            cause=f"SentinelOne API returned an unexpected status code: {status_code}.",
            assistance="Check the SentinelOne API documentation or contact support.",
            data=response.text,
        )
