import base64
from enum import Enum
import json
from logging import Logger
from typing import Optional
import xmltodict
import requests
from requests.auth import HTTPBasicAuth, AuthBase

from insightconnect_plugin_runtime.exceptions import PluginException


class BearerAuth(AuthBase):
    """
    Authentication class for Bearer auth
    """

    def __init__(self, access_token: str):
        self.access_token = access_token

    def __call__(self, request: requests.Request) -> requests.Request:
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        return request


class AuthenticationType(Enum):
    basic = "basic"
    oauth = "oauth"


class RequestHelper(object):
    def __init__(
        self,
        username: str,
        password: str,
        client_id: Optional[str],
        client_secret: Optional[str],
        auth_type: AuthenticationType,
        base_url: str,
        logger: Logger,
    ):
        """
        Creates a new instance of RequestHelper
        :param username: Username for ServiceNow
        :param password: Password for ServiceNow
        :param client_id: Client ID for OAuth app
        :param client_secret: Client Secret for OAuth app
        :param auth_type: Authentication type to use for requests
        :param base_url: Base URL for API
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: RequestHelper object
        """
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_type = auth_type
        self.base_url = base_url
        self.logger = logger

    def make_request(  # noqa: C901
        self, endpoint, method, payload=None, params=None, data=None, content_type="application/json"
    ):
        try:
            request_method = getattr(requests, method.lower())

            headers = {"Content-Type": content_type, "Accept": "application/json"}

            if not params:
                params = {}

            if self.auth_type == AuthenticationType.basic:
                auth_mechanism = HTTPBasicAuth(username=self.username, password=self.password)
            else:
                oauth_token = self._get_oauth_token()
                auth_mechanism = BearerAuth(access_token=oauth_token)

            response = request_method(
                url=endpoint, headers=headers, params=params, json=payload, data=data, auth=auth_mechanism, verify=False
            )
        except requests.RequestException as error:
            self.logger.error(error)
            raise

        if response.status_code in range(200, 299):
            content_type = response.headers.get("Content-Type", "")
            self.logger.info(f"Response received in content-type {content_type}")

            if response.status_code == 204:
                resource = None
            else:
                if "application/json" in content_type:
                    print("JSON")
                    try:
                        resource = response.json()
                    except json.decoder.JSONDecodeError:
                        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
                elif "xml" in content_type:
                    print("XML")
                    resource = xmltodict.parse(response.content).get("response", {})
                else:
                    resource = response.content

            return {"resource": resource, "status": response.status_code, "content-type": content_type}

        try:
            error = response.json()
        except json.decoder.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        raise PluginException(
            cause="Error in API request to ServiceNow. ",
            assistance=f"Status code: {response.status_code}, Error: {error}",
        )

    @staticmethod
    def get_attachment(connection, sys_id):
        response = connection.request.make_request(f"{connection.attachment_url}/{sys_id}/file", "get")
        resource = response.get("resource")

        if not resource:
            return ""

        if isinstance(resource, bytes):
            result = resource
        elif isinstance(resource, dict):
            try:
                result = json.dumps(resource).encode("utf-8")
            except TypeError:
                raise PluginException(PluginException.Preset.INVALID_JSON, data=resource)
        else:
            raise PluginException(PluginException.Preset.UNKNOWN, data=resource)

        return str(base64.b64encode(result), "utf-8")

    def _get_oauth_token(self) -> str:
        response = requests.post(
            url=f"{self.base_url}oauth_token.do",
            data={
                "grant_type": "password",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "username": self.username,
                "password": self.password,
            },
            timeout=30,
        )

        if response.status_code != 200:
            error_message = "unknown"
            if response.status_code == 401:
                error_message = response.json().get("error_description", "unauthorized")
            raise PluginException(
                cause=f"Error while trying to retrieve new OAuth token: {error_message}",
                assistance="Ensure credentials and ServiceNow endpoint are correct.",
            )
        try:
            access_token = response.json()["access_token"]
        except KeyError:
            raise PluginException(
                cause="Access token was not present in OAuth token response!", assistance="API may have changed"
            )

        return access_token
