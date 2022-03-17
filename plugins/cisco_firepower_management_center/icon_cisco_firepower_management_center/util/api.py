import json
import requests
from insightconnect_plugin_runtime.exceptions import PluginException


class CiscoFirePowerApi:
    def __init__(
        self,
        username: str,
        password: str,
        url: str,
        verify_ssl: bool,
        port: int,
        domain: str,
        logger,
    ):
        self.url = url.rstrip("/").replace("/api", "") + "/api/"
        self.verify_ssl = verify_ssl
        self.username = username
        self.password = password
        self.domain = domain
        self.port = port
        self.logger = logger
        self.domain_uuid = self.find_domain_uuid()

    def create_address_object(self, object_type: str, payload: dict) -> dict:
        if object_type in ["ipv4", "ipv6"]:
            endpoint = "hosts"
        elif object_type == "fqdn":
            endpoint = "fqdns"
        else:
            endpoint = "networks"

        return self._call_api("POST", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}", json_data=payload)

    def get_address_objects(self, endpoint: str) -> dict:
        return self._call_api("GET", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}")

    def get_address_object(self, endpoint: str, object_id: str) -> dict:
        return self._call_api("GET", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}/{object_id}")

    def delete_address_object(self, endpoint: str, object_id: str) -> dict:
        return self._call_api("DELETE", f"fmc_config/v1/domain/{self.domain_uuid}/object/{endpoint}/{object_id}")

    def get_network_addresses(self) -> list:
        return self.run_with_pages(f"fmc_config/v1/domain/{self.domain_uuid}/object/networkaddresses", expanded=True)

    def find_network_object(self, address_object: str) -> dict:
        for item in self.get_network_addresses():
            if item.get("name") == address_object or item.get("value") == address_object:
                return item

        return {}

    def get_network_address(self, network_address_name: str) -> dict:
        for item in self.get_network_addresses():
            if item.get("name") == network_address_name or item.get("objectId") == network_address_name:
                return item

        return {}

    def get_address_groups(self) -> list:
        return self.run_with_pages(f"fmc_config/v1/domain/{self.domain_uuid}/object/networkgroups", expanded=True)

    def get_address_group(self, group_name: str) -> dict:
        for item in self.get_address_groups():
            if item.get("name") == group_name:
                return item

        return {}

    def get_server_version(self) -> list:
        return self._call_api("GET", "fmc_platform/v1/info/serverversion")

    def update_address_group(self, payload):
        return self._call_api(
            "PUT",
            f"fmc_config/v1/domain/{self.domain_uuid}/object/networkgroups/{payload.get('id')}",
            json_data=payload,
        )

    def run_with_pages(self, path: str, expanded: bool = False) -> list:
        objects = []
        limit = 100
        for page in range(0, 9999):
            params = {"limit": limit, "offset": page * limit}
            if expanded:
                params["expanded"] = True
            response = self._call_api("GET", path, params=params)
            objects.extend(response.get("items", []))

            if (page + 1) * limit >= response.get("paging", {}).get("pages", 0):
                break

        return objects

    def _call_api(self, method: str, path: str, json_data: dict = None, params: dict = None):
        response = {"text": ""}

        headers = {"Content-Type": "application/json", "X-auth-access-token": self._generate_token()}

        try:
            response = requests.request(
                method,
                self.url + path,
                json=json_data,
                params=params,
                headers=headers,
                verify=self.verify_ssl,
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

    def _generate_token(self) -> str:
        response = requests.post(
            f"{self.url}fmc_platform/v1/auth/generatetoken",
            headers={"Content-Type": "application/json"},
            auth=(self.username, self.password),
            verify=self.verify_ssl,
        )

        if not response.status_code == 204:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        return response.headers.get("X-auth-access-token")

    def find_domain_uuid(self) -> str:
        domains = self._call_api("GET", "fmc_platform/v1/info/domain").get("items")

        for domain in domains:
            if domain.get("name") == self.domain:
                return domain.get("uuid")
        raise PluginException(
            cause="Unable to find Domain provided.",
            assistance="Please validate the domain name provided and try again.",
        )
