import json
import requests
from collections import OrderedDict
from insightconnect_plugin_runtime.exceptions import PluginException


class CiscoAsaAPI:
    def __init__(self, username, password, url, verify_ssl, port, logger):
        self.url = url + ":" + str(port) + "/api/"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.username = username
        self.password = password

    def get_groups(self):
        return self._call_api("GET", "objects/networkobjectgroups")

    def get_group(self, group_name):
        groups = self.get_groups()
        for item in groups.get("items", []):
            if item.get("name") == group_name or item.get("objectId") == group_name:
                return item

        return {}

    def get_objects(self):
        return self._call_api("GET", "objects/networkobjects")

    def get_clock(self):
        return self._call_api("GET", "monitoring/clock")

    def _call_api(self, method, path, json_data=None):
        response = {"text": ""}
        headers = OrderedDict([
            ('Content-Type', 'application/json'),
            ('User-Agent', 'test-user-agent')
        ])

        try:
            response = requests.request(
                method, self.url + path,
                json=json_data,
                auth=(self.username, self.password),
                headers=headers,
                verify=self.verify_ssl
            )

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
            self.logger.info(f"Call to Cisco ASA API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
