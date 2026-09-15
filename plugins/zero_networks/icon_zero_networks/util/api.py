import logging
from typing import Any, Dict, Optional

from insightconnect_plugin_runtime.exceptions import (
    APIException,
    HTTPStatusCodes,
    PluginException,
    ResponseExceptionData,
)
from insightconnect_plugin_runtime.helper import make_request
from requests import Request, Response


class ZeroNetworksAPI:
    """
    Thin client for the Zero Networks API.

    Authentication is a plain API key sent in the ``Authorization`` header, as described by
    the ``api_key`` security scheme in the Zero Networks OpenAPI document.
    """

    DEFAULT_TIMEOUT = 60

    def __init__(self, url: str, api_key: str, logger: logging.Logger) -> None:
        self.url = url.rstrip("/")
        self.api_key = api_key
        self.logger = logger

    def test_connection(self) -> None:
        """Make the cheapest authenticated call available to confirm the URL and API key work."""
        self._call("GET", "/assets", params={"_limit": 1})

    def search_asset_id(self, fqdn: str) -> Optional[str]:
        """
        Look up an asset ID by fully qualified domain name.

        Zero Networks answers with ``200`` and an object that has no ``assetId`` when nothing
        matches, and with ``404`` in some deployments - both mean "not found", so both return None.
        """
        try:
            response = self._call("GET", "/assets/searchId", params={"fqdn": fqdn})
        except APIException as error:
            if error.status_code == HTTPStatusCodes.NOT_FOUND:
                self.logger.info(f"No asset found for FQDN {fqdn}")
                return None
            raise

        return response.get("assetId") or None

    def set_asset_quarantine(self, asset_id: str, quarantine: bool) -> None:
        """Enable or disable quarantine for an asset. The API replies with an empty object."""
        self._call("PUT", f"/assets/{asset_id}/actions/quarantine", json_data={"quarantine": quarantine})

    def _call(
        self, method: str, endpoint: str, params: Dict[str, Any] = None, json_data: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        url = f"{self.url}{endpoint}"
        request = Request(
            method=method,
            url=url,
            headers={"Authorization": self.api_key, "Accept": "application/json"},
            params=params,
            json=json_data,
        )

        try:
            response = make_request(
                _request=request,
                timeout=self.DEFAULT_TIMEOUT,
                exception_custom_configs={
                    HTTPStatusCodes.UNAUTHORIZED: PluginException(
                        cause="The Zero Networks API rejected the provided API key.",
                        assistance="Verify the API key in the connection configuration and try again.",
                    ),
                    HTTPStatusCodes.FORBIDDEN: PluginException(
                        cause="The provided API key is not permitted to perform this operation.",
                        assistance="Verify that the API key has the required permissions in the Zero Networks portal.",
                    ),
                    HTTPStatusCodes.NOT_FOUND: PluginException(
                        cause=f"The Zero Networks API returned no resource at {url}.",
                        assistance="Verify the URL connection setting and the supplied identifiers, then try again.",
                    ),
                },
                exception_data_location=ResponseExceptionData.RESPONSE,
            )
        except PluginException as error:
            if isinstance(error.data, Response):
                raise APIException(
                    cause=error.cause,
                    assistance=error.assistance,
                    data=error.data.text,
                    status_code=error.data.status_code,
                ) from error
            raise

        return self._to_json(response)

    @staticmethod
    def _to_json(response: Response) -> Dict[str, Any]:
        """Return the decoded body, tolerating the empty bodies the action endpoints reply with."""
        if not response.content:
            return {}

        try:
            body = response.json()
        except ValueError as error:
            raise PluginException(
                preset=PluginException.Preset.INVALID_JSON,
                data=response.text,
            ) from error

        return body if isinstance(body, dict) else {}
