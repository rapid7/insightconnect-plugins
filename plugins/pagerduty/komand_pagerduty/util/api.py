from insightconnect_plugin_runtime.helper import clean
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from logging import Logger
import requests
import json


class PagerDutyAPI:
    def __init__(self, api_key: str, logger: Logger):
        self.headers = {
            "Authorization": f"Token token={api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.session = requests.session()
        self.logger = logger

    def get_on_calls(self, schedule_id: str = None) -> dict:
        return self.send_request("GET", f"/schedules/{schedule_id}/")

    def resolve_event(self, email: str, incident_id: str) -> dict:
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        data = {"incident": {"type": "incident", "status": "resolved"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", headers=headers, data=json.dumps(data)
        )

    def acknowledge_event(self, email: str, incident_id: str) -> dict:
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        data = {"incident": {"type": "incident", "status": "acknowledged"}}
        return self.send_request(
            method="PUT", path=f"/incidents/{incident_id}/", headers=headers, data=json.dumps(data)
        )

    def trigger_event(
        self,
        email: str,
        title: str,
        service: dict,
        dict_of_optional_fields: dict,
    ) -> dict:
        headers = {"From": f"{email}"}
        headers.update(self.headers)

        payload = {"incident": {"type": "incident", "title": title, "service": service}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["incident"][key] = value

        return self.send_request(method="POST", path="/incidents/", headers=headers, payload=payload)

    def create_user(
        self,
        from_email: str,
        new_users_email: str,
        name: str,
        dict_of_optional_fields: dict,
    ) -> dict:
        headers = {"From": f"{from_email}"}
        headers.update(self.headers)

        payload = {"user": {"name": name, "email": new_users_email}}

        for key, value in dict_of_optional_fields.items():
            if value:
                payload["user"][key] = value

        return self.send_request(method="POST", path="/users/", headers=headers, payload=payload)

    def delete_user_by_id(self, email: str, user_id: str) -> dict:
        headers = {"From": f"{email}"}
        headers.update(self.headers)
        return self.send_request(method="DELETE", path=f"/users/{user_id}/", headers=headers)

    def get_user_by_id(self, user_id: str) -> dict:
        return self.send_request(method="GET", path=f"/users/{user_id}/")

    def list_users(self) -> dict:
        return self.send_request(method="GET", path="/users/")

    def send_request(
        self, method: str, path: str, params: dict = None, payload: dict = None, headers: dict = None, data: dict = None
    ) -> dict:
        if not headers:
            headers = self.headers

        try:
            response = self.session.request(
                method.upper(),
                "https://api.pagerduty.com" + path,
                params=params,
                json=payload,
                headers=headers,
                data=data,
            )

            if method.upper() == "DELETE" and response.status_code == 204:
                return True
            if 200 <= response.status_code < 300:
                return clean(json.loads(response.content))

            self._check_status_code(response)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
    
    def _check_status_code(self, response:dict):

        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
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
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
