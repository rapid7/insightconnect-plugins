import json
import requests
from komand.exceptions import PluginException


class CiscoFirePowerMC:
    def __init__(self, username: str, password: str, url: str, user_agent: str, verify_ssl: bool, port: int,
                 logger: object):
        self.url = url + ":" + str(port) + "/api/"
        self.verify_ssl = verify_ssl
        self.logger = logger
        self.username = username
        self.password = password
        self.user_agent = user_agent

    def update_group(self, object_id: str, group: str, all_members: list):
        return self._call_api(
            "PUT",
            f"objects/networkobjectgroups/{object_id}",
            json_data={
                "name": group,
                "members": all_members
            }
        )

    def add_to_group(self, object_id: str, group: str, all_members: list):
        return self._call_api(
            "PUT",
            f"objects/networkobjectgroups/{object_id}",
            json_data={
                "name": group,
                "members": all_members
            }
        )

    def get_groups(self):
        return self.run_with_pages("objects/networkobjectgroups")

    def get_group(self, group_name: str):
        for item in self.get_groups():
            if item.get("name") == group_name or item.get("objectId") == group_name:
                return item

        return {}

    def get_objects(self):
        return self.run_with_pages("objects/networkobjects")

    def get_object(self, address_object_name: str):
        for item in self.get_objects():
            if item.get("name") == address_object_name or item.get("objectId") == address_object_name:
                return item

        return {}

    def delete_address_object(self, object_id: str):
        return self._call_api(
            "DELETE",
            f"objects/networkobjects/{object_id}"
        )

    def run_with_pages(self, path):
        objects = []
        limit = 100
        for page in range(0, 9999):
            response = self._call_api(
                "GET",
                path,
                params={
                    "limit": limit,
                    "offset": page * limit
                }
            )
            objects.extend(response.get("items", []))

            if (page + 1) * limit >= response.get("rangeInfo", {}).get("total", 0):
                break

        return objects

    def get_clock(self):
        return self._call_api("GET", "monitoring/clock")

    def _call_api(self, method: str, path: str, json_data: dict = None, params: dict = None):
        response = {"text": ""}
        headers = OrderedDict([
            ('Content-Type', 'application/json'),
            ('User-Agent', self.user_agent)
        ])

        try:
            response = requests.request(
                method, self.url + path,
                json=json_data,
                params=params,
                auth=(self.username, self.password),
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
                response_data = response.text
                raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response_data)
            if response.status_code == 204:
                return {}
            if 200 <= response.status_code < 300:
                return response.json()

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            self.logger.info(f"Invalid JSON: {e}")
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
        except requests.exceptions.HTTPError as e:
            self.logger.info(f"Call to Cisco ASA API failed: {e}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
