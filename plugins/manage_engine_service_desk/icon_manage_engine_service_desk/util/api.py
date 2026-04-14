import json
import time
from logging import Logger
from typing import Optional

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_manage_engine_service_desk.util import helpers
from icon_manage_engine_service_desk.util.constants import (
    CLOUD_API_BASE_URLS,
    ZOHO_OAUTH_BASE_URLS,
    ConnectionType,
    Request,
)
from icon_manage_engine_service_desk.util.endpoints import (
    ASSIGN_REQUEST_ENDPOINT,
    CLOSE_REQUEST_ENDPOINT,
    DELETE_REQUEST_ENDPOINT,
    PICKUP_REQUEST_ENDPOINT,
    REQUEST_ENDPOINT,
    REQUEST_NOTE_ENDPOINT,
    REQUEST_NOTES_ENDPOINT,
    REQUEST_RESOLUTIONS_ENDPOINT,
    REQUESTS_ENDPOINT,
)


class ManageEngineServiceDeskAPI:
    def __init__(
        self,
        connection_type: str,
        logger: Logger,
        # On-Prem fields
        api_key: Optional[str] = None,
        sdp_base_url: Optional[str] = None,
        ssl_verify: bool = True,
        # Cloud fields
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        refresh_token: Optional[str] = None,
        portal_name: Optional[str] = None,
        data_center: Optional[str] = None,
    ):
        self._connection_type = connection_type
        self._logger = logger
        self.ssl_verify = ssl_verify

        if connection_type == ConnectionType.ON_PREM:
            self._api_key = api_key
            self._api_base = f"{sdp_base_url.rstrip('/')}/api/v3"
            self._zoho_oauth_base = None
            self._client_id = None
            self._client_secret = None
            self._refresh_token = None
        else:
            cloud_base = CLOUD_API_BASE_URLS[data_center]
            self._api_base = f"{cloud_base}/app/{portal_name}/api/v3"
            self._zoho_oauth_base = ZOHO_OAUTH_BASE_URLS[data_center]
            self._client_id = client_id
            self._client_secret = client_secret
            self._refresh_token = refresh_token
            self._api_key = None
            # Cache for the short-lived access token
            self._access_token: Optional[str] = None
            self._access_token_expiry: float = 0.0

    def _get_access_token(self) -> str:
        """Fetch a new Zoho OAuth access token using the stored refresh token.
        Caches the result and only re-fetches when the token has expired."""
        if self._access_token and time.time() < self._access_token_expiry:
            return self._access_token

        self._logger.info("Fetching new Zoho OAuth access token...")
        try:
            response = requests.post(
                url=f"{self._zoho_oauth_base}/oauth/v2/token",
                params={
                    "grant_type": "refresh_token",
                    "client_id": self._client_id,
                    "client_secret": self._client_secret,
                    "refresh_token": self._refresh_token,
                },
                verify=True,
                timeout=30,
            )
            response.raise_for_status()
            token_data = response.json()
        except requests.exceptions.RequestException as e:
            raise PluginException(
                cause="Failed to obtain Zoho OAuth access token.",
                assistance="Verify that the Client ID, Client Secret, Refresh Token, and Data Center are correct.",
                data=str(e),
            )

        if "access_token" not in token_data:
            raise PluginException(
                cause="Zoho OAuth token response did not contain an access token.",
                assistance="Verify that the Client ID, Client Secret, and Refresh Token are correct.",
                data=token_data,
            )

        self._access_token = token_data["access_token"]
        # Zoho tokens typically expire in 3600 seconds; subtract a 60-second buffer
        expires_in = token_data.get("expires_in", 3600)
        self._access_token_expiry = time.time() + expires_in - 60
        return self._access_token

    def _get_headers(self) -> dict:
        if self._connection_type == ConnectionType.ON_PREM:
            return {"authtoken": self._api_key}
        return {"Authorization": f"Zoho-oauthtoken {self._get_access_token()}"}

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
            url=REQUESTS_ENDPOINT.format(api_base=self._api_base),
            headers=self._get_headers(),
            params=helpers.prepare_input_data({"list_info": list_parameters}),
        )

    def get_request(self, request_id: int) -> dict:
        self._logger.info(f"Getting a request with {request_id} id...")
        return self.make_json_request(
            method="GET",
            url=REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
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
            url=REQUESTS_ENDPOINT.format(api_base=self._api_base),
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
            url=REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": cleaned_request_parameters}),
        )

    def delete_request(self, request_id: int) -> dict:
        self._logger.info(f"Deleting a request with {request_id} id...")
        return self.make_json_request(
            method="DELETE",
            url=DELETE_REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
        )

    def close_request(self, request_id: int, closure_parameters: dict = None) -> dict:
        self._logger.info(f"Closing a request with {request_id} id...")
        return self.make_json_request(
            method="PUT",
            url=CLOSE_REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
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
            url=ASSIGN_REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"request": assign_params}),
        )

    def pickup_request(self, request_id: int) -> dict:
        self._logger.info(f"Picking up a request with {request_id} id...")
        return self.make_json_request(
            method="PUT",
            url=PICKUP_REQUEST_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
        )

    def add_request_resolution(
        self, request_id: int, content: str = None, add_to_linked_requests: bool = False
    ) -> dict:
        self._logger.info(f"Adding resolution to the request with {request_id} id...")
        return self.make_json_request(
            method="POST",
            url=REQUEST_RESOLUTIONS_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
            data=helpers.prepare_input_data(
                {"resolution": {"content": content, "add_to_linked_requests": add_to_linked_requests}}
            ),
        )

    def get_request_resolution(self, request_id: int) -> dict:
        self._logger.info(f"Getting resolution added to the request with {request_id} id...")
        return self.make_json_request(
            method="GET",
            url=REQUEST_RESOLUTIONS_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
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
            url=REQUEST_NOTES_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
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
                api_base=self._api_base, request_id=request_id, request_note_id=request_note_id
            ),
            headers=self._get_headers(),
            data=helpers.prepare_input_data({"note": note_params}),
        )

    def delete_request_note(self, request_id: int, request_note_id: int) -> dict:
        self._logger.info(f"Deleting a note with {request_note_id} note id added to the request with {request_id} id…")
        return self.make_json_request(
            method="DELETE",
            url=REQUEST_NOTE_ENDPOINT.format(
                api_base=self._api_base, request_id=request_id, request_note_id=request_note_id
            ),
            headers=self._get_headers(),
        )

    def get_request_notes(self, request_id: int) -> dict:
        self._logger.info(f"Getting a list of notes added to the request with {request_id} id…")
        return self.make_json_request(
            method="GET",
            url=REQUEST_NOTES_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
        )

    def make_request(
        self, method: str, url: str, headers: dict, params: dict = None, data: dict = None
    ) -> requests.Response:
        try:
            response = requests.request(
                method=method, url=url, verify=self.ssl_verify, headers=headers, params=params, data=data
            )

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
