import base64
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from logging import Logger
import requests
from requests.auth import HTTPBasicAuth, AuthBase
from typing import Any, Union

from komand_jira.util.constants import (
    REQUESTS_TIMEOUT,
    DEFAULT_JIRA_API_VERSION,
    OAUTH2_TOKEN_URL,
    OAUTH2_ACCESSIBLE_RESOURCES_URL,
    ATLASSIAN_API_DOMAIN,
)
from komand_jira.util.util import load_text_as_adf


class JiraApi:
    def __init__(
        self,
        base_url: str,
        authorization: Union[HTTPBasicAuth, dict[str, str]],
        logger: Logger,
        api_version: str = DEFAULT_JIRA_API_VERSION,
    ) -> None:
        self.base_url = base_url
        self.api_version = api_version
        self.authorization = authorization
        self.logger = logger
        self._update_base_url_for_oauth2()

    def get_issue(self, issue_id: str) -> dict[str, Any]:
        return self._call_api("GET", f"issue/{issue_id}")

    def get_user(self, username: str) -> list[dict[str, Any]]:
        return self._call_api("GET", "user/search", params={"query": username, "maxResults": 1})

    def assign_issue(self, issue_id: str, username: str) -> bool:
        # Get user accountId by username
        user = self.get_user(username)

        # In case no user is found, raise
        if not user:
            raise PluginException(
                cause=f"No user found with username: {username}.",
                assistance="Please provide a valid username.",
            )

        # In case multiple users are found, raise
        if len(user) > 1:
            raise PluginException(
                cause=f"Multiple users found with username: {username}.",
                assistance="Please provide a more specific username.",
            )
        self._call_api(
            "PUT",
            f"issue/{issue_id}/assignee",
            payload={"accountId": user[0].get("accountId", "")},
            return_json=False,
        )
        return True

    def add_attachment(self, issue_id: str, filename: str, file_bytes: str) -> int:
        try:
            data = base64.b64decode(file_bytes)
        except Exception as error:
            raise PluginException(
                cause="Unable to decode attachment bytes.",
                assistance=f"Please provide a valid attachment bytes. Error: {str(error)}",
            )
        return self._call_api(
            "POST",
            f"/issue/{issue_id}/attachments",
            files={"file": (filename, data, "application/octet-stream")},
            headers={"content-type": None, "X-Atlassian-Token": "nocheck"},
        )[0].get("id")

    def get_attachment_content(self, attachment_id: str) -> str:
        return self._call_api("GET", f"attachment/content/{attachment_id}", return_json=False)

    def add_comment_to_issue(self, issue_id: int, comment: str) -> dict[str, Any]:
        return self._call_api(
            "POST",
            f"issue/{issue_id}/comment",
            payload={"body": load_text_as_adf(comment)},
        )

    def get_all_issue_types(self) -> dict[str, Any]:
        return self._call_api("GET", "issuetype")

    def get_project(self, project_name: str) -> dict[str, Any]:
        return self._call_api("GET", "project/search", params={"query": project_name})

    def create_issue(self, issue_fields: dict[str, Any]) -> dict[str, Any]:
        return self._call_api("POST", "issue", payload={"fields": issue_fields})

    def edit_issue(self, issue_id: str, issue_fields: dict[str, Any], notify: bool) -> None:
        self._call_api(
            "PUT",
            f"issue/{issue_id}",
            params={"notifyUsers": notify},
            payload={"fields": issue_fields},
            return_json=False,
        )

    def get_issue_fields(self) -> dict[str, Any]:
        return self._call_api("GET", "field")

    def search_issues(self, jql: str, max_results: int) -> dict[str, Any]:
        return self._call_api("GET", "search/jql", params={"jql": jql, "maxResults": max_results, "fields": "*all"})

    def get_transitions(self, issue_id: str) -> dict[str, Any]:
        return self._call_api("GET", f"issue/{issue_id}/transitions")

    def transition_issue(
        self, issue_id: str, transition_name: str, comment: str, fields: dict[str, Any]
    ) -> dict[str, Any]:
        # Get the transition ID from the name if necessary
        transition_id = None
        if not transition_name.isdigit():
            for transition in self.get_transitions(issue_id).get("transitions", []):
                if transition.get("name", "").lower() == transition_name.lower():
                    transition_id = transition.get("id", "")
                    break
            if not transition_id:
                raise PluginException(
                    cause=f"No transition found with name: {transition_name}.",
                    assistance="Please provide a valid transition name or ID.",
                )

        # Initialize request payload data
        payload = {"transition": {"id": transition_id or transition_name}}

        # If a comment is provided, add it to the payload
        if comment:
            payload["update"] = {"comment": [{"add": {"body": load_text_as_adf(comment)}}]}

        # If fields are provided, add them to the payload
        if fields:
            payload["fields"] = fields
        return self._call_api("POST", f"issue/{issue_id}/transitions", payload=payload, return_json=False)

    def add_user(self, username: str, email: str, password: str, products: list[str], notify: bool) -> bool:
        try:
            self._call_api(
                "POST",
                "user",
                payload={
                    "displayName": username,
                    "emailAddress": email,
                    "password": password,
                    "notification": notify,
                    "name": username,
                    "products": products,
                },
            )
            return True
        except Exception as error:
            self.logger.error(error)
            return False

    def delete_user(self, account_id: str) -> bool:
        try:
            self._call_api("DELETE", "user", params={"accountId": account_id})
            return True
        except Exception as error:
            self.logger.error(error)
            return False

    def find_users(self, query: str, max_results: int = 10) -> list[dict[str, Any]]:
        return self._call_api("GET", "user/search", params={"query": query, "maxResults": max_results})

    def test_connection(self) -> Union[list[dict[str, Any]], None]:
        if self._is_oauth2_credentials():
            return self._get_oauth2_accessible_resources()
        return self._call_api("GET", self.base_url, return_json=False, is_api_path=False)

    @staticmethod
    def _get_access_token(client_id: str, client_secret: str) -> str:
        with requests.Session() as session:
            with session.request(
                "POST",
                OAUTH2_TOKEN_URL,
                data={
                    "grant_type": "client_credentials",
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
                timeout=REQUESTS_TIMEOUT,
            ) as response:
                if 200 <= response.status_code < 400:
                    return response.json().get("access_token", "")
                raise PluginException(
                    cause="Failed to obtain access token.",
                    assistance=f"Please check your client ID and client secret. Response: {response.text}",
                )

    def _get_oauth2_accessible_resources(self) -> list[dict[str, Any]]:
        return self._call_api("GET", OAUTH2_ACCESSIBLE_RESOURCES_URL, is_api_path=False)

    def _update_base_url_for_oauth2(self) -> None:
        # Only process OAuth2 credentials with generic Atlassian API endpoint
        if not self._is_oauth2_credentials():
            return

        # Only update base URL if it matches the generic pattern and doesn't already contain a cloud ID
        if not self.base_url.startswith(f"https://{ATLASSIAN_API_DOMAIN}") or "/ex/jira/" in self.base_url:
            return

        # Fetch cloud ID from accessible resources
        self.logger.info("Noticed OAuth2 credentials with generic base URL. Attempting to determine Jira cloud ID...")
        resources = self._get_oauth2_accessible_resources()
        if not resources or not (cloud_id := resources[0].get("id")):
            raise PluginException(
                cause="Unable to determine Jira cloud ID for OAuth2.",
                assistance="Verify your client credentials have access to at least one Jira site.",
            )

        self.base_url = f"https://{ATLASSIAN_API_DOMAIN}/ex/jira/{cloud_id}"
        self.logger.info(f"Updated base URL to: {self.base_url}")

    def _is_oauth2_credentials(self) -> bool:
        return isinstance(self.authorization, dict) and all(
            key in self.authorization for key in ("client_id", "client_secret")
        )

    def _get_authorization(self) -> tuple[Union[HTTPBasicAuth, None], dict[str, str]]:
        # Set default headers
        headers = {"Accept": "application/json"}

        # Basic Auth
        if isinstance(self.authorization, HTTPBasicAuth):
            self.logger.info("Authentication type: Basic Auth.")
            return self.authorization, headers

        # OAuth2
        if self._is_oauth2_credentials():
            self.logger.info("Authentication type: OAuth2 Client Credentials.")
            access_token = self._get_access_token(**self.authorization)
            headers["Authorization"] = f"Bearer {access_token}"
            return None, headers

        # PAT (Personal Access Token)
        self.logger.info("Authentication type: Personal Access Token (PAT).")
        headers.update(self.authorization)
        return None, headers

    def _call_api(  # noqa: MC0001
        self,
        method: str,
        path: str,
        files: dict[str, Any] = None,
        headers: dict[str, Any] = None,
        params: dict[str, Any] = None,
        payload: dict[str, Any] = None,
        timeout: int = REQUESTS_TIMEOUT,
        return_json: bool = True,
        is_api_path: bool = True,
    ) -> Union[list[dict[str, Any]], dict[str, Any], str]:
        try:
            # Prepare URL
            url = f"{self.base_url}/rest/api/{self.api_version}/{path}" if is_api_path else path

            # Get authorization and headers
            authorization, auth_headers = self._get_authorization()

            # Update headers with any additional headers provided in the method call
            if headers:
                auth_headers.update(headers)

            # Use context manager chaining for both session and response to ensure proper cleanup
            with requests.Session() as session:
                with session.request(
                    method.upper(),
                    url,
                    params=params,
                    json=payload,
                    headers=auth_headers,
                    files=files,
                    auth=authorization,
                    timeout=timeout,
                ) as response:
                    if response.status_code == 401:
                        raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
                    if response.status_code == 403:
                        raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
                    if response.status_code == 404:
                        raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
                    if 400 <= response.status_code < 500:
                        raise PluginException(
                            preset=PluginException.Preset.UNKNOWN,
                            data=response.text,
                        )
                    if response.status_code >= 500:
                        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
                    if 200 <= response.status_code < 300:
                        if return_json:
                            return response.json()
                        return response.content
                    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
