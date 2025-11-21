import json
import logging
import os.path
import sys

from icon_rapid7_insight_agent.connection import Connection
from icon_rapid7_insight_agent.connection.schema import Input

sys.path.append(os.path.abspath("../"))

DEFAULT_ENCODING = "utf-8"


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
        with open(
            (os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)), encoding=DEFAULT_ENCODING
        ) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            HTTP_EXCEPTION = "ExampleHttpException"

            def __init__(self, filename: str = None, text: str = ""):
                self.filename = filename
                self.text = text

            def json(self):
                return Util.load_json(f"responses/{self.filename}")

            def raise_for_status(self):
                if self.HTTP_EXCEPTION in self.text:
                    raise Exception(self.HTTP_EXCEPTION)

        body = args[0].__dict__.get("body")
        data = json.loads(body.decode(DEFAULT_ENCODING)) if body else None

        query = data.get("query")
        variables = data.get("variables")

        if query == "{ organizations(first: 1) { edges { node { id name } } } }":
            return MockResponse("org_key.json.resp")
        elif variables.get("orgId") == "9de5069c5afe602b2ea0a04b66beb2c0":
            return MockResponse("get_agent_details.resp")
        elif (
            query == "query( $orgId:String! ) { organization(id: $orgId) { assets( first: 10000 ) { pageInfo { hasNextPage endCursor } edges { node { id platform host { vendor version description hostNames { name } primaryAddress { ip mac } uniqueIdentity { source id } attributes { key value } } publicIpAddress location { city region countryName countryCode continent } agent { agentSemanticVersion agentStatus quarantineState { currentState } } } } } } }"
        ):
            return MockResponse("get_all_agents_by_ip.resp")
        elif variables.get("agentID") == "goodID":
            return MockResponse("check_agent_status.resp")
        elif variables.get("agentID") == "badID":
            return MockResponse("check_agent_status_bad.resp")
        elif variables.get("agentID", {}) == "goodIDQuarantine":
            return MockResponse("quarantine.resp")
        elif (
            variables.get("agentID") == "a1cfb273EQWE12312EDSAXZc8e7d46a9e2a0e2dae01a0ce" and
            query == "query( $orgID: String! $agentID: String! ) { assets( orgId: $orgID ids: [$agentID] ){ agent { id quarantineState{ currentState } agentStatus } } }"
        ):
            return MockResponse("unquarantine_check.resp")
        elif (
            variables.get("agentID") == "a1cfb273EQWE12312EDSAXZc8e7d46a9e2a0e2dae01a0ce" and
            query == "mutation( $orgID:String! $agentID:String!) { unquarantineAssets( orgId:$orgID assetIds: [$agentID] ) { results { assetId failed } } }"
        ):
            return MockResponse("unquarantine.resp")
        elif (
            variables.get("agentID") == "a1cfb273EQWE12312EDSAXZc8e7d46a9e2a0e2dae01a0ce"
        ):
            return MockResponse("quarantine.resp")
        elif variables.get("agentID") == "badIDQuarantine":
            return MockResponse("quarantine_bad.resp")
        elif variables.get("agentID") == "agent_id":
            return MockResponse("quarantine_multiple.resp")
        elif variables.get("agentID") == "agent_id_bad":
            return MockResponse("quarantine_multiple_failure.resp")
        raise Exception("Not implemented")
