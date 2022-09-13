import json
import os.path
from logging import Logger

from urllib.parse import urlparse, urlsplit, urlunsplit, urlencode
from typing import Dict, Any, Union
import base64

import requests
import tempfile
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

MESSAGE_CAUSE_BOTH_INPUTS = "You cannot send both inputs"
MESSAGE_ASSISTANCE_BOTH_INPUTS = "Try sending data either as an array OR an object, not both."


class Common:
    """Merge 2 dictionaries"""

    @staticmethod
    def merge_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    @staticmethod
    def copy_dict(x):
        """Copy the case insensitive headers dict to a normal one"""
        d = {}
        for key in x:
            d[key] = x[key]
        return d

    @staticmethod
    def body_object(response) -> dict:
        body_object = {}
        try:
            body_object = response.json()
        except ValueError:
            pass
        # Nothing? We don't care if it fails, that could be normal
        # It's possible to have a successful call with no body
        # https://stackoverflow.com/questions/32319845/python-requests-gives-none-response-where-json-data-is-expected
        if body_object is None:
            body_object = {}

        if isinstance(body_object, dict):
            return body_object
        else:
            # Convert to object
            return {"object": body_object}


def url_path_join(*parts):
    """Normalize url parts and join them with a slash."""
    schemes, netlocs, paths, queries, fragments = zip(*(urlsplit(part.strip()) for part in parts))
    scheme = first(schemes)
    netloc = first(netlocs)
    path = "/".join(x.strip("/") for x in paths if x)
    query = first(queries)
    fragment = first(fragments)
    return urlunsplit((scheme, netloc, path, query, fragment))


def first(sequence, default=""):
    return next((x for x in sequence if x), default)


def check_headers_for_urlencoded(headers: Union[Dict[str, str], None]) -> bool:
    """
    This method will check the headers for 'content-type' == 'application/x-www-form-urlencoded'
    :param headers: Headers dict to read
    :return: Boolean value indicating if the conditional is present
    """
    if headers is None:
        headers = {}
    for key, value in headers.items():
        if key.lower() == "content-type" and value.lower() == "application/x-www-form-urlencoded":
            return True
    return False


def convert_body_for_urlencoded(headers: Dict[str, str], body: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    This method will encode the body if the headers == x-www-form-urlencoded
    :param headers: Headers dict to read for conditional
    :param body: Body dict to convert to string with encoding
    :return: Body as an encoded string value
    """
    if check_headers_for_urlencoded(headers):
        body = urlencode(body)
    return body


def write_to_file(file: dict, file_path: str) -> str:
    """
    This method will write an input file as bytes and return the file path
    :param file: The file object containing content and filename
    :file_path: the file path to be used
    :return: the location of the written file
    """
    with open(file_path + file.get("filename"), "wb") as new_file:
        base64_decoded = base64.b64decode(file.get("content"))
        new_file.write(base64_decoded)
    return file_path + file.get("filename")


class RestAPI(object):
    CUSTOM_SECRET_INPUT = "CUSTOM_SECRET_INPUT"  # noqa: B105

    def __init__(
        self,
        url: str,
        logger: Logger,
        ssl_verify: bool,
        default_headers: dict = None,
        fail_on_error: bool = True,
        certificate=None,
        key=None,
    ):
        self.url = url
        self.logger = logger
        self.ssl_verify = ssl_verify
        self.auth = None
        self.default_headers = default_headers
        self.fail_on_error = fail_on_error,
        self.certificate = certificate
        self.key = key

    def with_credentials(
        self, authentication_type: str, username: str = None, password: str = None, secret_key: str = None
    ):
        if authentication_type in ("Basic Auth", "Digest Auth"):
            if not username or not password:
                raise PluginException(
                    cause="Basic Auth authentication selected without providing username and password.",
                    assistance="The authentication type requires a username and password."
                    " Please complete the connection with a username and password or change the authentication type.",
                )
        else:
            if not secret_key and authentication_type != "Custom":
                raise PluginException(
                    cause="An authentication type was selected that requires a secret key.",
                    assistance="Please complete the connection with a secret key or change the authentication type.",
                )

        if authentication_type == "Basic Auth":
            self.auth = HTTPBasicAuth(username, password)
        elif authentication_type == "Digest Auth":
            self.auth = HTTPDigestAuth(username, password)
        elif authentication_type == "Bearer Token":
            self.default_headers = Common.merge_dicts(self.default_headers, {"Authorization": f"Bearer {secret_key}"})
        elif authentication_type == "Rapid7 Insight":
            self.default_headers = Common.merge_dicts(self.default_headers, {"X-Api-Key": secret_key})
        elif authentication_type == "OpsGenie":
            self.default_headers = Common.merge_dicts(self.default_headers, {"Authorization": f"GenieKey {secret_key}"})
        elif authentication_type == "Pendo":
            self.default_headers = Common.merge_dicts(
                self.default_headers, {"content-type": "application/json", "x-pendo-integration-key": secret_key}
            )
        elif authentication_type == "Custom":
            new_headers = {}
            for key, value in self.default_headers.items():
                if value == self.CUSTOM_SECRET_INPUT:
                    if not secret_key:
                        raise PluginException(
                            cause="'CUSTOM_SECRET_INPUT' used in authentication header, but no secret provided.",
                            assistance="When using 'CUSTOM_SECRET_INPUT' as a value in authentication headers the"
                            " 'secret_key' field is required.",
                        )
                    new_headers[key] = secret_key
                else:
                    new_headers[key] = value
            self.default_headers = new_headers

    def call_api(
        self,
        method: str,
        path: str,
        data: str = None,
        json_data: dict = None,
        headers: dict = None,
    ) -> Response:
        try:
            # IF data exists - check the headers
            # IF urlencoded is in headers, send data as it is
            # ELSE run json.dumps(data)
            # ELSE data == None
            data_string = None
            if data and check_headers_for_urlencoded(headers):
                data_string = data
            elif data:
                data_string = json.dumps(data)

            request_params = {
                "method": method,
                "url": url_path_join(self.url, path),
                "data": data_string,
                "json": json_data,
                "headers": Common.merge_dicts(self.default_headers, headers or {}),
                "auth": self.auth,
                "verify": self.ssl_verify,
            }

            file_path = tempfile.mkdtemp() + "/"
            if self.certificate:
                certificate_path = write_to_file(self.certificate, file_path)
                request_params["cert"] = certificate_path
            if self.key and self.certificate:
                key_path = write_to_file(self.key, file_path)
                request_params["cert"] = (
                    certificate_path,
                    key_path
                )

            response = requests.request(**request_params)
            if not self.fail_on_error:
                return response

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.json().get("message", response.text),
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)


class TestRestAPI(RestAPI):
    def __init__(self, rest_api: RestAPI):
        super().__init__(
            TestRestAPI.get_parsed_url(rest_api.url), rest_api.logger, rest_api.ssl_verify, rest_api.default_headers
        )

    @staticmethod
    def get_parsed_url(url: str):
        url_parsed = urlparse(url)
        return f"{url_parsed.scheme}://{url_parsed.netloc}"
