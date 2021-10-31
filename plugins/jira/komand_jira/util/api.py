import base64
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from jira.resources import User


class JiraApi:
    def __init__(self, jira_client, is_cloud, logger):
        self.jira_client = jira_client
        self.is_cloud = is_cloud
        self.logger = logger
        self.session = jira_client._session
        self.base_url = jira_client._options["server"]

    def delete_user(self, account_id):
        url = f"{self.base_url}/rest/api/latest/user/?accountId={account_id}"
        r = self.session.delete(url)

        if 200 <= r.status_code <= 299:
            return True
        else:
            self.logger.error(r.status_code)
            return False

    def find_users(self, query, max_results=10):
        # pylint: disable=protected-access
        return self.jira_client._fetch_pages(User, None, "user/search", 0, max_results, {"query": query})

    def add_attachment(self, issue, filename, file_bytes):
        try:
            data = base64.b64decode(file_bytes)
        except Exception as e:
            raise PluginException(
                cause="Unable to decode attachment bytes.",
                assistance=f"Please provide a valid attachment bytes. Error: {str(e)}",
            )

        return self.call_api(
            "POST",
            f"/rest/api/latest/issue/{issue}/attachments",
            files={"file": (filename, data, "application/octet-stream")},
            headers={"content-type": None, "X-Atlassian-Token": "nocheck"},
        )[0].get("id")

    def call_api(
        self,
        method: str,
        path: str,
        files: dict = None,
        headers: dict = None,
        params: dict = None,
        payload: dict = None,
    ) -> dict:
        try:
            response = self.session.request(
                method.upper(),
                self.base_url + path,
                params=params,
                json=payload,
                headers=headers,
                files=files,
            )

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
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
