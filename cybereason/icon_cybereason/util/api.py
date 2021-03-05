import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import json
from logging import Logger
from typing import Optional


class CybereasonAPI:
    def __init__(self, hostname: str, port: int, username: str, password: str, logger: Logger):
        self.base_url = f"https://{hostname}:{port}/"
        self.username = username
        self.password = password
        self.headers = {"Content-Type": "application/json"}
        self.session = requests.session()
        self.logger = logger

    def connect(self):
        login_response = self.session.post(
            f"{self.base_url}/login.html",
            data={"username": self.username, "password": self.password},
            verify=True,
        )

        if login_response.status_code not in range(200, 299):
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE,
                data="There is a problem connecting to Cybereason. Please check your credentials and permissions.",
            )

    def file_search(self, server_filter: dict, file_filter: dict):
        api_response = self.session.request(
            "POST",
            f"{self.base_url}/rest/sensors/action/fileSearch",
            json={"filters": server_filter, "fileFilters": file_filter},
            headers=self.headers,
        )

        if api_response.status_code >= 400:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=api_response.text)
        if 200 <= api_response.status_code < 300:
            return insightconnect_plugin_runtime.helper.clean(json.loads(api_response.content))

        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=api_response.text)

    @staticmethod
    def parse_server_filter(server_filter: Optional[str] = None):
        if not server_filter:
            return []

        server_filter = server_filter.split(":")
        value = json.loads(
            '{"' + server_filter[0] + '":' + server_filter[1].replace("'", '"') + "}"
        )

        return [
            {
                "fieldName": server_filter[0],
                "operator": "ContainsIgnoreCase",
                "values": value[server_filter[0]],
            }
        ]

    @staticmethod
    def parse_file_filter(file_filter: str):
        file_filter = file_filter.split(":")
        value = json.loads('{"' + file_filter[0] + '":' + file_filter[1].replace("'", '"') + "}")
        command = file_filter[0].split(" ")
        file_name = command[0]
        operator = command[1]

        return [{"fieldName": file_name, "operator": operator, "values": value[file_filter[0]]}]
