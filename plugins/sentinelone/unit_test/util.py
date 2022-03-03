import sys
import os

sys.path.append(os.path.abspath("../"))


from komand_sentinelone.connection.connection import Connection
from requests.exceptions import HTTPError
import json
import logging

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.connection.schema import Input


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
                Input.CREDENTIALS: {"username": "username", "password": "password"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

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
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

            def raise_for_status(self):
                if self.status_code == 200:
                    return

                raise HTTPError("Bad response", response=self)

        if args[0] == "https://rapid7.com/web/api/v2.1/users/login":
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
            return MockResponse("activities_list", 200)
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
            or args[1] == "https://rapid7.com/web/api/v2.0/threats/mark-as-benign"
            or args[1] == "https://rapid7.com/web/api/v2.0/threats/mark-as-threat"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/rollback-remediation"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/quarantine"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/kill"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/remediate"
            or args[1] == "https://rapid7.com/web/api/v2.1/threats/mitigate/un-quarantine"
        ):
            return MockResponse("agents_action", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/agents/support-actions/reload":
            return MockResponse("agents_action", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/agents/summary":
            return MockResponse("agents_summary", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/agents/applications":
            return MockResponse("apps_by_agent_ids", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/sites":
            return MockResponse("sites", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/restrictions":
            return MockResponse("restrictions", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.0/threats?limit=1000":
            return MockResponse("restrictions", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.1/private/accounts/name-available":
            return MockResponse("name_available", 200)
        elif args[1] == "https://rapid7.com/web/api/v2.0/threats":
            return MockResponse("threats", 200)
        return MockResponse("error", 404)
