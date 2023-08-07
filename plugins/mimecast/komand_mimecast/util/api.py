import base64
import binascii
import datetime
import hashlib
import hmac
import json
import uuid
from io import BytesIO
from typing import Union, List, Dict, Any
from zipfile import ZipFile, BadZipFile

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case

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
)
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.util.util import Utils


class MimecastAPI:
    def __init__(self, region: str, access_key: str, secret_key: str, app_id: str, app_key: str, logger=None):
        self.url = Utils.prepare_base_url(region)
        self.access_key = access_key
        self.secret_key = secret_key
        self.app_id = app_id
        self.app_key = app_key
        self.logger = logger
        self.logger.info(self.url)

    def get_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/url/get-all-managed-urls", data=data)

    def get_ttp_url_logs(self, data: dict, meta_data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/url/get-logs", data=data, meta_data=meta_data)

    def add_group_member(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/directory/add-group-member", data=data)

    def create_blocked_sender_policy(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/policy/blockedsenders/create-policy", data=data)

    def delete_blocked_sender_policy(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/policy/blockedsenders/delete-policy", data=data)

    def search_message_finder(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/message-finder/search", data=data)

    def create_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/url/create-managed-url", data=data)

    def decode_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/url/decode-url", data=data)

    def delete_group_member(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/directory/remove-group-member", data=data)

    def delete_managed_url(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/url/delete-managed-url", data=data)

    def find_groups(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/directory/find-groups", data=data)

    def permit_or_block_sender(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/managedsender/permit-or-block-sender", data=data)

    def get_audit_events(self, data: dict, meta_data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/audit/get-audit-events", data=data, meta_data=meta_data)

    def create_remediation_incident(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/remediation/create", data=data)

    def get_remediation_incident(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/remediation/get-incident", data=data)

    def find_remediation_incidents(self, data: dict) -> dict:
        return self._handle_rest_call("POST", f"{API}/ttp/remediation/find-incidents", data=data)

    def get_siem_logs(self, data: Dict[str, Any]) -> Union[List[Dict], Dict, int]:
        uri = f"{API}/audit/get-siem-logs"
        default_data = {
            "compress": True,
            "file_format": "JSON",
            "type": "MTA",
        }
        data.update(default_data)
        payload = {DATA_FIELD: ([convert_dict_to_camel_case(data)] if data is not None else [])}

        request = requests.request(
            method="POST", url=f"{self.url}{uri}", headers=self._prepare_header(uri), data=str(payload)
        )
        self._check_rate_limiting(request)

        if "attachment" in request.headers.get("Content-Disposition", ""):
            combined_json_list = self._handle_zip_file(request)
            return combined_json_list, request.headers, request.status_code

        response = request.json()
        status_code = response.get(META_FIELD).get(STATUS_FIELD)
        try:
            if response.get(FAIL_FIELD):
                self._handle_siem_logs_error_response(response, status_code)
        except PluginException as error:
            status_code = error.status_code if isinstance(error, ApiClientException) else status_code
            raise ApiClientException(
                cause=error.cause,
                assistance=error.assistance,
                data=error.data,
                preset=error.preset,
                status_code=status_code,
            )
        raise ApiClientException(preset=PluginException.Preset.UNKNOWN, data=response, status_code=status_code)

    def _check_rate_limiting(self, request):
        rate_limit_status_code = 429
        if request.status_code == rate_limit_status_code:
            raise ApiClientException(
                preset=PluginException.Preset.RATE_LIMIT, status_code=rate_limit_status_code, data=request.text
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

    def _handle_zip_file(self, request: requests.request) -> List[Dict]:
        """
        Extracts JSON data from a ZIP file contained in a requests response
        Args:
            request (requests.request): The HTTP request object containing the ZIP file in its response
        Returns:
            List[Dict]: A list of dictionaries, where each dictionary represents a log entry extracted from the ZIP file
        """
        try:
            with ZipFile(BytesIO(request.content)) as my_zip:
                combined_json_list = [
                    log for file_name in my_zip.namelist() for log in json.loads(my_zip.read(file_name)).get("data")
                ]
            return combined_json_list
        except BadZipFile:
            return []

    def _prepare_header(self, uri: str) -> dict:
        # Generate request header values
        request_id = str(uuid.uuid4())
        hdr_date = f'{datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S")} UTC'

        # Decode secret key
        try:
            encoded_secret_key = self.secret_key.encode()
            bytes_secret_key = base64.b64decode(encoded_secret_key)
        except binascii.Error as error:
            raise ApiClientException(
                cause=PluginException.causes[PluginException.Preset.API_KEY],
                assistance="Please make sure that the Secret Key is valid and try again.",
                data=error,
                status_code=401,
            )

        # Create hmac message
        msg = ":".join([hdr_date, request_id, uri, self.app_key])

        # Create the HMAC SHA1 of the Base64 decoded secret key for the Authorization header
        hmac_sha1 = hmac.new(bytes_secret_key, msg.encode(), digestmod=hashlib.sha1).digest()

        # Use the HMAC SHA1 value to sign the hdrDate + ":" requestId + ":" + URI + ":" + appkey
        sig = base64.encodebytes(hmac_sha1).rstrip()
        sig = sig.decode("UTF-8")

        # Create request headers
        return {
            "Authorization": f"MC {self.access_key}:{sig}",
            "x-mc-app-id": self.app_id,
            "x-mc-date": hdr_date,
            "x-mc-req-id": request_id,
            "Content-Type": "application/json",
        }

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
                elif error.get(CODE) == DEVELOPER_KEY_ERROR:
                    raise ApiClientException(
                        preset=PluginException.Preset.API_KEY,
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

    def _handle_rest_call(  # noqa: C901
        self,
        method: str,
        uri: str,
        data: dict = None,
        meta_data: dict = None,
    ) -> dict:

        payload = {DATA_FIELD: ([data] if data is not None else [])}

        if meta_data is not None:
            payload[META_FIELD] = meta_data

        try:
            request = requests.request(
                method=method.upper(), url=f"{self.url}{uri}", headers=self._prepare_header(uri), data=str(payload)
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
            self._handle_error_response(response)

        status_code = response.get(META_FIELD).get(STATUS_FIELD)
        if not status_code or 200 <= status_code <= 299:
            return response

        self._handle_status_code_response(response, status_code)
