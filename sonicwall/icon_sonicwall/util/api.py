import requests
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from collections import OrderedDict


class SonicWallAPI:
    def __init__(self, username, password, url, verify_ssl, port, logger):
        self.url = url + ":" + str(port) + "/api/sonicos/"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.username = username
        self.password = password

    def login(self):
        self._call_api("post", "auth", auth=(self.username, self.password))

    def logout(self):
        self._call_api("DELETE", "auth", auth=(self.username, self.password))

    def get_object_type(self, name):
        self.login()
        for object_type in ["fqdn", "mac", "ipv6", "ipv4"]:
            try:
                if self._call_api("get", f"address-objects/{object_type}/name/{name}"):
                    return object_type
            except PluginException as _:
                continue

        self.logout()
        raise PluginException(cause="The address object does not exist in SonicWall.",
                              assistance="Please enter valid names and try again.")

    def get_group_type(self, name):
        try:
            if self._make_request("get", f"address-groups/ipv4/name/{name}"):
                return "ipv4"
        except PluginException as _:
            pass

        try:
            if self._make_request("get", f"address-groups/ipv6/name/{name}"):
                return "ipv6"
        except PluginException as _:
            pass

        raise PluginException(cause="The address group does not exist in SonicWall.",
                              assistance="Please enter valid names and try again.")

    def add_address_object_to_group(self, group_type, group_name, payload):
        return self._make_request("put", f"address-groups/{group_type}/name/{group_name}", json_data=payload)

    def _make_request(self, method, path, json_data=None):
        self.login()
        try:
            response = self._call_api(method, path, json_data)
            self._call_api("POST", "config/pending")
        except PluginException as e:
            raise PluginException(cause=e.cause, assistance=e.assistance, data=e.data)
        finally:
            self.logout()

        return response

    def _call_api(self, method, path, json_data=None, auth=None):
        response = {"text": ""}
        headers = OrderedDict([
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('charset', 'UTF-8')
        ])
        try:
            response = requests.request(method, self.url + path,
                                        json=json_data,
                                        auth=auth,
                                        headers=headers,
                                        verify=self.verify_ssl)

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)
            if response.status_code >= 400:
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to SonicWall API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
