import json
from logging import Logger
from urllib.parse import urlparse, urlsplit, urlunsplit
from typing import Dict, Any

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response
from requests.auth import HTTPBasicAuth, HTTPDigestAuth


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


def convert_dict_body_to_string(dict_object: Dict[str, Any]):
    """
    This method will convert a dict object to a string
    suitable for sending data in x-www-form-urlencoded format
    :param dict_object: The dict object to convert
    :return: A new string properly formatted
    """
    output_string = ""
    for key, value in dict_object.items():
        output_string += f"{key}={value}&"
    output_string = output_string[:-1]
    return output_string


def convert_string_to_dict(input_string: str) -> dict:
    output_dict = {}
    for parameter in input_string.split('&'):
        try:
            splitted_parameter = parameter.split('=')
            output_dict[splitted_parameter[0]] = splitted_parameter[1]
        except:
            raise PluginException(cause="Wrong format of input_string")
    return output_dict


class RestAPI(object):
    CUSTOM_SECRET_INPUT = "CUSTOM_SECRET_INPUT"  # noqa: B105

    def __init__(
            self, url: str, logger: Logger, ssl_verify: bool, default_headers: dict = None, fail_on_error: bool = True
    ):
        self.url = url
        self.logger = logger
        self.ssl_verify = ssl_verify
        self.auth = None
        self.default_headers = default_headers
        self.fail_on_error = fail_on_error

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
            self, method: str, path: str, data: str = None, json_data: dict = None, headers: dict = None
    ) -> Response:
        try:
            data_string = json.dumps(data) if data else None
            response = requests.request(
                method,
                url_path_join(self.url, path),
                data=data_string,
                json=json_data,
                headers=Common.merge_dicts(self.default_headers, headers or {}),
                auth=self.auth,
                verify=self.ssl_verify,
            )
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
