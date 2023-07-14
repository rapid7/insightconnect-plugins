import json
from typing import Optional, Union

import requests
from requests.auth import HTTPBasicAuth
from insightconnect_plugin_runtime.exceptions import PluginException

# Here is the docs for the next dev that comes through here
# https://github.com/TheHive-Project/TheHive4py/blob/master/thehive4py/api.py
# Do not trust the official docs on the hive website, this is what worked for me ^


class HiveAPI:
    def __init__(self, url: str, username: str, password: str, api_key: str, proxies, cert):
        self.url = url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.proxy = proxies
        self.verify = cert

    # Get Case
    def get_case(self, case_id: str):
        return self._call_api("GET", f"/api/case/{case_id}")

    # Get Cases
    def get_cases(self):
        return self._call_api("POST", "/api/case/_search", params={"range": "all", "sort": []}, data={})

    # Create Case
    def create_case(self, case):
        return self._call_api("POST", "/api/case", data=case)

    # Create Observable In Case
    # WIP
    def create_observable_in_case(self, case_id, observable):
        return self._call_api("POST", f"/api/case/{case_id}/artifact", data=observable)

    # Create Task in Case
    def create_task_in_case(self, case_id, task):
        return self._call_api("POST", f"/api/case/{case_id}/task", data=task)

    # Close Case
    def close_case(self, case_id, force):
        req_url = f"/api/case/{case_id}"
        if force:
            req_url += "/force"
        return self._call_api("DELETE", req_url)

    # Get Current User
    def get_current_user(self):
        return self._call_api("GET", "/api/user/current")

    # Get User By ID
    def get_user_by_id(self, user_id):
        return self._call_api("GET", f"/api/user/{user_id}")

    def _call_api(
        self, method: str, path: str, params: Optional[dict] = None, data: Optional = None, json_data: Optional = None
    ) -> Union[dict, None]:

        # Build out the headers
        headers = {"X-Organisation": "myOrg", "Content-Type": "application/json"}

        # Handle the authentication method
        auth = None

        # For API key auth, we need to add it into headers, not via request.auth()
        if self.api_key:
            headers.update({"Authorization": f"Bearer {self.api_key}"})

        if self.username and self.password:
            auth = HTTPBasicAuth(self.username, self.password)

        # Jsonify the data - Not sure if this is needed but it can't hurt
        # Doing this because it throws back 400 without detail if the JSON encoding is
        # not perfect
        data = json.dumps(data, sort_keys=True, indent=4, cls=json.JSONEncoder)

        response = requests.request(
            method, self.url + path, params=params, data=data, json=json_data, headers=headers, auth=auth
        )

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response)
        if response.status_code == 204:
            return None
        if response.status_code in range(200, 299):
            return response.json()

        # Anything which isn't caught by now, present the unknown preset and show the response.
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)
