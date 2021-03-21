import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response
from urllib.parse import urlparse, urlsplit, urlunsplit
from logging import Logger
from requests.auth import HTTPDigestAuth, HTTPBasicAuth
import json


class Common:
    """Merge 2 dictionaries"""

    @staticmethod
    def merge_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    """Copy the case insensitive headers dict to a normal one"""

    @staticmethod
    def copy_dict(x):
        d = {}
        for key in x:
            d[key] = x[key]
        return d

    @staticmethod
    def body_object(response) -> object:

        body_object = {}
        try:
            body_object = response.json()
        except ValueError:
            """ Nothing? We don't care if it fails, that could be normal """
        # It's possible to have a successful call with no body
        # https://stackoverflow.com/questions/32319845/python-requests-gives-none-response-where-json-data-is-expected
        if body_object is None:
            body_object = {}

        return body_object


def url_path_join(*parts):
    """Normalize url parts and join them with a slash."""
    schemes, netlocs, paths, queries, fragments = zip(*(urlsplit(part) for part in parts))
    scheme = first(schemes)
    netloc = first(netlocs)
    path = '/'.join(x.strip('/') for x in paths if x)
    query = first(queries)
    fragment = first(fragments)
    return urlunsplit((scheme, netloc, path, query, fragment))


def first(sequence, default=''):
    return next((x for x in sequence if x), default)


class RestAPI(object):
    CUSTOM_SECRET_INPUT = "CUSTOM_SECRET_INPUT"

    def __init__(
            self, url: str, logger: Logger, ssl_verify: bool, default_headers: dict = None
    ):
        self.url = url
        self.logger = logger
        self.ssl_verify = ssl_verify
        self.auth = None
        self.default_headers = default_headers

    def with_credentials(
            self, authentication_type: str, username: str = None, password: str = None, secret_key: str = None
    ):
        if authentication_type == "Basic Auth" or authentication_type == "Digest Auth":
            if not username or not password:
                raise PluginException(
                    cause="Basic Auth authentication selected without providing username and password.",
                    assistance="The authentication type requires a username and password."
                               " Please complete the connection with a username and password or change the authentication type.",
                )
        else:
            if not secret_key:
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
                    new_headers[key] = secret_key
                else:
                    new_headers[key] = value
            self.default_headers = new_headers

    def call_api(
            self, method: str, path: str, data: str = None, json_data: dict = None, headers: dict = None
    ) -> Response:
        try:
            response = requests.request(
                method,
                url_path_join(self.url, path),
                data=data,
                json=json_data,
                headers=Common.merge_dicts(self.default_headers, headers or {}),
                auth=self.auth
            )

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
            TestRestAPI.get_parsed_url(rest_api.url),
            rest_api.logger,
            rest_api.ssl_verify,
            rest_api.default_headers
        )

    @staticmethod
    def get_parsed_url(url: str):
        url_parsed = urlparse(url)
        return f"{url_parsed.scheme}://{url_parsed.netloc}"
