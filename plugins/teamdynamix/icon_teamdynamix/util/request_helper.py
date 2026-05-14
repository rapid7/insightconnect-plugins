"""TeamDynamix API request helper."""

from typing import Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_teamdynamix.util.constants import API_BASE_PATH, AUTH_ENDPOINT, HTTP_ERROR_MAP, TIMEOUT


class TeamDynamixClient:
    """Handles authentication and HTTP requests to the TeamDynamix Web API."""

    def __init__(self, base_url: str, beid: str, web_services_key: str, app_id: int, logger=None):
        self.base_url = base_url.rstrip("/")
        self.beid = beid
        self.web_services_key = web_services_key
        self.app_id = app_id
        self.logger = logger
        self._token = None
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

    @property
    def tickets_endpoint(self) -> str:
        """Base endpoint for ticket operations."""
        return f"{API_BASE_PATH}/{self.app_id}/tickets"

    def _authenticate(self) -> str:
        """Authenticate with TeamDynamix API using BEID and Web Services Key.
        Returns a bearer token string."""
        url = f"{self.base_url}{AUTH_ENDPOINT}"
        payload = {"BEID": self.beid, "WebServicesKey": self.web_services_key}

        if self.logger:
            self.logger.info(f"TeamDynamixClient: Authenticating at {url}")

        try:
            resp = self._session.post(url, json=payload, timeout=TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Authentication request to TeamDynamix timed out.",
                assistance=f"Verify the base URL is correct and the instance is reachable: {self.base_url}",
                data=str(error),
            )
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to TeamDynamix.",
                assistance=f"Verify the base URL is correct and network connectivity exists: {self.base_url}",
                data=str(error),
            )

        if resp.status_code != 200:
            raise PluginException(
                cause=f"TeamDynamix authentication failed with status {resp.status_code}.",
                assistance="Verify BEID and Web Services Key are correct and the admin service account is active.",
                data=resp.text,
            )

        token = resp.text.strip().strip('"')
        if not token:
            raise PluginException(
                cause="TeamDynamix returned an empty authentication token.",
                assistance="Check BEID and Web Services Key in your connection settings.",
            )

        return token

    def _get_token(self) -> str:
        """Return a valid bearer token, authenticating if necessary."""
        if not self._token:
            self._token = self._authenticate()
        return self._token

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self._get_token()}",
            "Content-Type": "application/json",
        }

    def _handle_status(self, status_code: int, response_text: str) -> None:
        """Raise PluginException with mapped error details for non-success status codes."""
        if 200 <= status_code < 300:
            return

        error_info = HTTP_ERROR_MAP.get(status_code, {})
        cause = error_info.get("cause", f"TeamDynamix API returned status {status_code}.")
        assistance = error_info.get("assistance", "Review the response for details.")

        raise PluginException(cause=cause, assistance=assistance, data=response_text)

    def make_request(
        self, method: str, endpoint: str, payload: dict = None, params: dict = None
    ) -> Union[dict, list]:
        """Make an authenticated request to the TeamDynamix API.

        Args:
            method: HTTP method ('get', 'post', 'patch', 'put', 'delete')
            endpoint: API endpoint path, e.g. '/TDWebApi/api/42/tickets'
            payload: JSON body dict (for POST/PATCH/PUT)
            params: Query parameters dict

        Returns:
            Parsed JSON response (dict or list), or empty dict for 204 responses.

        Raises:
            PluginException on HTTP errors, timeouts, or connection failures.
        """
        url = f"{self.base_url}{endpoint}"
        if self.logger:
            self.logger.info(f"TeamDynamixClient: {method.upper()} {url}")

        try:
            resp = self._session.request(
                method=method.upper(),
                url=url,
                headers=self._headers(),
                json=payload,
                params=params,
                timeout=TIMEOUT,
            )
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Request to TeamDynamix timed out.",
                assistance="The API did not respond within the timeout period. Retry the request.",
                data=str(error),
            )
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to TeamDynamix.",
                assistance=f"Verify network connectivity and that the instance is reachable: {self.base_url}",
                data=str(error),
            )

        # Handle token expiry with one retry
        if resp.status_code == 401:
            if self.logger:
                self.logger.info("TeamDynamixClient: Token expired, re-authenticating...")
            self._token = self._authenticate()
            try:
                resp = self._session.request(
                    method=method.upper(),
                    url=url,
                    headers=self._headers(),
                    json=payload,
                    params=params,
                    timeout=TIMEOUT,
                )
            except requests.exceptions.Timeout as error:
                raise PluginException(
                    cause="Request to TeamDynamix timed out after re-authentication.",
                    assistance="The API did not respond within the timeout period. Retry the request.",
                    data=str(error),
                )
            except requests.exceptions.ConnectionError as error:
                raise PluginException(
                    cause="Unable to connect to TeamDynamix after re-authentication.",
                    assistance=f"Verify network connectivity: {self.base_url}",
                    data=str(error),
                )

        if resp.status_code == 204:
            return {}

        self._handle_status(resp.status_code, resp.text)

        try:
            return resp.json()
        except ValueError:
            raise PluginException(
                cause="TeamDynamix API returned non-JSON response.",
                assistance="The API returned an unexpected response format.",
                data=resp.text,
            )

    def get_ticket(self, ticket_id: int) -> dict:
        """Get a single ticket by ID."""
        return self.make_request(method="get", endpoint=f"{self.tickets_endpoint}/{ticket_id}")

    def create_ticket(self, payload: dict) -> dict:
        """Create a new ticket."""
        return self.make_request(method="post", endpoint=self.tickets_endpoint, payload=payload)

    def update_ticket(self, ticket_id: int, payload: dict) -> dict:
        """Update an existing ticket (full edit via POST)."""
        return self.make_request(method="post", endpoint=f"{self.tickets_endpoint}/{ticket_id}", payload=payload)

    def search_tickets(self, payload: dict) -> list:
        """Search for tickets."""
        response = self.make_request(method="post", endpoint=f"{self.tickets_endpoint}/search", payload=payload)
        return response if isinstance(response, list) else []

    def test(self) -> bool:
        """Test the connection by performing a minimal ticket search."""
        self.search_tickets(payload={"MaxResults": 1})
        return True
