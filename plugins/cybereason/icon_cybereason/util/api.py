import insightconnect_plugin_runtime
import requests
import validators
import re
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
import json
from logging import Logger
from typing import Optional, Dict, Any, Union, List
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

    def isolate_machines(self, pylum_ids: [str], malop_id: str = None) -> Dict[str, Any]:
        return self.send_request(
            "POST",
            "/rest/monitor/global/commands/isolate",
            payload={"malopId": malop_id, "pylumIds": pylum_ids},
        )

    def un_isolate_machines(self, pylum_ids: [str], malop_id: str = None) -> Dict[str, Any]:
        return self.send_request(
            "POST",
            "/rest/monitor/global/commands/un-isolate",
            payload={"malopId": malop_id, "pylumIds": pylum_ids},
        )

    def remediate(self, initiator_user_name: str, actions_by_machine: Dict, malop_id: str = None) -> Dict[str, Any]:
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

    def file_search(self, server_filter: Dict[str, Any], file_filter: Dict[str, Any]) -> Dict[str, Any]:
        return self.send_request(
            "POST",
            "/rest/sensors/action/fileSearch",
            payload={"filters": server_filter, "fileFilters": file_filter},
        )

    def get_sensors(self, limit: int, offset: int, identifier: str) -> Dict[str, Any]:
        field_name = self.which_filter(identifier)
        return self.send_request(
            "POST",
            "/rest/sensors/query",
            payload={
                "limit": limit,
                "offset": offset,
                "filters": [{"fieldName": field_name, "operator": "ContainsIgnoreCase", "values": [identifier]}],
            },
        )

    def get_sensor_details(self, identifier: str) -> Dict[str, Any]:
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

    def archive_sensor(self, sensor_ids: List[str], argument: str) -> Dict[str, Any]:
        return self.send_request(
            "POST", "/rest/sensors/action/archive", payload={"sensorsIds": sensor_ids, "argument": argument}
        )

    def get_malop(self, malop_guid: str) -> Dict[str, Any]:
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

    def get_malop_feature_details(self, malop_guid: str, feature_name: str) -> Dict[str, Any]:
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

    def get_visual_search(
        self, requested_type: str, filters: List[Dict[str, Union[str, List[str]]]], custom_fields: List[str]
    ) -> Dict[str, Any]:
        try:
            return self.send_request(
                "POST",
                "/rest/visualsearch/query/simple",
                payload={
                    "queryPath": [{"requestedType": requested_type, "filters": filters, "isResult": True}],
                    "totalResultLimit": 1000,
                    "perGroupLimit": 100,
                    "perFeatureLimit": 100,
                    "templateContext": "SPECIFIC",
                    "queryTimeout": 120000,
                    "customFields": custom_fields,
                },
            )["data"]["resultIdToElementDataMap"]
        except KeyError:
            raise PluginException(
                cause="No results found.",
                assistance="No Visual Search results returned for the provided filter.",
            )

    @staticmethod
    def check_status_codes(status_code: int, response: Any) -> Union[Dict[str, Any], None]:
        if status_code == 401:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)
        if status_code == 403:
            raise PluginException(preset=PluginException.Preset.API_KEY)
        if status_code == 404:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
        if status_code == 204:
            raise PluginException(preset=PluginException.Preset.NOT_FOUND)
        if 200 <= status_code < 300:
            # Cybereason will return a Login page with a 200 status code if creds are incorrect
            # Therefore, check if the response is JSON-decodable (login page is not JSON)
            try:
                json_response = response.json()
            except json.decoder.JSONDecodeError:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD)

            return insightconnect_plugin_runtime.helper.clean(json_response)
        else:
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

    def send_request(self, method: str, path: str, params: Dict = None, payload: Dict = None) -> Dict[str, Any]:
        response = self.session.request(
            method.upper(),
            urljoin(self.base_url, path),
            params=params,
            json=payload,
            headers=self.headers,
        )
        return self.check_status_codes(response.status_code, response)

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
    def which_filter(identifier: str) -> str:
        if validators.ipv4(identifier):
            return "internalIpAddress"
        elif re.match(r"^(-?\d{9,10}\.-?\d{19})$", identifier):
            return "guid"
        else:
            return "machineName"

    @staticmethod
    def generate_sensor_filter(identifier: str) -> Dict[str, str]:
        sensor_filter = {"filters": [{"operator": "ContainsIgnoreCase", "values": [identifier]}]}

        if validators.ipv4(identifier):
            sensor_filter["filters"][0]["fieldName"] = "internalIpAddress"
        elif re.match(r"^(-?\d{9,10}\.-?\d{19})$", identifier):
            sensor_filter["filters"][0]["fieldName"] = "guid"
        else:
            sensor_filter["filters"][0]["fieldName"] = "machineName"

        return sensor_filter

    @staticmethod
    def get_machine_targets(results: Dict[str, Any], machine_guid: str) -> List[str]:
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

    def get_file_guids(self, files: List[str], machine_name: str, quarantine: bool) -> List[str]:
        filters = [
            {"facetName": "elementDisplayName", "filterType": "ContainsIgnoreCase", "values": files},
            {"facetName": "ownerMachine", "filterType": "ContainsIgnoreCase", "values": [machine_name]},
        ]

        if quarantine:
            results = self.get_visual_search(requested_type="File", filters=filters, custom_fields=["ownerMachine"])
        else:
            results = self.get_visual_search(
                requested_type="QuarantineFile", filters=filters, custom_fields=["quarantineFile"]
            )

        if quarantine:
            return list(results.keys())

        quarantined_file_guids = []
        for key in results.keys():
            try:
                quarantined_files = results[key]["elementValues"]["quarantineFile"]["elementValues"]
            except KeyError:
                continue
            for file in quarantined_files:
                quarantined_file_guids.append(file.get("guid"))

        return quarantined_file_guids

    @staticmethod
    def get_files_in_malop(malop_data: Dict[str, Any]) -> List[str]:
        try:
            element_values = malop_data["elementValues"]["primaryRootCauseElements"]["elementValues"]
        except KeyError:
            raise PluginException(
                cause="No root cause elements found for this Malop.",
                assistance="Please provide a Malop GUID of a Malop that has files involved.",
            )

        file_names = [element.get("name") for element in element_values if element.get("elementType") == "File"]

        if file_names:
            return file_names

        raise PluginException(
            cause="No files related to this Malop found.",
            assistance="Please provide a Malop GUID of a Malop that has files involved.",
        )

    @staticmethod
    def check_machine_in_malop(malop_data: Dict[str, Any], machine_guid: str, malop_id: str):
        try:
            element_values = malop_data["elementValues"]["affectedMachines"]["elementValues"]
        except KeyError:
            raise PluginException(
                cause="No affected machines found for this Malop.",
                assistance="Please provide a Malop GUID of a Malop that has machines involved.",
            )

        if not [machine for machine in element_values if machine.get("guid") == machine_guid]:
            raise PluginException(
                cause="Sensor provided is not related to the Malop ID Provided.",
                assistance=f"Make sure the provided sensor is involved in the Malop: {malop_id}.",
            )

    @staticmethod
    def get_list_of_actions(quarantine: bool, file_guids: List[str]) -> List[Dict[str, str]]:
        if quarantine:
            action_type = "QUARANTINE_FILE"
        else:
            action_type = "UNQUARANTINE_FILE"
        actions = []
        for guid in file_guids:
            actions.append({"targetId": guid, "actionType": action_type})

        if not actions:
            raise PluginException(
                cause="No actions to perform.",
                assistance="This can happen because there are no quarantined files in the provided Malop.",
            )
        return actions
