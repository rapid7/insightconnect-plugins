import json
from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_manage_engine_service_desk.util import helpers
from icon_manage_engine_service_desk.util.constants import Request
from icon_manage_engine_service_desk.util.endpoints import (
    REQUESTS_ENDPOINT,
    REQUEST_ENDPOINT,
    DELETE_REQUEST_ENDPOINT,
    CLOSE_REQUEST_ENDPOINT,
    ASSIGN_REQUEST_ENDPOINT,
    PICKUP_REQUEST_ENDPOINT,
    REQUEST_RESOLUTIONS_ENDPOINT,
    REQUEST_NOTES_ENDPOINT,
    REQUEST_NOTE_ENDPOINT,
)


class ManageEngineServiceDeskAPI:
    def __init__(self, api_key: str, sdp_base_url: str, logger: Logger):
        self._api_key = api_key
        self._sdp_base_url = sdp_base_url if not sdp_base_url.endswith("/") else sdp_base_url[:-1]
        self._logger = logger

    def _get_headers(self) -> dict:
        return {"authtoken": f"{self._api_key}"}

    def get_requests_list(
        self,
        start_index: int = None,
        page_size: str = None,
        search_fields: dict = None,
        sort_order: str = None,
        sort_field: str = None,
    ) -> dict:
        self._logger.info("Getting list of requests...")
        list_parameters = helpers.clean_dict(
            {
                "start_index": start_index,
                "row_count": page_size,
                "search_fields": search_fields,
                "sort_order": sort_order,
                "sort_field": sort_field,
            }
        )
        return self.make_json_request(
            method="GET",
            url=REQUESTS_ENDPOINT.format(sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            params=helpers.prepare_input_data({"list_info": list_parameters}),
        )

    def get_request(self, request_id: int) -> dict:
        self._logger.info(f"Getting a request with {request_id} id...")
        return self.make_json_request(
            method="GET",
            url=REQUEST_ENDPOINT.format(sdp_base_url=self._sdp_base_url, request_id=request_id),
            headers=self._get_headers(),
        )

    def add_request(self, request_parameters: dict) -> dict:
        self._logger.info("Adding a request...")
        cleaned_request_parameters = helpers.clean_dict(request_parameters)
        if not cleaned_request_parameters.get(Request.REQUESTER):
            raise PluginException(
                cause="Requester parameter not provided.",
                assistance="Please provide a Requester parameter and try again. If the issue persists, please contact support.",
            )
        return self.make_json_request(
            method="POST",
            url=REQUESTS_ENDPOINT.format(sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": cleaned_request_parameters}),
        )

    def edit_request(self, request_id: int, request_parameters: dict) -> dict:
        self._logger.info(f"Editing a request with {request_id} id...")
        cleaned_request_parameters = helpers.clean_dict(request_parameters)
        if not cleaned_request_parameters:
            raise PluginException(
                cause="Not enough input parameters were provided.",
                assistance="Please provide at least one input parameter except request id and try again. If the issue persists, please contact support.",
            )
        return self.make_json_request(
            method="PUT",
            url=REQUEST_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": cleaned_request_parameters}),
        )

    def delete_request(self, request_id: int) -> dict:
        self._logger.info(f"Deleting a request with {request_id} id...")
        return self.make_json_request(
            method="DELETE",
            url=DELETE_REQUEST_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
        )

    def close_request(self, request_id: int, closure_parameters: dict = None) -> dict:
        self._logger.info(f"Closing a request with {request_id} id...")
        return self.make_json_request(
            method="PUT",
            url=CLOSE_REQUEST_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": {"closure_info": helpers.clean_dict(closure_parameters)}}),
        )

    def assign_request(self, request_id: int, group: dict = None, technician: dict = None) -> dict:
        self._logger.info(f"Assigning a request with {request_id} id...")
        assign_params = helpers.clean_dict({"group": group, "technician": technician})
        if not assign_params:
            raise PluginException(
                cause="Not enough input parameters were provided.",
                assistance="Please provide at least one input parameter except request id and try again. If the issue persists, please contact support.",
            )

        return self.make_json_request(
            method="PUT",
            url=ASSIGN_REQUEST_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": assign_params}),
        )

    def pickup_request(self, request_id: int) -> dict:
        self._logger.info(f"Picking up a request with {request_id} id...")
        return self.make_json_request(
            method="PUT",
            url=PICKUP_REQUEST_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
        )

    def add_request_resolution(
        self, request_id: int, content: str = None, add_to_linked_requests: bool = False
    ) -> dict:
        self._logger.info(f"Adding resolution to the request with {request_id} id...")
        return self.make_json_request(
            method="POST",
            url=REQUEST_RESOLUTIONS_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data(
                {"resolution": {"content": content, "add_to_linked_requests": add_to_linked_requests}}
            ),
        )

    def get_request_resolution(self, request_id: int) -> dict:
        self._logger.info(f"Getting resolution added to the request with {request_id} id...")
        return self.make_json_request(
            method="GET",
            url=REQUEST_RESOLUTIONS_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
        )

    def add_request_note(
        self,
        request_id: int,
        description: str,
        show_to_requester: bool = False,
        notify_technician: bool = False,
        mark_first_response: bool = False,
        add_to_linked_requests: bool = False,
    ) -> dict:
        self._logger.info(f"Adding note to the request with {request_id} id...")
        return self.make_json_request(
            method="POST",
            url=REQUEST_NOTES_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
            data=helpers.prepare_input_data(
                {
                    "note": {
                        "description": description,
                        "show_to_requester": show_to_requester,
                        "notify_technician": notify_technician,
                        "mark_first_response": mark_first_response,
                        "add_to_linked_requests": add_to_linked_requests,
                    }
                }
            ),
        )

    def edit_request_note(
        self,
        request_id: int,
        request_note_id: int,
        description: str = None,
        show_to_requester: bool = False,
        notify_technician: bool = False,
        mark_first_response: bool = False,
        add_to_linked_requests: bool = False,
    ) -> dict:
        self._logger.info(
            f"Updating a note with {request_note_id} note id added to the request with {request_id} id..."
        )
        note_params = helpers.clean_dict(
            {
                "description": description,
                "show_to_requester": show_to_requester,
                "notify_technician": notify_technician,
                "mark_first_response": mark_first_response,
                "add_to_linked_requests": add_to_linked_requests,
            }
        )
        if not note_params:
            raise PluginException(
                cause="Not enough input parameters were provided.",
                assistance="Please provide at least one input parameter except ids and try again. If the issue persists, please contact support.",
            )
        return self.make_json_request(
            method="PUT",
            url=REQUEST_NOTE_ENDPOINT.format(
                request_id=request_id, request_note_id=request_note_id, sdp_base_url=self._sdp_base_url
            ),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"note": note_params}),
        )

    def delete_request_note(self, request_id: int, request_note_id: int) -> dict:
        self._logger.info(f"Deleting a note with {request_note_id} note id added to the request with {request_id} id…")
        return self.make_json_request(
            method="DELETE",
            url=REQUEST_NOTE_ENDPOINT.format(
                request_id=request_id, request_note_id=request_note_id, sdp_base_url=self._sdp_base_url
            ),
            headers=self._get_headers(),
        )

    def get_request_notes(self, request_id: int) -> dict:
        self._logger.info(f"Getting a list of notes added to the request with {request_id} id…")
        return self.make_json_request(
            method="GET",
            url=REQUEST_NOTES_ENDPOINT.format(request_id=request_id, sdp_base_url=self._sdp_base_url),
            headers=self._get_headers(),
        )

    def make_request(
        self, method: str, url: str, headers: dict, params: dict = None, data: dict = None
    ) -> requests.Response:
        try:
            response = requests.request(method=method, url=url, headers=headers, params=params, data=data)

            if response.status_code == 400:
                raise PluginException(
                    preset=PluginException.Preset.BAD_REQUEST, data=helpers.replace_status_code(response.json())
                )
            if response.status_code == 403:
                raise PluginException(
                    cause="Operation is not allowed.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=helpers.replace_status_code(response.json()),
                )
            if response.status_code == 404:
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=helpers.replace_status_code(response.json()),
                )
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=helpers.replace_status_code(response.json()),
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def make_json_request(
        self, method: str, url: str, headers: dict = None, params: dict = None, data: dict = None
    ) -> dict:
        try:
            response = self.make_request(method=method, url=url, params=params, data=data, headers=headers)
            response_json = response.json()
            response_json = helpers.map_ids_to_integer(response_json)
            return response_json
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
