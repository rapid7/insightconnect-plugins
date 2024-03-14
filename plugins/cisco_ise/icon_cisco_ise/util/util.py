import json
import re

import requests
from insightconnect_plugin_runtime.exceptions import PluginException


# Class from https://github.com/bobthebutcher/ise/blob/master/cream.py
class ERS(object):
    def __init__(self, ise_node, ers_user, ers_pass, verify, timeout=2):
        """
        Class to interact with Cisco ISE via the ERS API
        :param ise_node: IP Address of the primary admin ISE node
        :param ers_user: ERS username
        :param ers_pass: ERS password
        :param timeout: Query timeout
        """
        self.ise_node = ise_node
        self.user_name = ers_user
        self.user_pass = ers_pass

        self.url_base = f"https://{self.ise_node}:9060/ers"
        self.ise = requests.session()
        self.ise.auth = (self.user_name, self.user_pass)
        self.ise.verify = verify
        self.timeout = timeout
        self.ise.headers.update({"Connection": "keep_alive"})

        requests.packages.urllib3.disable_warnings()

    @staticmethod
    def _mac_test(mac: str) -> bool:
        if re.search(r"([0-9A-F]{2}[:]){5}([0-9A-F]){2}", mac.upper()) is not None:
            return True
        return False

    def get_endpoint_by_name(self, name):

        self.ise.headers.update({"ACCEPT": "application/json", "Content-Type": "application/json"})

        resp = self.ise.get(f"{self.url_base}/config/endpoint/name/{name}", verify=False)
        if resp.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if resp.reason == "Not Found":
            return "Not Found"
        found_endpoint = resp.json()
        return found_endpoint

    def get_endpoint_by_id(self, endpoint_id):

        self.ise.headers.update({"ACCEPT": "application/json", "Content-Type": "application/json"})

        resp = self.ise.get(f"{self.url_base}/config/endpoint/{endpoint_id}", verify=False)
        if resp.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if resp.reason == "Not Found":
            return "Not Found"
        found_endpoint = resp.json()
        return found_endpoint

    def get_endpoint(self):
        self.ise.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

        resp = self.ise.get(f"{self.url_base}/config/endpoint", verify=False)
        found_endpoint = resp.json()
        return found_endpoint

    def get_anc_endpoint_all(self) -> str:

        self.ise.headers.update({"ACCEPT": "application/json", "Content-Type": "application/json"})

        resp = self.ise.get(f"{self.url_base}/config/ancendpoint", verify=False)
        if resp.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if resp.reason == "Not Found":
            return "Not Found"

        found_endpoint = resp.json()
        return found_endpoint

    def get_anc_endpoint(self, endpoint_id="") -> str:

        self.ise.headers.update({"ACCEPT": "application/json", "Content-Type": "application/json"})

        resp = self.ise.get(f"{self.url_base}/config/ancendpoint/{endpoint_id}", verify=False)
        if resp.status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if resp.reason == "Not Found":
            return "Not Found"

        found_endpoint = resp.json()
        return found_endpoint

    def apply_anc_endpoint_mac(self, mac_address: str, policy: str):

        is_valid = ERS._mac_test(mac_address)

        if not is_valid:
            raise PluginException(
                cause=f"Mac Address is not valid {mac_address}. Must be in the form of AA:BB:CC:00:11:22"
            )
        else:
            self.ise.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

            payload = {
                "OperationAdditionalData": {
                    "additionalData": [
                        {"name": "macAddress", "value": mac_address},
                        {"name": "policyName", "value": policy},
                    ]
                }
            }
            payload = json.dumps(payload)

            resp = self.ise.put(f"{self.url_base}/config/ancendpoint/apply", data=payload, verify=False)
            if resp.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)

    def clean_anc_end_point(self, mac_address: str):

        is_valid = ERS._mac_test(mac_address)

        if not is_valid:
            raise PluginException(
                cause=f"Mac Address is not valid {mac_address}. Must be in the form of AA:BB:CC:00:11:22"
            )
        else:

            headers = {"Accept": "application/json", "Content-Type": "application/json"}
            payload = {"OperationAdditionalData": {"additionalData": [{"name": "macAddress", "value": mac_address}]}}
            payload = json.dumps(payload)

            resp = self.ise.put(
                f"{self.url_base}/config/ancendpoint/clear",
                data=payload,
                headers=headers,
                verify=False,
            )
            if resp.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
