from requests import request
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import Dict, Any


class InfobloxConnection:
    def __init__(self, host, api_version, user, password, ssl_verify, logger):
        self.host = host
        self.api_version = api_version
        self.user = user
        self.password = password
        self.ssl_verify = ssl_verify
        self.logger = logger

        self._validate_connection()

    def _validate_connection(self) -> None:
        self.logger.info("Validate: Testing Infoblox credentials")
        try:
            self._call_api("GET", "", params={"_schema": 1})
        except Exception:
            raise PluginException(
                cause="InfobloxConnection: Failed to connect to host. ",
                assistance="Please make sure that the credentials and host are correct",
            )

        self.logger.info("Validate: Successfully connected to Infoblox instance")

    def add_host(self, host: str) -> list:
        self.logger.info(f"AddHost: Creating new host: {host}")
        return self._call_api("POST", "record:host", json=host)

    def get_host(self, ref) -> list:
        ref_url = self._format_url_with_ref("record:host", ref)
        self.logger.info(f"GetHost: Getting host: {ref_url}")
        return self._call_api("GET", ref_url, params={"_return_fields+": "aliases,extattrs"})

    def modify_host(self, ref: str, updated_host: str) -> list:
        ref_url = self._format_url_with_ref("record:host", ref)
        self.logger.info(f"ModifyHost: Updating host: {ref_url}")
        return self._call_api("PUT", ref_url, json=updated_host)

    def delete_host(self, ref: str) -> list:
        ref_url = self._format_url_with_ref("record:host", ref)
        self.logger.info(f"DeleteHost: Deleting host: {ref_url}")
        return self._call_api("DELETE", ref_url)

    def add_fixed_address(self, address: str) -> list:
        self.logger.info(f"AddFixedAddress: Adding address: {address}")
        return self._call_api("POST", "fixedaddress", json=address)

    def search_by_name(self, name_pattern: str) -> list:
        self.logger.info(f"SearchByName: Searching for {name_pattern}")
        return self._call_api("GET", "record:host", params={"name~": name_pattern})

    def search_by_ip(self, ip: str) -> list:
        self.logger.info(f"SearchByIP: Searching for {ip}")
        return self._call_api("GET", "ipv4address", params={"ip_address": ip, "status": "USED"})

    def search_by_mac(self, mac: str) -> list:
        self.logger.info(f"SearchByMAC: Searching for {mac}")
        return self._call_api("GET", "fixedaddress", params={"mac": mac, "_return_fields+": "mac"})

    @staticmethod
    def _format_url_with_ref(base_url, ref):
        base_url = base_url.rstrip("/") + "/"
        if not ref.startswith(base_url):
            ref = base_url + ref
        return ref

    def _call_api(self, method: str, url: str, json: str = None, params: Dict[str, Any] = None) -> list:
        response = None

        if not params:
            params = {}
        params["_return_as_object"] = 1

        api_url = f"{self.host}/wapi/v{self.api_version}/{url}"
        self.logger.info(f"CallAPI: Calling {api_url} (json: {json}, params: {params})")

        try:
            response = request(
                method,
                api_url,
                json=json,
                params=params,
                auth=(self.user, self.password),
                verify=self.ssl_verify,
            )
            response.raise_for_status()
        except Exception:
            message = f"Requests: Failed to call {api_url} (status {response.status_code}):\n{response.json()}"
            self.logger.error(message)
            raise PluginException(
                cause=f"Requests: Failed to call {api_url} (status {response.status_code})",
                assistance=f"{response.json()}",
            )

        return response.json()["result"]
