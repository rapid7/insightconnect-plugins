import json
import urllib.parse
from logging import Logger
from typing import Literal

import requests

from icon_hybrid_analysis.util import constants
from insightconnect_plugin_runtime.exceptions import PluginException


URL_PREFIX_TYPE = Literal[constants.DEFAULT_HTTP_PREFIX, constants.DEFAULT_HTTP_WWW_PREFIX]


class HybridAnalysisAPI:
    def __init__(self, url, api_key, logger: Logger):
        self.api_version = "v2"
        self.base_url = f"{url}/api/{self.api_version}"
        self.headers = {"User-Agent": constants.DEFAULT_USER_AGENT, "api-key": api_key}
        self.logger = logger

    def lookup_by_hash(self, analyzed_hash: str):
        return self._send_request(
            method="GET",
            path="/search/hash",
            url_prefix=constants.DEFAULT_HTTP_PREFIX,
            params={"hash": analyzed_hash},
        )

    def lookup_by_terms(self, data: dict):
        return self._send_request(
            method="POST", path="/search/terms", url_prefix=constants.DEFAULT_HTTP_PREFIX, data=data
        )

    def report(self, analyzed_hash: str):
        return self._send_request(
            method="GET",
            path=f"/report/{urllib.parse.quote(analyzed_hash)}/state",
            url_prefix=constants.DEFAULT_HTTP_WWW_PREFIX,
        )

    def submit(self, files: dict, data: dict):
        return self._send_request(
            method="POST", path="/submit/file", url_prefix=constants.DEFAULT_HTTP_PREFIX, files=files, data=data
        )

    def _send_request(
        self, method: str, path: str, url_prefix: URL_PREFIX_TYPE, data: dict = None, params=None, files: dict = None
    ) -> dict:
        try:
            response = requests.request(
                method.upper(),
                f"{url_prefix}{self.base_url}{path}",
                data=data,
                params=params,
                files=files,
                headers=self.headers,
            )

            if not response.status_code or 200 <= response.status_code <= 299:
                return response.json()

            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            elif response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            elif response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            else:
                raise PluginException(
                    cause=response.json().get("message", "Unknown"),
                    assistance=f"validation_errors: {response.json().get('validation_errors')}",
                )

        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
