import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from requests.exceptions import HTTPError
from komand_sentinelone.connection.connection import Connection
from komand_sentinelone.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.INSTANCE: "rapid7",
                Input.APIKEY: {"secretKey": "test"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename),
            "r",
            encoding="utf-8",
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
            def __init__(self, status_code: int, filename: str = None, url: str = None):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"
                self.url = url
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}.json.resp")

            def json(self):
                return json.loads(self.text)

            def raise_for_status(self):
                if self.status_code == 200:
                    return
                raise HTTPError("Bad response", response=self)

        params = kwargs.get("params", {})
        json_data = kwargs.get("json", {})

        if args[0] == "https://rapid7.sentinelone.net/web/api/v2.1/users/login/by-api-token":
            return MockResponse(200, "get_token")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents":
            if not params:
                return MockResponse(200, "search_agents_all")
            elif params == {"isActive": True}:
                return MockResponse(200, "search_agents_all_active")
            elif params.get("ids") == "0000000000000000001":
                return MockResponse(200, "search_agents_single")
            elif params.get("computerName") == "Hostname0":
                return MockResponse(200, "search_agents_single")
            elif params.get("networkInterfaceInet__contains") == "1.2.3.4":
                return MockResponse(200, "search_agents_single")
            elif params.get("externalIp__contains") == "1.2.3.4":
                return MockResponse(200, "search_agents_single")
            elif params.get("networkInterfaceInet__contains") == "198.51.100.1":
                return MockResponse(200, "search_agents_single_2")
            elif params.get("externalIp__contains") == "198.51.100.1":
                return MockResponse(200, "search_agents_single_2")
            elif params.get("networkInterfacePhysical__contains") == "00:12:34:45:56:90":
                return MockResponse(200, "search_agents_single")
            elif params.get("networkInterfacePhysical__contains") == "b7b2d39171be4ae1af90f93d7ed20f07":
                return MockResponse(200, "search_agents_empty")
            elif params.get("uuid") == "b7b2d39171be4ae1af90f93d7ed20f07":
                return MockResponse(200, "search_agents_single")
            elif params.get("uuid") == "00:12:34:45:56:90":
                return MockResponse(200, "search_agents_empty")
            elif params.get("computerName") == "Hostname1":
                return MockResponse(200, "search_agents_multiple")
            elif params == {"isActive": False}:
                return MockResponse(200, "search_agents_empty")
            elif params.get("computerName") == "Hostname4":
                return MockResponse(200, "search_agents_empty")
        elif (
            args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/connect"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/disconnect"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/initiate-scan"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/abort-scan"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/fetch-logs"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/restart-machine"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/shutdown"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/decommission"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/uninstall"
        ):
            if json_data == {"filter": {"ids": ["0000000000000000002"]}}:
                return MockResponse(200, "affected_0")
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/enable-agent":
            if json_data.get("filter", {}).get("computerName") == "Hostname4":
                return MockResponse(200, "affected_0")
            elif json_data.get("filter", {}).get("computerName") == "Hostname1":
                return MockResponse(200, "affected_2")
            else:
                return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/disable-agent":
            if json_data.get("filter", {}).get("computerName") == "Hostname4":
                return MockResponse(200, "affected_0")
            elif json_data.get("filter", {}).get("computerName") == "Hostname1":
                return MockResponse(200, "affected_2")
            elif json_data.get("data", {}).get("expiration") == "2000-01-01T00:00:00.000000+03:00":
                return MockResponse(400)
            else:
                return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/add-to-blacklist":
            if json_data == {
                "filter": {"contentHashes": "3395856ce81f2b7382dee72602f798b642f14140"},
                "data": {"targetScope": "site"},
            }:
                return MockResponse(200, "affected_1")
            if json_data == {
                "filter": {"contentHashes": "invalid_hash"},
                "data": {"targetScope": "site"},
            }:
                return MockResponse(200, "affected_0")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/fetch-file":
            return MockResponse(200, "threats_fetch_file")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/users/auth/elevate":
            return MockResponse(200, "protected_actions_session")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/remote-scripts/execute":
            if json_data.get("filter") == {}:
                return MockResponse(200, "affected_2")
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/activities":
            if params.get("threatIds") == "1000000000000000001":
                return MockResponse(200, "activities_malicious_file_path")
            if params.get("countOnly"):
                return MockResponse(200, "activities_count_only")
            if params == {
                "includeHidden": False,
                "skipCount": True,
                "countOnly": False,
                "limit": 1000,
                "sortBy": "id",
                "sortOrder": "desc",
            }:
                return MockResponse(200, "activities_skip_count")
            if params == {
                "includeHidden": False,
                "skipCount": False,
                "countOnly": False,
                "limit": 1000,
                "sortBy": "createdAt",
                "sortOrder": "asc",
            }:
                return MockResponse(200, "activities_first_page")
            if params == {
                "includeHidden": False,
                "skipCount": False,
                "ids": "invalid_id",
                "countOnly": False,
                "limit": 1000,
                "sortBy": "createdAt",
                "sortOrder": "asc",
            }:
                return MockResponse(200, "activities_empty")
            if params in [
                {
                    "limit": 1000,
                    "sortBy": "createdAt",
                    "createdAt__gt": "1999-12-31T00:00:00.000000Z",
                    "createdAt__lte": "2000-01-01T00:00:00.000000Z",
                },
                {
                    "limit": 1000,
                    "sortBy": "createdAt",
                    "cursor": "YWdlbnRfaWQ6NTgwMjkzODE=",
                },
                {
                    "limit": 1000,
                    "createdAt__gt": "1999-12-30T00:00:00.000000Z",
                    "createdAt__lte": "2000-01-01T00:00:00.000000Z",
                    "sortBy": "createdAt",
                },
            ]:
                return MockResponse(200, "monitor_logs_activities")
            if params == {
                "limit": 1000,
                "sortBy": "createdAt",
                "cursor": "ZWdlbnRfaWQ6NTgwMjkzODE=",
            }:
                return MockResponse(401)
            if params.get("cursor") == "400":
                return MockResponse(400)
            if params.get("cursor") == "401":
                return MockResponse(401)
            if params.get("cursor") == "403":
                return MockResponse(403)
            if params.get("cursor") == "404":
                return MockResponse(404)
            if params.get("cursor") == "500":
                return MockResponse(500)
            return MockResponse(200, "activities_second_page")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/activities/types":
            return MockResponse(200, "activities_types")
        elif (
            args[1] == "https://rapid7.sentinelone.net/web/api/v2.0/threats/mark-as-threat"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/mitigate/rollback-remediation"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/mitigate/quarantine"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/mitigate/kill"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/mitigate/remediate"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/mitigate/un-quarantine"
        ):
            if kwargs.get("json", {}).get("filter", {}).get("ids") == ["XYZABC"]:
                return MockResponse(400)
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/private/threats/ioc-create-threats":
            data = json_data.get("data", [])
            if data and isinstance(data, list):
                if data[0].get("agentId") == "invalid_id" or data[0].get("hash") == "invalid_hash":
                    return MockResponse(400)
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/private/agents/support-actions/reload":
            if json_data == {
                "filter": {"ids": ["invalid_id"]},
                "data": {"module": "monitor"},
            }:
                return MockResponse(200, "affected_0")
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/private/agents/summary":
            if params in [
                {},
                {"siteIds": "1234567890987654321"},
                {"siteIds": "1234567890987654321,1234567890987654322"},
                {"accountIds": "1234567890987654321"},
                {"accountIds": "1234567890987654321,1234567890987654321"},
                {"siteIds": "1234567890987654321", "accountIds": "1234567890987654321"},
            ]:
                return MockResponse(200, "agents_summary")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/dv/query-status":
            if params == {"queryId": "q9679169d5a4607cc41a9100123456789"}:
                return MockResponse(200, "get_query_status")
            if params == {"queryId": "q9679169d5a4607cc41a9100987654321"}:
                return MockResponse(404)
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/dv/cancel-query":
            if json_data == {"queryId": "q9679169d5a4607cc41a9100123456789"}:
                return MockResponse(200, "cancel_running_query")
            if json_data == {"queryId": "q9679169d5a4607cc41a9100987654321"}:
                return MockResponse(404, "cancel_running_query")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/dv/init-query":
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
                return MockResponse(200, "create_query")
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "isVerbose": False,
                "limit": 100,
                "query": "AgentName IS NOT EMPTY",
                "tenant": False,
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse(200, "create_query")
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "limit": 100,
                "query": "AgentName IS NOT EMPTY",
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse(200, "create_query")
            if json_data == {
                "fromDate": "2023-09-20T04:49:26.257525Z",
                "limit": 100,
                "query": "AgentName IS NOT EMPTYY",
                "toDate": "2023-09-21T20:49:26.257525Z",
            }:
                return MockResponse(400)
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/applications":
            return MockResponse(200, "apps_by_agent_ids_success")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/sites":
            return MockResponse(200, "sites")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/restrictions":
            if params == {
                "type": "black_hash",
                "includeChildren": True,
                "includeParents": True,
                "value": "3395856ce81f2b7382dee72602f798b642f14141",
            }:
                return MockResponse(200, "restrictions_2")
            if params == {
                "type": "black_hash",
                "includeChildren": True,
                "includeParents": True,
                "value": "3395856ce81f2b7382dee72602f798b642f14142",
            }:
                return MockResponse(200, "restrictions_empty")
            if params == {
                "type": "black_hash",
                "ids": "1234567891,1234567892,1234567893",
                "includeChildren": True,
                "includeParents": True,
            }:
                return MockResponse(200, "restrictions_2")
            return MockResponse(200, "restrictions")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.0/threats" and params.get("limit") == 1000:
            if params.get("cursor") == "abcd":
                return MockResponse(200, "get_threat_summary_page_2")
            else:
                return MockResponse(200, "get_threat_summary_page_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/private/accounts/name-available":
            if "NotAvailableName" in params.get("name"):
                return MockResponse(200, "name_not_available")
            return MockResponse(200, "name_available")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats":
            if params.get("cursor") == "401":
                return MockResponse(401)
            if params.get("cursor") == "403":
                return MockResponse(403)
            if params.get("ids") in [
                ["valid_threat_id_1"],
                ["valid_threat_id_2"],
                ["1000000000000000000"],
                ["1000000000000000001"],
            ]:
                return MockResponse(200, "threats")
            if params.get("ids") == ["same_status_threat_id_1"]:
                return MockResponse(200, "threats_same_status")
            if params.get("ids") in [
                ["non_existing_threat_id_1"],
                ["0000000000000000000"],
            ]:
                return MockResponse(200, "threats_not_found")
            return MockResponse(200, "monitor_logs_threats")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/cloud-detection/alerts":
            if params.get("ids") in [["valid_alert_id_1"], ["valid_alert_id_2"]]:
                return MockResponse(200, "alerts")
            if params.get("ids") == ["same_status_alert_id_1"]:
                return MockResponse(200, "alerts_same_status")
            if params.get("ids") == ["non_existing_alert_id_1"]:
                return MockResponse(200, "alerts_non_existing")
        elif (
            args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/analyst-verdict"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/cloud-detection/alerts/analyst-verdict"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/threats/incident"
            or args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/cloud-detection/alerts/incident"
        ):
            if sorted(json_data.get("filter", {}).get("ids")) == [
                "valid_threat_id_1",
                "valid_threat_id_2",
            ]:
                return MockResponse(200, "affected_2")
            if sorted(json_data.get("filter", {}).get("ids")) == [
                "valid_alert_id_1",
                "valid_alert_id_2",
            ]:
                return MockResponse(200, "affected_2")
            return MockResponse(200, "affected_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.0/threats":
            return MockResponse(200, "threats")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/invalid_id/actions/fetch-files":
            return MockResponse(404)
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/1234567890/actions/fetch-files":
            return MockResponse(200, "fetch_file_by_agent_id_success")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.0/threats/mark-as-benign":
            if json_data.get("filter", {}).get("ids") == ["12345678"] and not json_data.get("data", {}).get(
                "whiteningOption"
            ):
                return MockResponse(200, "mark_as_benign_success")
            elif json_data.get("filter", {}).get("ids") == ["invalid_id"]:
                return MockResponse(400)
            if json_data.get("filter", {}).get("ids") == ["12345679"]:
                return MockResponse(200, "mark_as_benign_success_no_affected")
            if json_data.get("data", {}).get("whiteningOption") == "file-type":
                return MockResponse(200, "mark_as_benign_success")
        elif (
            args[1]
            == r"https://rapid7.sentinelone.net/web/api/v2.1/Device\HarddiskVolume2\Users\Administrator\Desktop\test.txt"
        ):
            mock_response = MockResponse(200)
            mock_response.content = Util.read_file_to_bytes(f"responses/threats_fetch_file_download.zip.resp")
            return mock_response
        elif (
            args[1]
            == r"https://rapid7.sentinelone.net/web/api/v2.1/Fake\HarddiskVolume2\Users\Administrator\Desktop\test.txt"
        ):
            mock_response = MockResponse(200)
            mock_response.content = Util.read_file_to_bytes(f"responses/threats_fetch_file_download.zip.resp")
            return mock_response
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/dv/events":
            if params.get("queryId") == "q9679169d5a4607cc41a9101234567891":
                return MockResponse(404)
            else:
                if params.get("subQuery") == "AgentName IS EMPTY":
                    return MockResponse(200, "get_events_success_with_sub_query")
                elif params.get("subQuery") == "invalid_sub_query":
                    return MockResponse(503)
                elif params.get("limit") == 2:
                    return MockResponse(200, "get_events_success_with_limit")
                else:
                    if params.get("cursor"):
                        return MockResponse(200, "get_events_success_page_2")
                    else:
                        return MockResponse(200, "get_events_success_page_1")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/agents/actions/move-to-site":
            if json_data.get("data", {}).get("targetSiteId", "") == "1234567891234567890":
                return MockResponse(200, "move_between_sites_minimum")
            elif json_data.get("data", {}).get("targetSiteId", "") == "1234567891234567891":
                return MockResponse(200, "move_between_sites_data")
        elif args[1] == "https://rapid7.sentinelone.net/web/api/v2.1/device-control/events":
            if params.get("eventTime__gt") == "1999-12-25T00:00:00.000000Z":
                return MockResponse(200, "monitor_logs_events_unexpected_timestamp")
            if params.get("cursor") == "401":
                return MockResponse(401)
            if params.get("cursor") == "403":
                return MockResponse(403)
            return MockResponse(200, "monitor_logs_events")
        return MockResponse(404)
