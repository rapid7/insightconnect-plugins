from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
import requests
import json
from logging import Logger
from icon_happyfox.util.endpoints import (
    CREATE_INLINE_ATTACHMENT_ENDPOINT,
    DELETE_TICKET_ENDPOINT,
    TICKETS_ENDPOINT,
    TICKET_CUSTOM_FIELDS_ENDPOINT,
    USER_CUSTOM_FIELDS_ENDPOINT,
)
from icon_happyfox.util.constants import Cause, Assistance


class HappyFoxAPI:
    def __init__(self, url: str, api_key: str, auth_code: str, logger: Logger):
        self.base_url = url
        self._api_key = api_key
        self._auth = requests.auth.HTTPBasicAuth(api_key, auth_code)
        self.headers = {"content-type": "application/json"}
        self.logger = logger

    def create_ticket(self, json_data: dict) -> dict:
        return self.make_json_request(
            path=TICKETS_ENDPOINT,
            method="POST",
            json_data=json_data,
            headers=self.headers,
        )

    def delete_ticket(self, ticket_id: str, json_data: dict) -> bool:
        self.make_request(
            path=DELETE_TICKET_ENDPOINT.format(ticket_id=ticket_id),
            method="POST",
            json_data=json_data,
            headers=self.headers,
        )
        return True

    def list_tickets(self, parameters: dict) -> dict:
        return self.make_json_request(
            path=TICKETS_ENDPOINT,
            method="GET",
            params=parameters,
            headers=self.headers,
        )

    def create_inline_attachment(self, attachment: list) -> dict:
        return self.make_json_request(
            path=CREATE_INLINE_ATTACHMENT_ENDPOINT,
            method="POST",
            files=attachment,
        )

    def create_ticket_with_attachments(self, json_data: dict, attachments: list) -> dict:
        return self.make_json_request(
            path=TICKETS_ENDPOINT,
            method="POST",
            data=json_data,
            files=attachments,
        )

    def get_ticket_custom_field(self):
        return self.make_json_request(path=TICKET_CUSTOM_FIELDS_ENDPOINT, method="GET", headers=self.headers)

    def get_user_custom_field(self):
        return self.make_json_request(path=USER_CUSTOM_FIELDS_ENDPOINT, method="GET", headers=self.headers)

    def get_available_custom_fields(self, provided_category: int) -> list:
        available_custom_fields = []
        ticket_custom_fields = self.get_ticket_custom_field()
        contact_custom_fields = self.get_user_custom_field()
        for ticket_custom_field in ticket_custom_fields:
            categories = ticket_custom_field.get("categories")
            for category in categories:
                if category.get("category") == provided_category:
                    available_custom_fields.append(
                        {"name": ticket_custom_field.get("name"), "id": f"t-cf-{ticket_custom_field.get('id')}"}
                    )
        for contact_custom_field in contact_custom_fields:
            available_custom_fields.append(
                {"name": contact_custom_field.get("name"), "id": f"c-cf-{contact_custom_field.get('id')}"}
            )
        return available_custom_fields

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
                url=f"{self.base_url}/api/1.1/json{path}",
                auth=self._auth,
                json=json_data,
                params=params,
                data=data,
                files=files,
                headers=headers,
            )
            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code in [401, 403]:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(
                    cause=Cause.NOT_FOUND,
                    assistance=Assistance.NOT_FOUND,
                    data=response.text,
                )
            if 400 < response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(
                    cause=Cause.SERVER_ERROR,
                    assistance=Assistance.SERVER_ERROR,
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
