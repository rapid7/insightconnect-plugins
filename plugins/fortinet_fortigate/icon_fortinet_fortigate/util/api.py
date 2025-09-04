import requests
from requests import Session
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_fortinet_fortigate.util.util import Helpers
import json


class FortigateAPI:
    def __init__(self, host, api_key, logger, ssl_verify=False):
        self.host = host
        self.logger = logger
        self.ssl_verify = ssl_verify
        self.session = Session()
        self.helper = Helpers(self.logger)
        self.headers = {"Authorization": f"Bearer {api_key}", "Content-type": "application/json"}

    def call_api(
        self, path: str, method: str = "GET", params: dict = None, json_data: dict = None
    ) -> requests.Response:
        try:
            response = self.session.request(
                method=method.upper(),
                url=f"https://{self.host}/api/v2/cmdb/{path}",
                verify=self.ssl_verify,
                json=json_data,
                params=params,
                headers=self.headers,
            )
            self.helper.http_errors(response.text, response.status_code)
            if response.status_code > 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

    def create_address_object(self, name: str, host: str, address_type: str):
        endpoint = "firewall/address"
        payload = {"name": name, "type": address_type}
        if address_type == "ipmask":
            payload["subnet"] = host
        elif address_type == "fqdn":
            payload["fqdn"] = host
        else:
            payload["ip6"] = host
            endpoint = "firewall/address6"
        return self.call_api(endpoint, "POST", json_data=payload)

    def delete_address_object(self, endpoint: str):
        return self.call_api(endpoint, "DELETE")

    def get_address_group(self, address_group_name: str, is_ipv6: bool):
        endpoint = "firewall/addrgrp"

        if is_ipv6:
            endpoint = "firewall/addrgrp6"

        result = self.call_api(
            path=endpoint,
            params={
                "filter": f"name=@{address_group_name}",
            },
        )

        groups = result.get("results")
        if not len(groups) > 0:
            raise PluginException(
                cause=f"Could not find address group '{address_group_name}' in results.\n",
                assistance=f"Please make sure the group '{address_group_name}' exists.\n",
                data=result,
            )

        return groups[0]

    def get_address_object(self, address_name: str):
        # encode '/' characters in address name
        encoded_address_name = self.helper.url_encode(address_name)
        try:
            response_ipv4 = self.call_api(path=f"firewall/address/{encoded_address_name}")
            if response_ipv4.get("http_status") == 200:
                return response_ipv4
        except PluginException:
            self.logger.info(f"The specified object {address_name} was not found in domain and IPv4 address objects.")

        response_ipv6 = self.call_api(path=f"firewall/address6/{encoded_address_name}")
        if response_ipv6.get("http_status") == 200:
            return response_ipv6

        raise PluginException(
            cause=f"Get address object failed. Address object '{address_name}' does not exists.\n",
            assistance="Contact support for assistance.",
            data=response_ipv6,
        )

    def get_address_objects(self, endpoint: str, params: dict):
        return self.call_api(endpoint, params=params)

    def get_policies(self, params: dict):
        return self.call_api("firewall/policy", params=params)

    def modify_objects_in_group(self, endpoint: str, group: dict):
        return self.call_api(endpoint, "PUT", json_data=group)
