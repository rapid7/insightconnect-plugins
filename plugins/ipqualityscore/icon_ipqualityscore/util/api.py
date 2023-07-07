import json
from logging import Logger
from requests import Response, session
from requests.exceptions import ConnectTimeout, HTTPError, InvalidURL, ProxyError
from insightconnect_plugin_runtime.exceptions import PluginException


BASE_URL = "https://ipqualityscore.com/api/json"
IP_ENDPOINT = BASE_URL + "/ip"
EMAIL_ENDPOINT = BASE_URL + "/email"
URL_ENDPOINT = BASE_URL + "/url"
PHONE_ENDPOINT = BASE_URL + "/phone"


class IPQSClient:
    def __init__(self, api_key, logger: Logger):
        self._headers = {"IPQS-KEY": api_key, "Content-Type": "application/json"}
        self._logger = logger
        self.session = session()

    def ipqs_lookup(self, url: str, ad_params: dict) -> dict:
        try:
            response = self.session.get(url, headers=self._headers, params=ad_params).json()
            if str(response["success"]) != "True":
                self._logger.error(f"Error: {response['message']}")
                raise PluginException(
                    cause=PluginException.Preset.BAD_REQUEST,
                    assistance="Verify your plugin input is correct and not malformed and try again. "
                    "If the issue persists, please contact support.\n",
                    data=response,
                )
            return response

        except (ConnectTimeout, ProxyError, InvalidURL) as error:
            msg = "Error connecting with the IPQualityScore."
            self._logger.error(f"{msg} Error: {error}")
            raise PluginException(
                cause=PluginException.Preset.BAD_REQUEST,
                assistance="Verify your plugin input is correct and not malformed and try again. "
                "If the issue persists, please contact support.\n",
                data=response,
            )

        except HTTPError as error:
            self._logger.info("[API ERROR] PluginException: UNKNOWN")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        except json.decoder.JSONDecodeError as error:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
