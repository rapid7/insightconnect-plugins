import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import List, Tuple, Union


class GitLabAPI:
    def __init__(self, base_url: str, token: str, verify: bool):
        super().__init__()
        self.base_url = base_url
        self.token = token
        self.verify = verify

    def block_user(self, user_id: int):
        return self._call_api(method="POST", path=f"/users/{str(user_id)}/block")

    def create_issue(self, project_id: int, issue_params: List[Tuple[str, Union[str, int]]]):
        return self._call_api(method="POST", path=f"/projects/{str(project_id)}/issues", params=issue_params)

    def delete_ssh(self, user_id: int, key_id: int):
        return self._call_api(method="DELETE", path=f"/users/{str(user_id)}/keys/{str(key_id)}")

    def delete_user(self, user_id: int):
        return self._call_api(method="DELETE", path=f"/users/{str(user_id)}")

    def get_user(self, user_id: int):
        return self._call_api(method="GET", path=f"/users/{str(user_id)}")

    def list_ssh(self, user_id: int):
        return self._call_api(method="GET", path=f"/users/{str(user_id)}/keys")

    def unblock_user(self, user_id: int):
        return self._call_api(method="POST", path=f"/users/{str(user_id)}/unblock")

    def get_issues(self, issue_params: List[Tuple[str, Union[str, int]]]):
        return self._call_api(method="GET", path=f"/issues", params=issue_params)

    def _call_api(self, method: str, path: str, params=None):
        headers = {"PRIVATE-TOKEN": self.token}

        response = requests.request(method, self.base_url + path, headers=headers, params=params, verify=self.verify)

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.json())
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.json())
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.json())
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.json())
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.json())
        if 200 <= response.status_code < 300:
            return response.json()
