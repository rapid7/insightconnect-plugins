from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
import requests
import json
import base64
import mimetypes
from icon_freshservice.util.endpoints import (
    LIST_ALL_GROUPS_ENDPOINT,
    LIST_ALL_AGENTS_ENDPOINT,
    TICKET_ENDPOINT,
    TICKETS_ENDPOINT,
    TICKET_TASK_ENDPOINT,
    TICKET_TASKS_ENDPOINT,
)


class FreshServiceAPI:
    def __init__(self, url: str, api_key: str, logger):
        self.base_url = url
        self._api_key = api_key
        self._auth = requests.auth.HTTPBasicAuth(api_key, "X")
        self.headers = {"content-type": "application/json"}
        self.logger = logger

    def list_all_groups(self) -> dict:
        return self.make_json_request(path=LIST_ALL_GROUPS_ENDPOINT, headers=self.headers)

    def list_all_agents(self, parameters: dict) -> dict:
        return self.make_json_request(path=LIST_ALL_AGENTS_ENDPOINT, params=parameters, headers=self.headers)

    def list_tickets(self, parameters: dict) -> dict:
        return self.make_json_request(path=TICKETS_ENDPOINT, params=parameters, headers=self.headers)

    def create_ticket(self, json_data: dict) -> dict:
        return self.make_json_request(
            path=TICKETS_ENDPOINT,
            method="POST",
            json_data=json_data,
            headers=self.headers,
        )

    def update_ticket(self, ticket_id: int, json_data: dict = None, attachments: list = None) -> dict:
        response = {}
        if json_data:
            response = self.make_json_request(
                path=TICKET_ENDPOINT.format(ticket_id=ticket_id),
                method="PUT",
                json_data=json_data,
                headers=self.headers,
            )
        if attachments:
            for attachment in attachments:
                name = attachment.get("name")
                content = base64.b64decode(attachment.get("content"))
                mime_type = mimetypes.guess_type(name)[0]
                if not mime_type:
                    mime_type = "text/plain"
                response = self.make_json_request(
                    path=TICKET_ENDPOINT.format(ticket_id=ticket_id),
                    method="PUT",
                    files={"attachments[]": (name, content, mime_type)},
                )
        return response

    def delete_ticket(self, ticket_id: str) -> bool:
        self.make_request(
            path=TICKET_ENDPOINT.format(ticket_id=ticket_id),
            method="DELETE",
            headers=self.headers,
        )
        return True

    def create_ticket_task(self, ticket_id: str, json_data: dict) -> dict:
        return self.make_json_request(
            path=TICKET_TASKS_ENDPOINT.format(ticket_id=ticket_id),
            method="POST",
            json_data=json_data,
            headers=self.headers,
        )

    def update_ticket_task(self, ticket_id: str, task_id: str, json_data: dict) -> dict:
        return self.make_json_request(
            path=TICKET_TASK_ENDPOINT.format(ticket_id=ticket_id, task_id=task_id),
            method="PUT",
            json_data=json_data,
            headers=self.headers,
        )

    def delete_ticket_task(self, ticket_id: str, task_id: str) -> bool:
        self.make_request(
            path=TICKET_TASK_ENDPOINT.format(ticket_id=ticket_id, task_id=task_id),
            method="DELETE",
            headers=self.headers,
        )
        return True

    def make_request(  # noqa: C901
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        files: dict = None,
        headers: dict = None,
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method.upper(),
                url=f"{self.base_url}/api/v2{path}",
                auth=self._auth,
                json=json_data,
                params=params,
                data=data,
                files=files,
                headers=headers,
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Verify your input is correct and not malformed and try again. If the issue persists, "
                    "please contact support.",
                    data=response.text,
                )
            if 400 < response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(
                    cause="Server error occurred.",
                    assistance="Verify your plugin connection inputs are correct and not malformed and try "
                    "again. If the issue persists, please contact support.",
                    data=response.text,
                )
            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self,
        path: str,
        method: str = "GET",
        params: dict = None,
        json_data: dict = None,
        data: dict = None,
        files: dict = None,
        headers: dict = None,
    ) -> dict:
        try:
            response = self.make_request(
                path=path, method=method, params=params, json_data=json_data, data=data, files=files, headers=headers
            )
            return clean(response.json())
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
