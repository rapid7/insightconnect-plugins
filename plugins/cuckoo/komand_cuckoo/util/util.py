import base64
import json
from typing import Dict
from insightconnect_plugin_runtime.exceptions import PluginException
from requests import Response


class Util(object):

    @staticmethod
    def extract_json(response: Response) -> Dict:
        """
        Extract JSON from a Response while catching JSONDecodeErrors
        :param response: The response object to extract JSON from
        :return: The JSON value of the response as a Python dictionary
        """
        try:
            return response.json()
        except json.decoder.JSONDecodeError as exception:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=exception)

    @staticmethod
    def prepare_decoded_value(content: bytes) -> str:
        """
        Prepare content ensuring unsafe characters are removed and a safe text representation is returned
        :param content: A bytes string
        :return: A decoded bytes string
        """
        try:
            return base64.b64encode(content).decode("UTF-8")
        except (TypeError, ValueError, UnicodeDecodeError) as exception:
            raise PluginException(preset=PluginException.Preset.BASE64_DECODE, data=exception)
