import json
import requests
from komand.exceptions import PluginException
import datetime


class CiscoFirePowerApi:
    def __init__(self, username: str, password: str, url: str, verify_ssl: bool, port: int, domain: str,
                 logger: object):
        self.url = url.rstrip('/').replace('/api', '') + '/api/'
        self.verify_ssl = verify_ssl
        self.username = username
        self.password = password
        self.domain = domain
        self.logger = logger
        self.domain_uuid = self.find_domain_uuid()

    def create_address_object(self, object_type: str, payload: dict) -> dict:
        if object_type == "ipv4" or object_type == "ipv6":
            endpoint = "hosts"
        if object_type == "fqdn":
            endpoint = "fqdns"
        if object_type == "cidr":
            endpoint = "networks"

        return self._call_api("POST", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}", json_data=payload)

    def get_address_objects(self, endpoint: str) -> dict:
        return self._call_api("GET", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}")

    def delete_address_object(self, endpoint: str, object_id: str) -> dict:
        return self._call_api("DELETE", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}/{object_id}")

    def _call_api(self, method: str, path: str, json_data: dict = None, params: dict = None):
        response = {"text": ""}

        headers = {
            "Content-Type": "application/json",
            "X-auth-access-token": self.generate_token()
        }

        try:
            response = requests.request(
                method, self.url + path,
                json=json_data,
                params=params,
                headers=headers,
                verify=self.verify_ssl
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND)
            if response.status_code >= 400:
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
            if response.status_code == 204:
                return {}
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Cisco FirePower API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

    def generate_token(self) -> str:
        response = requests.post(f"{self.url}fmc_platform/v1/auth/generatetoken",
                                    headers={"Content-Type": "application/json"},
                                    auth=(self.username, self.password),
                                    verify=self.verify_ssl)

        if not response.status_code == 204:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        return response.headers.get('X-auth-access-token')

    def find_domain_uuid(self) -> str:
        domains = self._call_api("GET", "fmc_platform/v1/info/domain").get('items')

        for domain in domains:
            if domain.get('name') == self.domain:
                return domain.get('uuid')
        else:
            raise PluginException(cause="Unable to find Domain provided.",
                                  assistance="Please validate the domain name provided and try again.")
