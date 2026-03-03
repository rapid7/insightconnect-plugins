import json
from logging import Logger
from typing import Any

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from insightconnect_plugin_runtime.exceptions import PluginException


class JiraServiceManagementApi:

    def __init__(self, client_id: str, client_secret: str, instance: str, logger: Logger) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.instance = instance
        self.logger = logger
        self.authorization = {"Authorization": f"Bearer {self._get_token()}"}
        self.cloud_id = self._get_cloud_id()

    def _get_token(self) -> str:
        return self.make_request(
            method="POST",
            url="https://auth.atlassian.com/oauth/token",
            payload={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "audience": "api.atlassian.com",
            },
            headers={"Content-Type": "application/json"},
        ).get("access_token")

    def _get_cloud_id(self) -> str:
        resources = self.make_request(
            method="GET",
            url="https://api.atlassian.com/oauth/token/accessible-resources",
            headers=self.authorization,
        )

        for resource in resources:
            if resource.get("name", "") == self.instance:
                return resource.get("id", "")
        raise PluginException(
            cause=f"No accessible resource found for instance: {self.instance}.",
            assistance="Please provide a valid instance name.",
        )

    def make_request(  # noqa: MC0001
        self,
        method: str,
        url: str,
        headers: dict[str, Any] = None,
        params: dict[str, Any] = None,
        payload: dict[str, Any] = None,
        timeout: int = REQUESTS_TIMEOUT,
    ) -> dict[str, Any]:
        try:
            if headers is None:
                headers = {"Accept": "application/json"}

            if hasattr(self, "authorization") and self.authorization:
                headers.update(self.authorization)

            response = requests.request(
                method.upper(),
                url,
                params=params,
                json=payload,
                headers=headers,
                timeout=timeout,
            )

            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if response.status_code == 422:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code < 300:
                return response.json()
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
