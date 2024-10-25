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
from werkzeug.utils import secure_filename

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
    IS_LAST_TOKEN_FIELD,
    INVALID_REGION,
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

    def get_siem_logs(self, next_page_token: str) -> Union[List[Dict[str, Any]], Dict[str, Any], int]:
        uri = f"{API}/audit/get-siem-logs"
        data = {"compress": True, "file_format": "JSON", "type": "MTA", "token": next_page_token}

        payload = {DATA_FIELD: ([convert_dict_to_camel_case(data)] if data is not None else [])}

        prepared_headers = self._prepare_header(uri)

        response = requests.request(method="POST", url=f"{self.url}{uri}", headers=prepared_headers, data=str(payload))
        self._check_rate_limiting(response)

        if "attachment" in response.headers.get("Content-Disposition", "") or self._is_last_token(response):
            combined_json_list, file_name_list = self._handle_zip_file(response)
            return combined_json_list, response.headers, response.status_code, file_name_list

        # Due to how Mimecast returns a zip file in the response content, this error handling needs to happen after
        # the attempt to parse the content. Otherwise we hit json errors on the zipped content.
        try:
            response = response.json()
            status_code = response.get(META_FIELD, {}).get(STATUS_FIELD)
            if response.get(FAIL_FIELD):
                self._handle_siem_logs_error_response(response, status_code)
        except json.JSONDecodeError as json_error:
            error_info = f'response content="{response.content}", response headers="{response.headers}"'
            self.logger.info(
                f"A error was raised when making an api call to Mimecast with request ID '{prepared_headers.get('x-mc-req-id')}'"
            )
            raise ApiClientException(
                cause=json_error,
                data=error_info,
                preset=PluginException.Preset.INVALID_JSON,
                status_code=response.status_code,
            )
        except PluginException as error:
            status_code = error.status_code if isinstance(error, ApiClientException) else status_code
            self.logger.info(
                f"A error was raised when making an api call to Mimecast with request ID '{prepared_headers.get('x-mc-req-id')}'"
            )
            # From Mimecast API we can see that some errors are coming back as a 200
            # if the status code here is a 200 then these errors will not be correctly shown to the UI
            if status_code in [200, 201]:
                status_code = 400

            raise ApiClientException(
                cause=error.cause,
                assistance=error.assistance,
                data=error.data,
                preset=error.preset,
                status_code=status_code,
            )

        self.logger.info(
            f"A error was raised when making an api call to Mimecast with request ID '{prepared_headers.get('x-mc-req-id')}'"
        )
        raise ApiClientException(
            preset=PluginException.Preset.UNKNOWN, data=response.content, status_code=response.status_code
        )

    def _is_last_token(self, request: requests.Response) -> bool:
        """
        Check if the given response has the last page token.

        :param request: The response object to check and update.
        :type: requests.Response

        :return: True if the response contains last token, False otherwise.
        :rtype: bool
        """

        try:
            last_token = request.json().get("meta", {}).get(IS_LAST_TOKEN_FIELD, False)
            request.headers.update({IS_LAST_TOKEN_FIELD: last_token})
            return last_token
        except json.JSONDecodeError:
            return False

    def _check_rate_limiting(self, response):
        rate_limit_status_code = 429
        if response.status_code == rate_limit_status_code:
            raise ApiClientException(
                preset=PluginException.Preset.RATE_LIMIT, status_code=rate_limit_status_code, data=response.text
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
                combined_json_list = []
                file_name_list = my_zip.namelist()
                for file_name in file_name_list:
                    try:
                        # To avoid potential path traversal vulnerabilities, only valid files should be allowed.
                        # Due to the nature of the IO buffer, the filename cannot be checked until it is read in.
                        file_name = secure_filename(file_name)

                        contents = my_zip.read(file_name)
                        for log in json.loads(contents).get("data"):
                            combined_json_list += [log]
                    except json.decoder.JSONDecodeError as json_error:
                        self.logger.error(
                            f"JSON decode error on file ({file_name}), will continue loop... "
                            f"Mimecast request ID: '{request.headers.get('mc-siem-token')}', "
                            f"error: {json_error}, contents: {contents}",
                        )
                        continue
                    except Exception as gen_exception:
                        self.logger.error(
                            "Hit an unexpected error, will continue loop..."
                            f"Mimecast request ID: '{request.headers.get('mc-siem-token')}', "
                            f"error: {gen_exception}",
                            exc_info=True,
                        )
                        continue
            return combined_json_list, file_name_list
        except BadZipFile as error:
            # empty response from Mimecast can hit this, which we know is not an error, don't log it
            if error.args[0] != "File is not a zip file":
                self.logger.error(
                    "Hit BadZipFile, returning []. "
                    f"Mimecast request ID: '{request.headers.get('mc-siem-token')}', "
                    f"Error: {error}",
                    exc_info=True,
                )
        except Exception as exception_error:
            self.logger.error(
                "Hit an unexpected error,"
                f"Mimecast request ID: '{request.headers.get('mc-siem-token')}', "
                f"returning []. Error: {exception_error}",
                exc_info=True,
            )
        return [], []

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
