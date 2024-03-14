import json.decoder
from typing import Dict, List, Any
from insightconnect_plugin_runtime.exceptions import PluginException
import requests
from requests import Response

from komand_cuckoo.util import util


class API(object):
    def __init__(self, url: str):
        self.url = url

    def send(
        self,
        endpoint: str,
        method: str = "GET",
        data: Dict = None,
        files: List = None,
        _json: bool = True
    ) -> Any:
      """
      Sends a HTTP request, returning the response body or JSON
      """
      try:
        response = requests.Request(
          url=f"{self.url}/{endpoint}",
          method=method,
          data=data,
          files=files
        )
        self.response_handler(response)
        if _json:
          return util.extract_json(response)
        return response
      except requests.exceptions.HTTPError as exception:
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)

    @staticmethod
    def response_handler(response: Response) -> Response:
        """
        Handles response codes, returning appropriate PluginException Preset
        """
        if response.status_code == 400:
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=response.text)
        if response.status_code == 401:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=response.text)
        if response.status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
        if response.status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
        if 400 <= response.status_code < 500:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if 200 <= response.status_code < 300:
            return response
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
