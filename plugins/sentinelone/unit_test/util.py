import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from requests.exceptions import HTTPError
from komand_sentinelone.connection.connection import Connection
from komand_sentinelone.connection.schema import Input
from komand_sentinelone.util.constants import CONSOLE_USER_TYPE


class Util:
    mock_response_params = {}

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: "https://rapid7.com",
                Input.USER_TYPE: CONSOLE_USER_TYPE,
                Input.API_KEY: {"secretKey": "test"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_bytes(filename: str) -> bytes:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "rb") as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"
                Util.mock_response_params["args"] = args
                Util.mock_response_params["kwargs"] = kwargs

            def json(self):
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

            def raise_for_status(self):
                if self.status_code == 200:
                    return

                raise HTTPError("Bad response", response=self)

        params = kwargs.get("params")
        json_data = kwargs.get("json")

        if args[0] == "https://rapid7.com/web/api/v2.1/users/login/by-api-token":
            return MockResponse("get_token", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?networkInterfaceInet__contains=10.10.10.10":
            return MockResponse("none_in_location", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?networkInterfaceInet__contains=10.10.10.11":
            return MockResponse("good_response", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?externalIp__contains=10.10.10.10":
            return MockResponse("none_in_location", 404)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?externalIp__contains=10.10.10.11":
            return MockResponse("good_response", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/threats/add-to-blacklist":
            return MockResponse("agents_action", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.0/agents?computerName=hostname123":
            return MockResponse("apps_by_agent_ids", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?computerName=hostname123":
            return MockResponse("apps_by_agent_ids", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?computerName=hostname_na":
            return MockResponse("get_agent_details_na", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?computerName=hostname_fully_disabled":
            return MockResponse("get_agent_details_fully_disabled", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?computerName=hostname_partially_disabled":
            return MockResponse("get_agent_details_partially_disabled", 200)
        elif args[0] == "https://rapid7.com/web/api/v2.1/agents?computerName=hostname_disabled_error":
            return MockResponse("get_agent_details_disabled_error", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats/fetch-file":
            return MockResponse("threats_fetch_file", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/remote-scripts/execute":
            return MockResponse("remote_scripts_execute", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/activities":
            return MockResponse("activities_list", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/activities/types":
            return MockResponse("activities_types", 200)
        elif (
            args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/abort-scan"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/connect"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/decommission"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/disconnect"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/fetch-logs"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/initiate-scan"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/restart-machine"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/shutdown"
            or args[1] == "https://rapid7.com/web/api/v2.1/agents/actions/uninstall"
            or args[1] == "https://rapid7.com/web/api/v2.1/private/threats/ioc-create-threats"
            or args[1] == "https://rapid7.com/web/api/v2.0/threats/mark-as-threat"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/rollback-remediation"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/quarantine"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/kill"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/remediate"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/un-quarantine"
        ):
            if kwargs.get("json", {}).get("filter", {}).get("ids") == ["XYZABC"]:
                return MockResponse("", 400)
            return MockResponse("agents_action", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/agents/support-actions/reload":
            return MockResponse("agents_action", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/agents/summary":
            if params in [
                {},
                {"siteIds": "1234567890987654321"},
                {"siteIds": "1234567890987654321,1234567890987654322"},
                {"accountIds": "1234567890987654321"},
                {"accountIds": "1234567890987654321,1234567890987654321"},
                {"siteIds": "1234567890987654321", "accountIds": "1234567890987654321"},
            ]:
                return MockResponse("agents_summary", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/dv/query-status":
            if params == {"queryId": "q9679169d5a4607cc41a9100123456789"}:
                return MockResponse("get_query_status", 200)
            if params == {"queryId": "q9679169d5a4607cc41a9100987654321"}:
                return MockResponse("error", 404)
        elif args[1] == "https://rapid7.com/web/api/v2.1/dv/cancel-query":
            if json_data == {"queryId": "q9679169d5a4607cc41a9100123456789"}:
                return MockResponse("cancel_running_query", 200)
            if json_data == {"queryId": "q9679169d5a4607cc41a9100987654321"}:
                return MockResponse("cancel_running_query", 404)
        elif args[1] == "https://rapid7.com/web/api/v2.1/dv/init-query":
            if json_data == {
                "accountIds": ["1234567890"],
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "groupIds": ["1234567890"],
                "isVerbose": True,
                "limit": 20000,
                "query": "AgentName IS NOT EMPTY",
                "queryType": ["events"],
                "siteIds": ["1234567890"],
                "tenant": True,
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse("create_query", 200)
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "isVerbose": False,
                "limit": 100,
                "query": "AgentName IS NOT EMPTY",
                "tenant": False,
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse("create_query", 200)
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "limit": 100,
                "query": "AgentName IS NOT EMPTY",
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse("create_query", 200)
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "limit": 100,
                "query": "AgentName IS NOT EMPTYY",
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse("error", 400)
        elif args[1] == "https://rapid7.com/web/api/v2.1/agents/applications":
            return MockResponse("apps_by_agent_ids_success", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/sites":
            return MockResponse("sites", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/restrictions":
            return MockResponse("restrictions", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.0/threats" and params.get("limit") == 1000:
            if params.get("cursor") == "abcd":
                return MockResponse("get_threat_summary_page_2", 200)
            else:
                return MockResponse("get_threat_summary_page_1", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/accounts/name-available":
            if "NotAvailableName" in params.get("name"):
                return MockResponse("name_not_available", 200)
            return MockResponse("name_available", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats" and kwargs.get("params", {}).get("ids") == [
            "same_status_threat_id_1"
        ]:
            return MockResponse("threats_same_status", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts" and kwargs.get("params", {}).get(
            "ids"
        ) == ["same_status_alert_id_1"]:
            return MockResponse("alerts_same_status", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats" and kwargs.get("params", {}).get("ids") == [
            "non_existing_threat_id_1"
        ]:
            return MockResponse("threats_non_existing", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts" and kwargs.get("params", {}).get(
            "ids"
        ) == ["non_existing_alert_id_1"]:
            return MockResponse("alerts_non_existing", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats" and kwargs.get("params", {}).get("ids") in [
            ["valid_threat_id_1"],
            ["valid_threat_id_2"],
        ]:
            return MockResponse("threats", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts" and kwargs.get("params", {}).get(
            "ids"
        ) in [["valid_alert_id_1"], ["valid_alert_id_2"]]:
            return MockResponse("alerts", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats/analyst-verdict" and sorted(
            kwargs.get("json", {}).get("filter", {}).get("ids")
        ) == ["valid_threat_id_1", "valid_threat_id_2"]:
            return MockResponse("affected_2", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts/analyst-verdict" and sorted(
            kwargs.get("json", {}).get("filter", {}).get("ids")
        ) == ["valid_alert_id_1", "valid_alert_id_2"]:
            return MockResponse("affected_2", 200)
        elif (
            args[1] == "https://rapid7.com/web/api/v2.1/threats/analyst-verdict"
            or args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts/analyst-verdict"
        ):
            return MockResponse("affected_1", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats/incident" and sorted(
            kwargs.get("json", {}).get("filter", {}).get("ids")
        ) == ["valid_threat_id_1", "valid_threat_id_2"]:
            return MockResponse("affected_2", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts/incident" and sorted(
            kwargs.get("json", {}).get("filter", {}).get("ids")
        ) == ["valid_alert_id_1", "valid_alert_id_2"]:
            return MockResponse("affected_2", 200)
        elif (
            args[1] == "https://rapid7.com/web/api/v2.1/threats/incident"
            or args[1] == "https://rapid7.com/web/api/v2.1/cloud-detection/alerts/incident"
        ):
            return MockResponse("affected_1", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.0/threats":
            return MockResponse("threats", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/agents/invalid_id/actions/fetch-files":
            return MockResponse("", 404)
        elif args[1] == "https://rapid7.com/web/api/v2.1/agents/1234567890/actions/fetch-files":
            return MockResponse("fetch_file_by_agent_id_success", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.0/threats/mark-as-benign":
            if json_data.get("filter", {}).get("ids") == ["12345678"] and not json_data.get("data", {}).get(
                "whiteningOption"
            ):
                return MockResponse("mark_as_benign_success", 200)
            elif json_data.get("filter", {}).get("ids") == ["invalid_id"]:
                return MockResponse("", 400)
            if json_data.get("filter", {}).get("ids") == ["12345679"]:
                return MockResponse("mark_as_benign_success_no_affected", 200)
            if json_data.get("data", {}).get("whiteningOption") == "file-type":
                return MockResponse("mark_as_benign_success", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/threats":
            if kwargs.get("params", {}).get("ids") == ["0000000000000000000"]:
                return MockResponse("threats_not_found", 200)
            return MockResponse("threats", 200)
        elif args[1] == r"https://rapid7.com/web/api/v2.1/Device\HarddiskVolume2\Users\Administrator\Desktop\test.txt":
            mock_response = MockResponse("", 200)
            mock_response.content = Util.read_file_to_bytes(f"responses/threats_fetch_file_download.zip.resp")
            return mock_response
        return MockResponse("error", 404)
