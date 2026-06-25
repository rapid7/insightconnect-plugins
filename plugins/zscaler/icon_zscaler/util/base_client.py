import time
from abc import ABC, abstractmethod

import jwt
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_zscaler.util.constants import (
    HTTP_ERROR_MAP,
    Assistance,
    Cause,
)


class BaseClient(ABC):
    """Base client for Zscaler OneAPI with OAuth 2.0 Client Credentials (Private Key) authentication."""

    BASE_URL = "https://api.zsapi.net"
    TOKEN_EXPIRY_BUFFER = 30  # seconds before expiry to trigger refresh

    def __init__(self, client_id: str, private_key: str, vanity_domain: str, cloud: str, logger: object):
        self.client_id = client_id
        self.private_key = private_key
        self.vanity_domain = vanity_domain
        self.cloud = cloud
        self.logger = logger
        self.base_url = self.BASE_URL
        self.service_prefix = ""  # Set by subclasses (e.g., "/zia/api/v1", "/zpa/api/v1")
        self._token = None
        self._token_expiry = 0

    @property
    def token_endpoint(self) -> str:
        return f"https://{self.vanity_domain}.{self.cloud}/oauth2/v1/token"

    def _authenticate(self) -> None:
        """Authenticate via OAuth 2.0 Client Credentials with Private Key JWT assertion."""
        now = int(time.time())
        claims = {
            "iss": self.client_id,
            "sub": self.client_id,
            "aud": self.token_endpoint,
            "iat": now,
            "exp": now + 300,  # 5 minutes
        }

        self.logger.info("Building JWT assertion for OAuth 2.0 authentication...")
        assertion = jwt.encode(claims, self.private_key, algorithm="RS256")

        body = (
            "grant_type=client_credentials"
            "&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
            f"&client_assertion={assertion}"
        )

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        self.logger.info(f"Requesting OAuth token from {self.token_endpoint}")
        try:
            response = requests.request(
                method="POST",
                url=self.token_endpoint,
                data=body,
                headers=headers,
            )
        except requests.exceptions.Timeout:
            raise PluginException(
                cause="Timeout while requesting OAuth token.",
                assistance="Verify network connectivity and that the Zscaler identity provider is reachable.",
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(
                cause="Connection error while requesting OAuth token.",
                assistance="Verify the vanity_domain and cloud settings are correct and the identity provider is reachable.",
            )

        if response.status_code != 200:
            raise PluginException(
                cause="Failed to obtain OAuth 2.0 access token.",
                assistance=(
                    f"Token endpoint returned HTTP {response.status_code}. "
                    "Verify that client_id, private_key, vanity_domain, and cloud are correct."
                ),
                data=response.text,
            )

        token_data = response.json()
        self._token = token_data.get("access_token")
        expires_in = token_data.get("expires_in", 3600)
        self._token_expiry = int(time.time()) + expires_in
        self.logger.info("OAuth 2.0 token obtained successfully.")

    def _get_token(self) -> str:
        """Return cached token or refresh if expired/near-expiry (30s buffer)."""
        if self._token is None or time.time() >= (self._token_expiry - self.TOKEN_EXPIRY_BUFFER):
            self.logger.info("Token missing or near expiry, refreshing...")
            self._authenticate()
        return self._token

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Build full URL with service prefix and make an authenticated API request."""
        url = f"{self.base_url}{self.service_prefix}/{endpoint}"
        token = self._get_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        return self._call_api(method, url, headers=headers, **kwargs)

    def _call_api(self, method: str, url: str, **kwargs) -> requests.Response:
        """Execute HTTP request using requests.request() (no Session). Handle transport errors."""
        try:
            response = requests.request(method=method, url=url, **kwargs)
        except requests.exceptions.Timeout:
            raise PluginException(
                cause="Request timed out.",
                assistance="The Zscaler API did not respond in time. Retry the request or check network connectivity.",
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(
                cause="Connection error occurred.",
                assistance="Unable to reach the Zscaler API. Verify network connectivity and API availability.",
            )

        return self._handle_status(response, method, url, **kwargs)

    def _handle_status(self, response: requests.Response, method: str, url: str, **kwargs) -> requests.Response:
        """Map HTTP status codes to PluginException using HTTP_ERROR_MAP. Handle 401 with one retry."""
        status_code = response.status_code

        if 200 <= status_code < 300:
            return response

        # Handle 401 with one re-authentication retry
        if status_code == 401:
            self.logger.info("Received 401 Unauthorized. Re-authenticating and retrying...")
            self._authenticate()
            # Update the Authorization header with the new token
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self._token}"
            kwargs["headers"] = headers

            try:
                retry_response = requests.request(method=method, url=url, **kwargs)
            except requests.exceptions.Timeout:
                raise PluginException(
                    cause="Request timed out on retry.",
                    assistance="The Zscaler API did not respond in time after re-authentication.",
                )
            except requests.exceptions.ConnectionError:
                raise PluginException(
                    cause="Connection error on retry.",
                    assistance="Unable to reach the Zscaler API after re-authentication.",
                )

            if 200 <= retry_response.status_code < 300:
                return retry_response

            # Still 401 after retry — raise auth error
            if retry_response.status_code == 401:
                error_info = HTTP_ERROR_MAP.get(401, {})
                raise PluginException(
                    cause=error_info.get("cause", Cause.TOKEN_EXPIRED),
                    assistance=error_info.get("assistance", Assistance.REAUTHENTICATE),
                    data=retry_response.text,
                )

            # Different error after retry — handle normally
            return self._raise_for_status(retry_response)

        return self._raise_for_status(response)

    def _raise_for_status(self, response: requests.Response) -> requests.Response:
        """Raise PluginException for non-2xx responses using HTTP_ERROR_MAP."""
        status_code = response.status_code

        if 200 <= status_code < 300:
            return response

        error_info = HTTP_ERROR_MAP.get(status_code)

        if error_info:
            if status_code == 429:
                retry_after = response.headers.get("Retry-After", "unknown")
                self.logger.info(f"Rate limited. Retry-After: {retry_after}")
            raise PluginException(
                cause=error_info["cause"],
                assistance=error_info["assistance"],
                data=response.text,
            )

        # Fallback for unmapped status codes
        raise PluginException(
            cause=f"Unexpected HTTP status code: {status_code}",
            assistance="An unexpected error occurred. Please contact support if the issue persists.",
            data=response.text,
        )

    @abstractmethod
    def test(self) -> dict:
        """Test connectivity to the Zscaler API. Implemented by subclasses."""
