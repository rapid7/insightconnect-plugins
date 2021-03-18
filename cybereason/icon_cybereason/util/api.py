import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import json
from logging import Logger
from typing import Optional
from urllib.parse import urljoin


class CybereasonAPI:
    def __init__(self, hostname: str, port: int, username: str, password: str, logger: Logger):
        self.base_url = f"https://{hostname}:{port}"
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

    def isolate_machines(self, malop_id: str, pylum_ids: [str]) -> dict:
        return self.send_request(
            "POST",
            "/rest/monitor/global/commands/isolate",
            payload={"malopId": malop_id, "pylumIds": pylum_ids},
        )

    def remediate(self, initiator_user_name: str, actions_by_machine: dict) -> dict:
        return self.send_request(
            "POST",
            "/rest/remediate",
            payload={
                "initiatorUserName": initiator_user_name,
                "actionsByMachine": actions_by_machine,
            },
        )

    def file_search(self, server_filter: dict, file_filter: dict) -> dict:
        if not file_filter:
            raise PluginException(
                cause="File filter shouldn't be empty.", assistance="Please check this input."
            )

        return self.send_request(
            "POST",
            "/rest/sensors/action/fileSearch",
            payload={"filters": server_filter, "fileFilters": file_filter},
        )

    def send_request(
        self, method: str, path: str, params: dict = None, payload: dict = None
    ) -> dict:
        try:
            response = self.session.request(
                method.upper(),
                urljoin(self.base_url, path),
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                raise PluginException(
                    preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text
                )
            if response.status_code == 403:
                raise PluginException(preset=PluginException.Preset.API_KEY, data=response.text)
            if response.status_code == 404:
                raise PluginException(preset=PluginException.Preset.NOT_FOUND, data=response.text)
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(
                    preset=PluginException.Preset.SERVER_ERROR, data=response.text
                )

            if 200 <= response.status_code < 300:
                return insightconnect_plugin_runtime.helper.clean(json.loads(response.content))

            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)
        except json.decoder.JSONDecodeError as e:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=e)
        except requests.exceptions.HTTPError as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

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
