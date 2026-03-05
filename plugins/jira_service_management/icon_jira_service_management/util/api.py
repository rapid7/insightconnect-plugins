import json
from logging import Logger
from typing import Any

import requests

from icon_jira_service_management.util.constants import REQUESTS_TIMEOUT
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import make_request


class JiraServiceManagementApi:

    def __init__(self, client_id: str, client_secret: str, instance: str, logger: Logger) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.instance = instance
        self.logger = logger

    def _get_token(self) -> str:
        try:
            return (
                make_request(
                    _request=requests.Request(
                        method="POST",
                        url="https://auth.atlassian.com/oauth/token",
                        json={
                            "grant_type": "client_credentials",
                            "client_id": self.client_id,
                            "client_secret": self.client_secret,
                            "audience": "api.atlassian.com",
                        },
                    ),
                    timeout=REQUESTS_TIMEOUT,
                )
                .json()
                .get("access_token", "")
            )
        except Exception:
            raise PluginException(
                cause=f"Failed to obtain access token for provided client id and client secret.",
                assistance="Please check your credentials and try again.",
            )

    def _get_cloud_id(self, authorization: str) -> str:
        resources = make_request(
            _request=requests.Request(
                method="GET",
                url="https://api.atlassian.com/oauth/token/accessible-resources",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {authorization}",
                },
            )
        ).json()

        for resource in resources:
            if resource.get("name", "") == self.instance:
                return resource.get("id", "")
        raise PluginException(
            cause=f"No accessible resource found for instance: {self.instance}.",
            assistance="Please provide a valid instance name.",
        )
