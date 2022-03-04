import datetime
import hashlib
import hmac
import json
from base64 import b64decode, b64encode
from json import JSONDecodeError
from logging import Logger
from typing import List, Optional, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .endpoints import Endpoint
from .tools import Message, rate_limiting, clean_query_output


MAX_TRIES = 10


class AzureClient:
    def __init__(self):
        self.workspace_id = ""
        self.shared_key = ""
        self.auth_token = ""  # nosec

    def _connection(
        self,
        client_id: str,
        client_secret: str,
        tenant_id: str,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        resource: str,
    ) -> None:
        self._get_auth_token(tenant_id, client_id, client_secret, resource)
        self._get_shared_key(subscription_id, resource_group_name, workspace_name)
        self._get_workspace_id(subscription_id, resource_group_name, workspace_name)

    def _generate_signature(
        self, workspace_id: str, shared_key: str, date: str, json_body: List[dict], method: str, content_type: str
    ) -> str:
        try:
            x_headers = f"x-ms-date:{date}"
            content_length = len(json.dumps(json_body))
            string_to_hash = f"{method}\n{str(content_length)}\n{content_type}\n{x_headers}\n/api/logs"
            bytes_to_hash = bytes(string_to_hash, encoding="utf-8")
            decoded_key = b64decode(shared_key)
            encoded_hash = b64encode(hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()).decode()
            authorization = f"SharedKey {workspace_id}:{encoded_hash}"
            return authorization
        except TypeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

    def _get_workspace_id(self, subscription_id: str, resource_group_name: str, workspace_name: str) -> None:
        api_version = "2021-12-01-preview"
        get_workspace_id_url = Endpoint.GET_WORKSPACE_ID.format(
            subscription_id, resource_group_name, workspace_name, api_version
        )

        self.logger.info("Getting workspace ID...")
        response = self._call_api("GET", get_workspace_id_url, headers=self._get_auth_headers())
        self.workspace_id = response.get("properties").get("customerId")
        self.logger.info(f"Workspace ID: ****************{self.workspace_id[-5:]}")

    def _get_shared_key(self, subscription_id: str, resource_group_name: str, workspace_name: str) -> None:
        api_version = "2020-08-01"
        get_shared_key_url = Endpoint.GET_SHARED_KEY.format(
            subscription_id, resource_group_name, workspace_name, api_version
        )

        self.logger.info("Getting shared key...")
        response = self._call_api("POST", get_shared_key_url, headers=self._get_auth_headers())
        self.shared_key = response.get("primarySharedKey")
        self.logger.info(f"Shared Key: ****************{self.shared_key[-5:]}")

    def _get_auth_headers(self) -> dict:
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        return headers

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
        headers: dict = None,
        data: dict = None,
        json_data: Union[List[dict], dict] = None,
        params: dict = None,
    ) -> dict:
        try:
            response = requests.request(method, url, headers=headers, data=data, json=json_data, params=params)
            if response.status_code == 400:
                raise PluginException(cause=Message.BAD_REQUEST_MESSAGE, data=response.text)
            if response.status_code in (401, 403):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code == 409:
                raise PluginException(cause=Message.CONFLICTED_STATE_OF_OBJECT_MESSAGE, data=response.text)
            if response.status_code in (429, 503):
                raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
            if 200 <= response.status_code < 300:
                return response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        self.logger.info("Call to Microsoft Log Analytics API failed")
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)


class AzureLogAnalyticsClientAPI(AzureClient):
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

    def get_log_data(self, subscription_id: str, resource_group_name: str, workspace_name: str, query: str) -> dict:
        self._connection(
            self.client_id,
            self.client_secret,
            self.tenant_id,
            subscription_id,
            resource_group_name,
            workspace_name,
            Endpoint.RESOURCE_MANAGEMENT,
        )
        self._get_auth_token(self.tenant_id, self.client_id, self.client_secret, Endpoint.RESOURCE_LOG_API)
        api_version = "v1"
        get_log_data_url = Endpoint.GET_LOG_DATA.format(api_version, self.workspace_id)
        data = {"query": query}
        response = self._call_api("POST", get_log_data_url, json_data=data, headers=self._get_auth_headers())
        return clean_query_output(response)

    @rate_limiting(max_tries=MAX_TRIES)
    def send_log_data(
        self, subscription_id: str, resource_group_name: str, workspace_name: str, log_type: str, json_body: List[dict]
    ):
        self._connection(
            self.client_id,
            self.client_secret,
            self.tenant_id,
            subscription_id,
            resource_group_name,
            workspace_name,
            Endpoint.RESOURCE_MANAGEMENT,
        )
        api_version = "2016-04-01"
        send_log_data_url = Endpoint.SEND_LOG_DATA.format(self.workspace_id, api_version)

        method = "POST"
        content_type = "application/json"
        rfc1123date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

        signature = self._generate_signature(
            self.workspace_id, self.shared_key, rfc1123date, json_body, method, content_type
        )

        headers = {
            "Content-Type": content_type,
            "Authorization": signature,
            "Log-Type": log_type,
            "x-ms-date": rfc1123date,
        }

        response = requests.request("POST", send_log_data_url, headers=headers, json=json_body)
        if response.status_code == 400:
            raise PluginException(cause=Message.BAD_REQUEST_MESSAGE, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if response.status_code in (429, 503):
            raise PluginException(preset=PluginException.Preset.RATE_LIMIT)
        if response.status_code == 200:
            return
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def test_connection(self):
        self._get_auth_token(self.tenant_id, self.client_id, self.client_secret, Endpoint.RESOURCE_MANAGEMENT)
