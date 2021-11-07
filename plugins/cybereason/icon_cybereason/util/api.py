import insightconnect_plugin_runtime
import requests
import validators
import re
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

    def isolate_machines(self, pylum_ids: [str], malop_id: str = None) -> dict:
        return self.send_request(
            "POST",
            "/rest/monitor/global/commands/isolate",
            payload={"malopId": malop_id, "pylumIds": pylum_ids},
        )

    def un_isolate_machines(self, pylum_ids: [str], malop_id: str = None) -> dict:
        return self.send_request(
            "POST",
            "/rest/monitor/global/commands/un-isolate",
            payload={"malopId": malop_id, "pylumIds": pylum_ids},
        )

    def remediate(self, initiator_user_name: str, actions_by_machine: dict, malop_id: str = None) -> dict:
        payload = {
            "initiatorUserName": initiator_user_name,
            "actionsByMachine": actions_by_machine,
        }
        if malop_id:
            payload["malopId"] = malop_id

        return self.send_request(
            "POST",
            "/rest/remediate",
            payload=payload,
        )

    def file_search(self, server_filter: dict, file_filter: dict) -> dict:
        if not file_filter:
            raise PluginException(cause="File filter shouldn't be empty.", assistance="Please check this input.")

        return self.send_request(
            "POST",
            "/rest/sensors/action/fileSearch",
            payload={"filters": server_filter, "fileFilters": file_filter},
        )

    def get_sensor_details(self, identifier: str) -> dict:
        sensors = self.send_request("POST", "/rest/sensors/query", payload=self.generate_sensor_filter(identifier))

        if sensors.get("totalResults") == 0:
            raise PluginException(
                cause=f"No sensors found using identifier: {identifier}.",
                assistance="Please validate inputs and try again.",
            )
        if sensors.get("totalResults") > 1:
            raise PluginException(
                cause=f"Multiple sensors found using identifier: {identifier}.",
                assistance="Please provide a unique identifier and try again.",
            )

        return sensors.get("sensors")[0]

    def get_malop(self, malop_guid: str) -> dict:
        try:
            return self.send_request(
                "POST",
                "/rest/crimes/unified",
                payload={
                    "totalResultLimit": 10000,
                    "perGroupLimit": 10000,
                    "templateContext": "OVERVIEW",
                    "queryPath": [{"requestedType": "MalopProcess", "guidList": [malop_guid], "result": True}],
                },
            )["data"]["resultIdToElementDataMap"][malop_guid]
        except KeyError:
            raise PluginException(
                cause=f"Unable to retrieve Malop information for {malop_guid}.",
                assistance="Please ensure that provided Malop GUID is valid and try again.",
            )

    def get_malop_feature_details(self, malop_guid: str, feature_name: str) -> dict:
        response = self.send_request(
            "POST",
            "/rest/visualsearch/query/simple",
            payload={
                "totalResultLimit": 10000,
                "perGroupLimit": 10000,
                "templateContext": "CUSTOM",
                "queryPath": [
                    {
                        "requestedType": "MalopProcess",
                        "guidList": [malop_guid],
                        "connectionFeature": {"elementInstanceType": "MalopProcess", "featureName": feature_name},
                    },
                    {"requestedType": "Autorun", "isResult": True},
                ],
                "customFields": ["name", "ownerMachine"],
            },
        )
        try:
            return response["data"]["resultIdToElementDataMap"]

        except KeyError:
            raise PluginException(
                cause=f"Unable to retrieve detailed Malop information for {malop_guid}.",
                assistance="Please ensure that provided Malop ID is valid and try again.",
            )

    def get_visual_search(self, requestedType: str, filters: list, customFields: list) -> dict:
        try:
            return self.send_request(
                "POST",
                "/rest/visualsearch/query/simple",
                payload={
                    "queryPath": [{"requestedType": requestedType, "filters": filters, "isResult": True}],
                    "totalResultLimit": 1000,
                    "perGroupLimit": 100,
                    "perFeatureLimit": 100,
                    "templateContext": "SPECIFIC",
                    "queryTimeout": 120000,
                    "customFields": customFields,
                },
            )["data"]["resultIdToElementDataMap"]
        except KeyError:
            raise PluginException(
                cause="No results found.",
                assistance="No Visual Search results returned for the provided filter.",
            )

    def send_request(self, method: str, path: str, params: dict = None, payload: dict = None) -> dict:
        try:
            response = self.session.request(
                method.upper(),
                urljoin(self.base_url, path),
                params=params,
                json=payload,
                headers=self.headers,
            )

            if response.status_code == 401:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=response.text)
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
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

            if 200 <= response.status_code < 300:
                # Cybereason will return a Login page with a 200 status code if creds are incorrect
                # Therefore, check if the response is JSON-decodable (login page is not JSON)
                try:
                    json_response = response.json()
                except json.decoder.JSONDecodeError:
                    raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)

                return insightconnect_plugin_runtime.helper.clean(json_response)

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
        value = json.loads('{"' + server_filter[0] + '":' + server_filter[1].replace("'", '"') + "}")

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

    @staticmethod
    def generate_sensor_filter(identifier: str) -> dict:
        sensor_filter = {"filters": [{"operator": "ContainsIgnoreCase", "values": [identifier]}]}

        if validators.ipv4(identifier):
            sensor_filter["filters"][0]["fieldName"] = "internalIpAddress"
        elif re.match(r"^(-?\d{9,10}\.-?\d{19})$", identifier):
            sensor_filter["filters"][0]["fieldName"] = "guid"
        else:
            sensor_filter["filters"][0]["fieldName"] = "machineName"

        return sensor_filter

    @staticmethod
    def get_machine_targets(results: str, machine_guid: str) -> list:
        target_ids = []

        for key, value in results.items():
            try:
                for i in value["elementValues"]["ownerMachine"]["elementValues"]:
                    if machine_guid in i["guid"]:
                        target_ids.append(key)
            # Doing a KeyError check, as during testing `elementValues`
            # list was occasionally returned as an empty dictionary
            except KeyError:
                pass

        if not target_ids:
            raise PluginException(
                cause="No targets found for this machine in the Malop provided.",
                assistance=f"No remediation targets for machine: {machine_guid}, in the provided Malop.",
            )

        return target_ids
