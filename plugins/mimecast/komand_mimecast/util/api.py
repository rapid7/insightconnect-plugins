import json
import uuid
from typing import Dict
from urllib.request import Request
from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_mimecast.util.constants import (
    API,
    DATA_FIELD,
    META_FIELD,
    XDK_BINDING_EXPIRED_ERROR,
    CODE,
    FIELD_VALIDATION_ERROR,
    VALIDATION_BLANK_ERROR,
    ERROR_CASES,
    BASIC_ASSISTANCE_MESSAGE,
    FAIL_FIELD,
    STATUS_FIELD,
    DEVELOPER_KEY_ERROR,
    INVALID_REGION,
)
from komand_mimecast.util.exceptions import ApiClientException


class MimecastAPI:
    def __init__(self, client_id: str, client_secret: str, logger: Logger) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.logger = logger
        self.access_token = None

    def authenticate(self) -> None:
        self.logger.info("Authenticating...")
        data = {"client_id": self.client_id, "client_secret": self.client_secret, "grant_type": "client_credentials"}
        response = self._handle_rest_call(
            "POST",
            f"{API}/oauth/token",
            header_fields={"Content-Type": "application/x-www-form-urlencoded"},
            data=data,
        )
        self.access_token = response.get("access_token")
        self.logger.info("Authenticated")

    def get_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/url/get-all-managed-urls", data=data)

    def get_ttp_url_logs(self, data: dict, meta_data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/url/get-logs", data=data, meta_data=meta_data)

    def add_group_member(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/directory/add-group-member", data=data)

    def create_blocked_sender_policy(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/policy/blockedsenders/create-policy", data=data)

    def delete_blocked_sender_policy(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/policy/blockedsenders/delete-policy", data=data)

    def search_message_finder(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/message-finder/search", data=data)

    def create_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/url/create-managed-url", data=data)

    def decode_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/url/decode-url", data=data)

    def delete_group_member(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/directory/remove-group-member", data=data)

    def delete_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/url/delete-managed-url", data=data)

    def find_groups(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/directory/find-groups", data=data)

    def permit_or_block_sender(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/managedsender/permit-or-block-sender", data=data)

    def get_audit_events(self, data: dict, meta_data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/audit/get-audit-events", data=data, meta_data=meta_data)

    def create_remediation_incident(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/remediation/create", data=data)

    def get_remediation_incident(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/remediation/get-incident", data=data)

    def find_remediation_incidents(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/api/ttp/remediation/find-incidents", data=data)

    def _check_rate_limiting(self, response):
        rate_limit_status_code = 429
        if response.status_code == rate_limit_status_code:
            raise ApiClientException(
                preset=PluginException.Preset.RATE_LIMIT,
                status_code=rate_limit_status_code,
                data=response.text,
                response=response,
            )

    def _handle_status_code_response(self, response: requests.request, status_code: int):
        if status_code == 401:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response)
        elif status_code == 403:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response)
        elif status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response)
        elif status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response)
        else:
            self.logger.error(response)
            raise PluginException(
                cause="Server request failed.",
                assistance=f"Status code is {status_code}, see log for details.",
                data=response.get(FAIL_FIELD),
            )

    def _prepare_header(self, header_fields: Dict = {}, auth_token: str = None) -> dict:
        # Generate request header values
        request_id = str(uuid.uuid4())
        headers = {"x-mc-req-id": request_id}
        headers.update(header_fields)
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        return headers

    def _handle_error_response(self, response: dict):
        for errors in response.get(FAIL_FIELD, []):
            for error in errors.get("errors", []):
                if error.get(CODE) == XDK_BINDING_EXPIRED_ERROR:
                    raise PluginException(
                        cause=ERROR_CASES.get(XDK_BINDING_EXPIRED_ERROR),
                        assistance="Please provide a valid AccessKey.",
                        data=response,
                    )
                elif error.get(CODE) in ERROR_CASES:
                    raise PluginException(
                        cause=ERROR_CASES.get(error.get(CODE)),
                        assistance=BASIC_ASSISTANCE_MESSAGE,
                        data=response,
                    )
                elif error.get(CODE) == FIELD_VALIDATION_ERROR:
                    raise PluginException(
                        cause=f"This {error.get('field')} field is mandatory; it cannot be NULL.",
                        assistance=BASIC_ASSISTANCE_MESSAGE,
                        data=response,
                    )
                elif error.get(CODE) == VALIDATION_BLANK_ERROR:
                    raise PluginException(
                        cause=f"This {error.get('field')} field, if present, cannot be blank or empty.",
                        assistance=BASIC_ASSISTANCE_MESSAGE,
                        data=response,
                    )
                else:
                    self.logger.error(response)
                    raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)

    def _handle_siem_logs_error_response(self, response: dict, status_code: int):
        for errors in response.get(FAIL_FIELD, []):
            for error in errors.get("errors", []):
                if error.get(CODE) == XDK_BINDING_EXPIRED_ERROR:
                    raise ApiClientException(
                        preset=PluginException.Preset.API_KEY,
                        data=response,
                        status_code=401,
                    )
                elif error.get(CODE) == INVALID_REGION:
                    raise ApiClientException(
                        assistance="Please ensure that the correct region is selected",
                        cause="Incorrect region supplied.",
                        data=response,
                        status_code=403,
                    )
                elif error.get(CODE) == DEVELOPER_KEY_ERROR:
                    raise ApiClientException(
                        assistance="Please ensure that the correct app ID is selected",
                        cause="Incorrect app ID supplied.",
                        data=response,
                        status_code=401,
                    )
                elif error.get(CODE) in ERROR_CASES:
                    raise ApiClientException(
                        assistance=ERROR_CASES.get(error.get(CODE)),
                        cause=PluginException.causes[PluginException.Preset.BAD_REQUEST],
                        data=response,
                        status_code=400,
                    )
                elif error.get(CODE) == FIELD_VALIDATION_ERROR:
                    raise ApiClientException(
                        assistance=f"This {error.get('field')} field is mandatory; it cannot be NULL.",
                        cause=PluginException.causes[PluginException.Preset.BAD_REQUEST],
                        data=response,
                        status_code=400,
                    )
                elif error.get(CODE) == VALIDATION_BLANK_ERROR:
                    raise ApiClientException(
                        assistance=f"This {error.get('field')} field, if present, cannot be blank or empty.",
                        cause=PluginException.causes[PluginException.Preset.BAD_REQUEST],
                        data=response,
                        status_code=400,
                    )
                else:
                    self._handle_status_code_response(response, status_code)

    def _handle_rest_call(  # noqa: C901, pylint: disable=too-many-positional-arguments
        self,
        method: str,
        uri: str,
        data: dict = None,
        params: dict = None,
        meta_data: dict = None,
        header_fields: dict = {},
    ) -> dict:
        payload = data
        if meta_data is not None:
            payload[META_FIELD] = meta_data
        if not self.access_token:
            payload = str({DATA_FIELD: ([data] if data is not None else [])})
        try:
            request = requests.request(
                method=method.upper(),
                url=uri,
                headers=self._prepare_header(header_fields, self.access_token),
                data=payload,
                params=params,
            )
        except requests.exceptions.RequestException as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=e)

        self._check_rate_limiting(request)

        try:
            response = request.json()
        except json.decoder.JSONDecodeError as error:
            raise PluginException(
                cause="Unknown error.",
                assistance="The Mimecast server did not respond correctly. Response not in JSON format. Response in logs.",
                data=error,
            )

        if response.get(FAIL_FIELD):
            if response.get(FAIL_FIELD, [{}])[0].get("code", "") == "token_expired":
                self.logger.info("Token has expired, attempting re-authentication...")
                self.access_token = None
                self.authenticate()
                request = response.request
                return self._handle_rest_call(
                    method=request.method,
                    uri=request.url,
                    header_fields=self._prepare_header(request.headers, self.access_token),
                    data=request.body,
                    params=request.params,
                )
            else:
                self._handle_error_response(response)

        status_code = response.get(META_FIELD, {}).get(STATUS_FIELD)
        if not status_code or 200 <= status_code <= 299:
            return response

        self._handle_status_code_response(response, status_code)
