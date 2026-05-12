import json
import time
from logging import Logger
from typing import Optional

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_manage_engine_service_desk.util import helpers
from icon_manage_engine_service_desk.util.constants import (
    API_REQUEST_INITIAL_BACKOFF_SECONDS,
    API_REQUEST_MAX_RETRIES,
    CLOUD_API_BASE_URLS,
    DEFAULT_TOKEN_EXPIRY_SECONDS,
    OAUTH_REQUEST_TIMEOUT_SECONDS,
    TOKEN_EXPIRY_BUFFER_SECONDS,
    TOKEN_FETCH_INITIAL_BACKOFF_SECONDS,
    TOKEN_FETCH_MAX_RETRIES,
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
        Caches the result and only re-fetches when the token has expired.
        Retries with exponential backoff on transient failures."""
        if self._access_token and time.time() < self._access_token_expiry:
            return self._access_token

        self._logger.info("Fetching new Zoho OAuth access token...")
        last_error = None

        for attempt in range(TOKEN_FETCH_MAX_RETRIES):
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
                    timeout=OAUTH_REQUEST_TIMEOUT_SECONDS,
                )
                response.raise_for_status()
                token_data = response.json()
            except requests.exceptions.RequestException as error:
                last_error = error
                if attempt < TOKEN_FETCH_MAX_RETRIES - 1:
                    backoff = TOKEN_FETCH_INITIAL_BACKOFF_SECONDS * (2**attempt)
                    self._logger.info(
                        f"Token fetch attempt {attempt + 1} failed: {error}. Retrying in {backoff}s..."
                    )
                    time.sleep(backoff)
                    continue
                raise PluginException(
                    cause="Failed to obtain Zoho OAuth access token.",
                    assistance="Verify that the Client ID, Client Secret, Refresh Token, and Data Center are correct.",
                    data=last_error,
                )

            if "access_token" not in token_data:
                raise PluginException(
                    cause="Zoho OAuth token response did not contain an access token.",
                    assistance="Verify that the Client ID, Client Secret, and Refresh Token are correct.",
                    data=token_data,
                )

            self._access_token = token_data["access_token"]
            # Zoho tokens typically expire in 3600 seconds; subtract a 5-minute buffer
            expires_in = token_data.get("expires_in", DEFAULT_TOKEN_EXPIRY_SECONDS)
            self._access_token_expiry = time.time() + expires_in - TOKEN_EXPIRY_BUFFER_SECONDS
            return self._access_token

        # Should not reach here, but safety net
        raise PluginException(
            cause="Failed to obtain Zoho OAuth access token after retries.",
            assistance="Verify that the Client ID, Client Secret, Refresh Token, and Data Center are correct.",
            data=last_error,
        )

    def _get_headers(self) -> dict:
        if self._connection_type == ConnectionType.ON_PREM:
            return {"authtoken": self._api_key}
        return {
            "Authorization": f"Zoho-oauthtoken {self._get_access_token()}",
            "Accept": "application/vnd.manageengine.sdp.v3+json",
            "Content-Type": "application/x-www-form-urlencoded",
        }

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
        input_data = helpers.prepare_input_data({"list_info": list_parameters}) if list_parameters else None
        return self.make_json_request(
            method="GET",
            url=REQUESTS_ENDPOINT.format(api_base=self._api_base),
            headers=self._get_headers(),
            data=input_data,
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

    @property
    def _note_key(self) -> str:
        """Cloud API uses 'request_note' while On-Prem uses 'note' as the entity key."""
        return "request_note" if self._connection_type != ConnectionType.ON_PREM else "note"

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
        response = self.make_json_request(
            method="POST",
            url=REQUEST_NOTES_ENDPOINT.format(api_base=self._api_base, request_id=request_id),
            headers=self._get_headers(),
            data=helpers.prepare_input_data(
                {
                    self._note_key: {
                        "description": description,
                        "show_to_requester": show_to_requester,
                        "notify_technician": notify_technician,
                        "mark_first_response": mark_first_response,
                        "add_to_linked_requests": add_to_linked_requests,
                    }
                }
            ),
        )
        return helpers.normalize_note_response(response)

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
            data=helpers.prepare_input_data({self._note_key: note_params}),
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
            if response.status_code == 401:
                raise PluginException(
                    cause="Authentication failed.",
                    assistance="The access token may have expired or been revoked. Please try again.",
                    data=response.text,
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
            if response.status_code == 429:
                raise PluginException(
                    cause="API rate limit reached.",
                    assistance="Too many requests. Please wait and try again.",
                    data=response.text,
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
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def make_json_request(
        self, method: str, url: str, headers: dict = None, params: dict = None, data: dict = None
    ) -> dict:
        """Make an API request with retry logic for rate limits, server errors, and token expiry."""
        last_error = None

        for attempt in range(API_REQUEST_MAX_RETRIES):
            try:
                response = self.make_request(method=method, url=url, params=params, data=data, headers=headers)
                return response.json()
            except PluginException as error:
                last_error = error
                is_retryable = (
                    "API rate limit reached" in str(error.cause)
                    or error.preset == PluginException.Preset.SERVER_ERROR
                )
                is_auth_failure = "Authentication failed" in str(error.cause)

                if is_auth_failure and self._connection_type != ConnectionType.ON_PREM:
                    # Token may have been revoked — clear cache and retry once
                    if attempt < 1:
                        self._logger.info("Received 401, refreshing access token and retrying...")
                        self._access_token = None
                        self._access_token_expiry = 0.0
                        headers = self._get_headers()
                        continue
                    raise

                if is_retryable and attempt < API_REQUEST_MAX_RETRIES - 1:
                    backoff = API_REQUEST_INITIAL_BACKOFF_SECONDS * (2**attempt)
                    self._logger.info(
                        f"Request attempt {attempt + 1} failed: {error.cause}. Retrying in {backoff}s..."
                    )
                    time.sleep(backoff)
                    # Refresh headers in case token expired during backoff
                    if self._connection_type != ConnectionType.ON_PREM:
                        headers = self._get_headers()
                    continue

                raise
            except json.decoder.JSONDecodeError as error:
                raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)

        raise last_error
