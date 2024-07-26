from logging import Logger
from typing import Union

import requests
from insightconnect_plugin_runtime.helper import request_error_handling, extract_json, response_handler
from insightconnect_plugin_runtime.exceptions import ResponseExceptionData, PluginException

from icon_freshdesk.util.helpers import clean_dict, create_attachments_form
from icon_freshdesk.util.endpoints import FITLER_TICKETS_ENDPOINT, TICKETS_ENDPOINT, TICKET_ENDPOINT, TICKET_FIELDS_ENDPOINT


class FreshDeskAPI:
    def __init__(self, api_key: str, domain: str, logger: Logger):
        self._auth = requests.auth.HTTPBasicAuth(api_key, "x")
        self._domain = domain
        self._headers = {"Content-Type": "application/json"}
        self._logger = logger

    def create_ticket(self, ticket_parameters: dict) -> dict:
        self._logger.info("Creating a ticket...")
        response_json = self.make_json_request(
            method="POST",
            url=TICKETS_ENDPOINT.format(domain=self._domain),
            json_data=ticket_parameters,
        )
        self._logger.info("Ticket created successfully.")
        return response_json

    def update_ticket(self, ticket_id: int, ticket_parameters: dict = None, attachments: list = None) -> dict:
        response_json = {}
        if ticket_parameters:
            self._logger.info(f"Updating a ticket (id={ticket_id})...")
            response_json = self.make_json_request(
                method="PUT",
                url=TICKET_ENDPOINT.format(domain=self._domain, ticket_id=ticket_id),
                json_data=ticket_parameters,
            )
            self._logger.info(f"Ticket (id={ticket_id}) updated successfully.")
        if attachments:
            self._logger.info(f"Updating a ticket (id={ticket_id}) attachments...")
            ticket_form_data = create_attachments_form(attachments)
            response_json = self.make_json_request(
                method="PUT",
                url=TICKET_ENDPOINT.format(domain=self._domain, ticket_id=ticket_id),
                files=ticket_form_data,
            )
            self._logger.info(f"Ticket (id={ticket_id}) attachments updated successfully.")
        return response_json

    def get_ticket_by_id(self, ticket_id: int, include: str = None) -> dict:
        self._logger.info(f"Getting a ticket by id (id={ticket_id})...")
        response_json = self.make_json_request(
            method="GET",
            url=TICKET_ENDPOINT.format(domain=self._domain, ticket_id=ticket_id),
            headers=self._headers,
            params={"include": include},
        )
        return response_json

    def get_tickets(
        self,
        predefined_filter: str = None,
        include: str = None,
        order_by: str = None,
        order_type: str = None,
        per_page: int = None,
        page: int = None,
        filter_by: dict = None,
    ) -> dict:
        self._logger.info("Getting a list of tickets...")
        return self.make_json_request(
            method="GET",
            url=TICKETS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            params=clean_dict(
                {
                    "filter": predefined_filter,
                    "include": include,
                    "order_by": order_by,
                    "order_type": order_type,
                    "per_page": per_page,
                    "page": page,
                    **filter_by,
                }
            ),
        )

    def filter_tickets(self, query: str = None, page: int = None) -> dict:
        return self.make_json_request(
            method="GET",
            url=FITLER_TICKETS_ENDPOINT.format(domain=self._domain),
            headers=self._headers,
            params=clean_dict({"query": query, "page": page})
        )

    def get_ticket_fields(self) -> Union[list, dict]:
        return self.make_json_request(
            method="GET", url=TICKET_FIELDS_ENDPOINT.format(domain=self._domain), headers=self._headers.get("json")
        )

    def make_request(
        self, method: str, url: str, headers: dict, params: dict = None, json_data: dict = None, files: list = None
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=self._auth,
                headers=headers,
                params=params,
                json=clean_dict(json_data),
                files=files,
            )
            response_handler(response, data_location=ResponseExceptionData.RESPONSE_TEXT)
        except requests.exceptions.Timeout as exception:
            raise PluginException(
                preset=PluginException.Preset.TIMEOUT, data=str(exception)
            )
        except requests.exceptions.ConnectionError as exception:
            raise PluginException(
                preset=PluginException.Preset.CONNECTION_ERROR, data=str(exception)
            )
        except requests.exceptions.TooManyRedirects as exception:
            raise PluginException(
                preset=PluginException.Preset.REDIRECT_ERROR, data=str(exception)
            )
        return response

    def make_json_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        json_data: dict = None,
        files: list = None,
    ) -> dict:
        response = self.make_request(
            method=method, url=url, params=params, json_data=json_data, headers=headers, files=files
        )
        return extract_json(response)
