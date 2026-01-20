import base64
import json
from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_connectwise.util.constants import SearchParameters, Ticket
from icon_connectwise.util.helpers import clean_dict, rename_keys
from icon_connectwise.util.endpoints import (
    BASE_URL,
    SERVICE_TICKETS_ENDPOINT,
    SERVICE_TICKET_ENDPOINT,
    SERVICE_NOTES_ENDPOINT,
    SERVICE_NOTE_ENDPOINT,
    COMPANIES_ENDPOINT,
)


class ConnectWiseAPI:
    def __init__(self, public_key: str, private_key: str, client_id: str, company: str, region: str, logger: Logger):
        self._public_key = public_key
        self._private_key = private_key
        self._client_id = client_id
        self._company = company
        self._region = region
        self._logger = logger
        self._base_url = BASE_URL.format(region=self._region)

    def _get_headers(self) -> dict:
        auth_header = f"{self._company}+{self._public_key}:{self._private_key}"
        encoded_auth_header = base64.b64encode(auth_header.encode()).decode()
        return {"Authorization": f"Basic {encoded_auth_header}", "clientId": self._client_id}

    def get_tickets(self, page_size: int = None, page: int = None, conditions: str = None) -> dict:
        return self.make_json_request(
            method="GET",
            url=f"{self._base_url}{SERVICE_TICKETS_ENDPOINT}",
            headers=self._get_headers(),
            params=clean_dict(
                {
                    SearchParameters.PAGE_SIZE: page_size,
                    SearchParameters.PAGE: page,
                    SearchParameters.CONDITIONS: conditions,
                }
            ),
        )

    def get_ticket_by_id(self, ticket_id: int) -> dict:
        return self.make_json_request(
            method="GET",
            url=f"{self._base_url}{SERVICE_TICKET_ENDPOINT.format(ticket_id=ticket_id)}",
            headers=self._get_headers(),
        )

    def get_ticket_notes(self, ticket_id: int, page_size: int = None, page: int = None, conditions: str = None) -> dict:
        return self.make_json_request(
            method="GET",
            url=f"{self._base_url}{SERVICE_NOTES_ENDPOINT.format(ticket_id=ticket_id)}",
            headers=self._get_headers(),
            params=clean_dict(
                {
                    SearchParameters.PAGE_SIZE: page_size,
                    SearchParameters.PAGE: page,
                    SearchParameters.CONDITIONS: conditions,
                }
            ),
        )

    def create_ticket(self, ticket_parameters: dict) -> dict:
        return self.make_json_request(
            method="POST",
            url=f"{self._base_url}{SERVICE_TICKETS_ENDPOINT}",
            headers=self._get_headers(),
            json_data=clean_dict(ticket_parameters),
        )

    def update_ticket(self, ticket_id: int, ticket_parameters: dict) -> dict:
        clean_ticket_parameters = clean_dict(ticket_parameters)
        required_parameters = {
            key: clean_ticket_parameters.get(key)
            for key in [Ticket.STATUS, Ticket.BOARD, Ticket.IMPACT, Ticket.PRIORITY, Ticket.TEAM]
        }
        not_provided = {key: value for key, value in required_parameters.items() if not value}
        if not_provided:
            raise PluginException(
                cause="Not enough input parameters were provided.",
                assistance=f"Please provide `{', '.join(list(not_provided.keys()))}` and try again. If the issue persists, please contact support.",
            )
        return self.make_json_request(
            method="PUT",
            url=f"{self._base_url}{SERVICE_TICKET_ENDPOINT.format(ticket_id=ticket_id)}",
            headers=self._get_headers(),
            json_data=clean_dict(clean_ticket_parameters),
        )

    def delete_ticket(self, ticket_id: int) -> bool:
        return (
            self.make_request(
                method="DELETE",
                url=f"{self._base_url}{SERVICE_TICKET_ENDPOINT.format(ticket_id=ticket_id)}",
                headers=self._get_headers(),
            ).status_code
            == 204
        )

    def create_ticket_note(self, ticket_id: int, note_parameters: dict) -> dict:
        return self.make_json_request(
            method="POST",
            url=f"{self._base_url}{SERVICE_NOTES_ENDPOINT.format(ticket_id=ticket_id)}",
            headers=self._get_headers(),
            json_data=note_parameters,
        )

    def update_ticket_note(self, ticket_id: int, note_id: int, note_parameters: dict) -> dict:
        if not note_parameters:
            raise PluginException(
                cause="Not enough input parameters were provided.",
                assistance="Please provide at least one input parameter except Ticket ID and Note ID and try again. If the issue persists, please contact support.",
            )
        return self.make_json_request(
            method="PUT",
            url=f"{self._base_url}{SERVICE_NOTE_ENDPOINT.format(ticket_id=ticket_id, note_id=note_id)}",
            headers=self._get_headers(),
            json_data=note_parameters,
        )

    def delete_ticket_note(self, ticket_id: int, note_id: int) -> bool:
        return (
            self.make_request(
                method="DELETE",
                url=f"{self._base_url}{SERVICE_NOTE_ENDPOINT.format(ticket_id=ticket_id, note_id=note_id)}",
                headers=self._get_headers(),
            ).status_code
            == 204
        )

    def get_company(self, company_id: int) -> dict:
        return self.make_json_request(
            method="GET",
            url=f"{self._base_url}{COMPANIES_ENDPOINT.format(company_id=company_id)}",
            headers=self._get_headers(),
        )

    def make_request(
        self, method: str, url: str, headers: dict, params: dict = None, data: dict = None, json_data: dict = None
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=url, headers=headers, params=params, data=data, json=json_data
            )

            if response.status_code == 400:
                raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
            if response.status_code == 403:
                raise PluginException(
                    cause="Operation is not allowed.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=response.text,
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=response.text,
                )
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def make_json_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
        json_data: dict = None,
    ) -> dict:
        try:
            response = self.make_request(
                method=method, url=url, params=params, data=data, headers=headers, json_data=json_data
            )
            return rename_keys(response.json(), "_info", "info")
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
