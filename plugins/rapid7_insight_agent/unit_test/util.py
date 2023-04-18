import json
import logging
import os.path
import sys

sys.path.append(os.path.abspath("../"))
from icon_rapid7_insight_agent.connection import Connection
from icon_rapid7_insight_agent.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.REGION: "United States",
            Input.API_KEY: {"secretKey": "0709b1ba-07da-41a1-bf84-79e67d6f0c54"},
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str = None):
                self.filename = filename

            def json(self):
                return Util.load_json(f"responses/{self.filename}")

            def raise_for_status(self):
                pass

        if kwargs.get("json").get("query") == "{ organizations(first: 1) { edges { node { id name } } } }":
            return MockResponse("org_key.json.resp")
        elif kwargs.get("json").get("variables").get("agentID") == "goodID":
            return MockResponse("check_agent_status.resp")
        elif kwargs.get("json").get("variables").get("agentID") == "badID":
            return MockResponse("check_agent_status_bad.resp")
        elif kwargs.get("json").get("variables").get("agentID") == "goodIDQuarantine":
            return MockResponse("quarantine.resp")
        elif kwargs.get("json").get("variables").get("agentID") == "badIDQuarantine":
            return MockResponse("quarantine_bad.resp")
        elif kwargs.get("json").get("variables").get("agentID") == "assetID":
            return MockResponse("quarantine_multiple.resp")
        elif kwargs.get("json").get("variables").get("orgId") == "9de5069c5afe602b2ea0a04b66beb2c0":
            return MockResponse("get_agent_details.resp")
        return "Not implemented"
