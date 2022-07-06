from json import JSONDecodeError
from logging import Logger
from typing import List, Optional, Union, Callable

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .endpoints import Endpoint
from .tools import Message, rate_limiting

MAX_TRIES = 10

KEYS_TO_REMOVE = ("@odata.context",)


class AzureClient:
    def __init__(self):
        self.auth_token = ""  # nosec

    def _get_auth_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.auth_token}"}

    def _get_auth_token(self, tenant_id: str, client_id: str, client_secret: str, resource: str) -> None:
        get_auth_token_url = Endpoint.GET_AUTH_TOKEN.format(tenant_id)

        self.logger.info("Updating auth token...")

        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "resource": resource,
        }

        response = self._call_api("POST", get_auth_token_url, data=data)

        self.auth_token = response.get("access_token")
        self.logger.info(f"Authentication Token: ****************{self.auth_token[-5:]}")

    @rate_limiting(max_tries=MAX_TRIES)
    def _call_api(
        self,
        method: str,
        url: str,
        data: dict = None,
        json_data: Union[List[dict], dict] = None,
        params: dict = None,
    ) -> Union[List[dict], dict]:
        try:
            response = requests.request(
                method, url, headers=self._get_auth_headers(), data=data, json=json_data, params=params
            )
            if response.status_code == 400:
                raise PluginException(cause=Message.BAD_REQUEST_MESSAGE, data=response.text)
            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(
                    cause=Message.RESOURCE_WAS_NOT_FOUND_CAUSE,
                    assistance=Message.RESOURCE_WAS_NOT_FOUND_ASSISTANCE,
                    data=response.json().get("error", {}).get("message", ""),
                )
            if response.status_code in (429, 503):
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if response.status_code == 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
            if 200 <= response.status_code < 300:
                return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        self.logger.info("Call to Microsoft Defender API failed")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)


class MicrosoftDefenderClientAPI(AzureClient):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        tenant_id: str,
        logger: Optional[Logger] = None,
    ):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.logger = logger

    def _connection(func: Callable) -> None:
        """connection. Decorator allows to obtain access token automatically and update headers.
        :param func: Function to be decorated
        :type func: Callable
        :rtype: None
        """

        def _wrapper(self, *args, **kwargs):
            # pylint: disable=protected-access, not-callable
            self._get_auth_token(self.tenant_id, self.client_id, self.client_secret, Endpoint.RESOURCE_SECURITY)
            return func(self, *args, **kwargs)

        return _wrapper

    @_connection
    def advanced_hunting(self, query: str) -> dict:
        return self._call_api("POST", Endpoint.ADVANCED_HUNTING, json_data={"Query": query})

    @_connection
    def test_connection(self) -> None:
        pass
