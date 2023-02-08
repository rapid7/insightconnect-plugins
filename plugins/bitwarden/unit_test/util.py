import json
import logging
import sys
import os

import insightconnect_plugin_runtime

from icon_bitwarden.connection import Connection
from icon_bitwarden.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {Input.CLIENTID: "clientId.1234", Input.CLIENTSECRET: {"secretKey": "my-secret-1234"}}
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        url = kwargs.get("url", "")
        json_data = kwargs.get("json", {})
        method = kwargs.get("method", "")
        params = kwargs.get("params", {})

        if url == "https://identity.bitwarden.com/connect/token":
            return MockResponse(200, "connection.txt.resp")

        if url == "https://api.bitwarden.com/public/collections":
            return MockResponse(200, "list_collections.json.resp")

        if url == "https://api.bitwarden.com/public/members" and method == "GET":
            return MockResponse(200, "list_all_members.json.resp")

        if url == "https://api.bitwarden.com/public/members":
            if json_data.get("collections") == []:
                return MockResponse(200, "create_member.json.resp")

            if json_data.get("collections") == [{"id": "aa8e96ad-11c1-44d8-a628-cdc986b79c5d", "readOnly": False}]:
                return MockResponse(200, "create_member_with_collections.json.resp")

            if json_data.get("collections") == ["string"]:
                return MockResponse(400, "")

        if method == "PUT":
            if url.endswith("6a47f057-a57c-421f-9a28-5957c990ad90"):
                return MockResponse(200, "update_member.json.resp")
            if url.endswith("664a90c1-0516-40d6-b09f-6b30ba92bc90"):
                return MockResponse(200, "update_member_no_collections.json.resp")
            if url.endswith("85cbb47b-c634-4baa-bbf3-fe7aaf3c7691"):
                return MockResponse(400, "")
            if url.endswith("67c9877c-99fd-410c-8320-96c6ad0c736c"):
                return MockResponse(404, "")

        if url == "https://api.bitwarden.com/public/members/409d849f-79eb-4f38-b752-2096bdb8b70d":
            return MockResponse(200, "retrieve_member.json.resp")

        if url == "https://api.bitwarden.com/public/members/5f8038a8-3741-49fd-b224-3f8d0311b4e3":
            return MockResponse(200, "retrieve_member_with_collections.json.resp")

        if url == "https://api.bitwarden.com/public/members/e122170e-3c69-4e2f-91c3-c6e0c1f9c97a":
            return MockResponse(404, "")

        if url == "https://api.bitwarden.com/public/members/invalid-uuid":
            return MockResponse(400, "")

        if url == "https://api.bitwarden.com/public/members/01a6ef63-a5b9-4f88-a8ca-d6cd2635cd4a":
            return MockResponse(200, "")

        if url == "https://api.bitwarden.com/public/groups":
            return MockResponse(200, "list_all_groups.json.resp")

        if url == "https://api.bitwarden.com/public/members/44d88612-fea8-a8f3-6de8-2e1278abb02f/reinvite":
            return MockResponse(200, "")
        if url == "https://api.bitwarden.com/public/members/invalid_id/reinvite":
            return MockResponse(404, "")

        if (
            url == "https://api.bitwarden.com/public/members/44d88612-fea8-a8f3-6de8-2e1278abb02f/group-ids"
            and method == "PUT"
        ):
            return MockResponse(200, "")
        if url == "https://api.bitwarden.com/public/members/44d88612-fea8-a8f3-6de8-2e1278abb02f/group-ids":
            return MockResponse(200, "retrieve_members_group_ids.json.resp")
        if url == "https://api.bitwarden.com/public/members/invalid_id/group-ids":
            return MockResponse(404, "")

        if url == "https://api.bitwarden.com/public/events" and params == {
            "actingUserId": "539a36c5-e0d2-4cf9-979e-51ecf5cf6593"
        }:
            return MockResponse(200, "list_events2.json.resp")
        if url == "https://api.bitwarden.com/public/events" and params == {"actingUserId": "invalid_id"}:
            return MockResponse(200, "list_events_empty.json.resp")
        if url == "https://api.bitwarden.com/public/events" and params == {
            "itemId": "44d88612-fea8-a8f3-6de8-2e1278abb02f"
        }:
            return MockResponse(200, "list_events3.json.resp")
        if url == "https://api.bitwarden.com/public/events" and params == {
            "start": "2023-01-10T12:00:00Z",
            "end": "2023-01-20T12:00:00Z",
        }:
            return MockResponse(200, "list_events1.json.resp")
        if url == "https://api.bitwarden.com/public/events":
            return MockResponse(200, "list_events1.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
