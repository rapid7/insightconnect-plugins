import hashlib
import hmac
import json
from datetime import datetime
from logging import Logger
from typing import Any, Dict
from urllib import parse

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean


class DarkTraceAPI:
    def __init__(
        self, url: str, public_token: str, private_token: str, ssl_verification: bool = True, logger: Logger = None
    ):
        self.url = url.rstrip("/")
        self.public_token = public_token
        self.private_token = private_token
        self.ssl_verification = ssl_verification
        self.logger = logger

    def get_status(self):
        return self._call_api("GET", "status")

    def model_breaches(self, params):
        return self._call_api("GET", "modelbreaches", params=clean(params))

    def update_intelfeed(
        self,
        status: bool,
        entry: str,
        description: str,
        source: str,
        expiration: str,
        hostname: bool,
    ):
        return self._call_api(
            "POST",
            "intelfeed",
            data={
                ("addentry" if status else "removeentry"): entry,
                "description": description,
                "expiry": expiration,
                "hostname": hostname,
                "source": source,
                "fulldetails": True,
            },
        )

    def _get_signature(self, request: str, date: str) -> str:
        return hmac.new(
            self.private_token.encode("ASCII"),
            f"{request}\n{self.public_token}\n{date}".encode("ASCII"),
            hashlib.sha1,
        ).hexdigest()

    def _get_headers(self, endpoint: str) -> Dict[str, Any]:
        """Returns the headers needed for all the Darktrace API requests

        :param endpoint: Endpoint for headers to be generated
        :type endpoint: str

        :return: Dictionary contains headers needed for Darktrace API requests
        :rtype: Dict[str, Any]
        """

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        headers = {
            "DTAPI-Token": self.public_token,
            "DTAPI-Date": date,
            "DTAPI-Signature": self._get_signature(endpoint, date),
        }
        return headers

    def _process_request_response(self, response: requests.Response) -> Dict[str, Any]:
        """Processes the request response depending on it's status code

        :param response: Response from requests.request
        :type response: requests.Response

        :return: Dict containing JSON API response
        :rtype: Dict[str, Any]
        """

        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if 300 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if 200 <= response.status_code < 300:
            return response.json() if response.text else {}
        raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

    def _call_api(self, method: str, path: str, data: dict = None, params: dict = None) -> dict:
        query = None
        if params:
            query = parse.urlencode(params)

        if data:
            query = parse.urlencode(data)

        endpoint = f"/{path}"
        if query:
            endpoint = f"{endpoint}?{query}"

        try:
            response = requests.request(
                method,
                f"{self.url}/{path}",
                data=data,
                params=params,
                headers=self._get_headers(endpoint),
                verify=self.ssl_verification,
            )
            return self._process_request_response(response)
        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
        except requests.exceptions.HTTPError as error:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=error)
