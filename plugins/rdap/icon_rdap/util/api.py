import json
from logging import Logger
import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_rdap.util.endpoints import ASN_ENDPOINT, DOMAIN_LOOKUP_ENDPOINT, IP_ENDPOINT


class RdapAPI:
    def __init__(self, logger: Logger):
        self._headers = {"Content-Type": "application/json"}
        self._logger = logger

    def asn_lookup(self, asn: int) -> dict:
        return self.make_json_request(method="GET", url=ASN_ENDPOINT.format(asn=asn))

    def domain_lookup(self, domain: str) -> dict:
        return self.make_json_request(method="GET", url=DOMAIN_LOOKUP_ENDPOINT.format(domain=domain))

    def ip_lookup(self, ip_address: str) -> dict:
        return self.make_json_request(method="GET", url=IP_ENDPOINT.format(ip_address=ip_address))

    def make_request(self, method: str, url: str, headers: dict = None) -> requests.Response:
        try:
            response = requests.request(method=method, url=url, headers=headers)

            if response.status_code == 400:
                self._logger.info(f"[API ERROR] Code: {response.status_code}\n")
                raise PluginException(
                    cause="The server is unable to process the request.",
                    assistance="Verify your plugin input is correct and not malformed and try again. "
                    "If the issue persists, please contact support.",
                    data=response.text,
                )
            if response.status_code == 403:
                self._logger.info(f"[API ERROR] Code: {response.status_code}\n")
                raise PluginException(
                    cause="Operation is not allowed.",
                    assistance="Please verify inputs and if the issue persists, contact support.",
                    data=response.text,
                )
            if response.status_code == 404:
                self._logger.info(f"[API ERROR] Code: {response.status_code}\n")
                raise PluginException(
                    cause="Resource not found.",
                    assistance="Verify your plugin input is correct and not malformed and try again. "
                    "If the issue persists, please contact support.",
                    data=response.text,
                )
            if 400 <= response.status_code < 500:
                self._logger.info(f"[API ERROR] Code: {response.status_code}\n")
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code >= 500:
                self._logger.info(f"[API ERROR] Code: {response.status_code}\n")
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
            if 200 <= response.status_code <= 302:
                self._logger.info(f"[API SUCCESS] Code: {response.status_code}\n")
                return response

            self._logger.info(f"[API ERROR] PluginException: UNKNOWN\n")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        except requests.exceptions.HTTPError as e:
            self._logger.info(f"[API ERROR] PluginException: UNKNOWN\n")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def make_json_request(self, method: str, url: str, headers: dict = None) -> dict:
        try:
            response = self.make_request(method=method, url=url, headers=headers)
            return response.json()

        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
