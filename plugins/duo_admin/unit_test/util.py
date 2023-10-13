import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime

from komand_duo_admin.connection import Connection
from komand_duo_admin.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.HOSTNAME: "example.com",
            Input.SECRETKEY: {"secretKey": "duo-secret-key"},
            Input.INTEGRATIONKEY: {"secretKey": "duo-integration-key"},
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
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
                self.status_code = status_code
                self.text = ""
                self.headers = headers
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        method = kwargs.get("method", "")
        url = kwargs.get("url", "")
        params = kwargs.get("params", {})

        if url == "https://example.com/admin/v2/logs/authentication":
            breakpoint()
            if params == {"mintime": "1682843686000", "maxtime": "1682929966000", "limit": "1000", "sort": "ts:asc"}:
                print("return A1")
                return MockResponse(200, "get_auth_logs.json.resp")
            if params == {"mintime": "1682843686000", "maxtime": "1682929966000", "limit": "1000", "sort": "ts:asc"}:
                print("return A*")
                return MockResponse(200, "get_auth_logs.json.resp")
            if params == {"mintime": "1682670886000", "maxtime": "1682929966000", "limit": "1000", "sort": "ts:asc"}:
                print("return A2")
                return MockResponse(200, "get_auth_logs_empty.json.resp")
            if params == {
                "mintime": "1684009458000",
                "maxtime": "1684209458000",
                "applications": ["DI8CODQSMK4BXPLYS47K"],
                "users": ["DUWZR0IUOT27EPXSCOI9"],
                "event_types": ["enrollment"],
                "factors": ["not_available"],
                "groups": ["DPS4SII7YZ7ISQITTC2W"],
                "phone_numbers": ["+111111111"],
                "results": ["success"],
                "limit": "1000",
            }:
                print("return A3")
                return MockResponse(200, "get_auth_logs_2.json.resp")
            if params == {"mintime": "1682843686000", "maxtime": "1682930026000", "limit": "1000"}:
                return MockResponse(200, "get_auth_logs_3.json.resp")
            if params == {
                "mintime": "1682843686000",
                "maxtime": "1682930026000",
                "limit": "1000",
                "next_offset": ["1683730665255", "9de5069c-5afe-602b-2ea0-a04b66beb2c0"],
                "sort": "ts:asc",
            }:
                return MockResponse(200, "get_auth_logs_4.json.resp")
        if url == "https://example.com/admin/v1/logs/administrator":
            breakpoint()
            if params == {"mintime": "1682843686"}:
                return MockResponse(200, "get_admin_logs.json.resp")
            if params == {"mintime": "1682670886"}:
                return MockResponse(200, "get_admin_logs.json.resp")
            if params == {"mintime": "1682930026"}:
                return MockResponse(200, "get_admin_logs.json.resp")
        if url == "https://example.com/admin/v1/trust_monitor/events":
            breakpoint()
            if params == {"mintime": "1682843686000", "maxtime": "1682929966000", "limit": "200"}:
                return MockResponse(200, "get_trust_monitor_events.json.resp")
            if params == {"mintime": "1682670886000", "maxtime": "1682929966000", "limit": "200"}:
                return MockResponse(200, "get_trust_monitor_events.json.resp")
            if params == {"mintime": "1682843686000", "maxtime": "1682930026000", "limit": "200", "offset": "1591014"}:
                return MockResponse(200, "get_trust_monitor_events_2.json.resp")
            if params == {"mintime": "1000000000400", "maxtime": "1682930026000", "limit": "200"}:
                return MockResponse(400)
            if params == {"mintime": "1000000000500", "maxtime": "1682930026000", "limit": "200"}:
                return MockResponse(500)

        if url == "https://example.com/admin/v1/users/valid-id" and params == {}:
            return MockResponse(200, "get_user_by_id.json.resp")
        if url == "https://example.com/admin/v1/users/not-exist" and params == {}:
            return MockResponse(404, "")
        if url == "https://example.com/admin/v1/users" and params == {"username": "Example User"}:
            return MockResponse(200, "get_user_status.json.resp")
        if url == "https://example.com/admin/v1/users" and params == {"username": "Invalid User"}:
            return MockResponse(200, "get_user_status_invalid_username.json.resp")
        if url == "https://example.com/admin/v1/users" and params == {"username": "valid-username-1"}:
            return MockResponse(200, "get_user_by_username_1.json.resp")
        if url == "https://example.com/admin/v1/users" and params == {"username": "valid-alias"}:
            return MockResponse(200, "get_user_by_username_2.json.resp")
        if url == "https://example.com/admin/v1/users" and params == {"username": "not-exist-username"}:
            return MockResponse(404, "get_user_by_username_bad.json.resp")

        if url == "https://example.com/admin/v1/users" and params == {}:
            return MockResponse(200, "get_users.json.resp")

        if method == "POST" and url == "https://example.com/admin/v1/users/modify-non-existing":
            return MockResponse(404, "")

        if method == "POST" and url == "https://example.com/admin/v1/users/modify-valid-id":
            if params == {"username": "duplicated-username"} or params == {"alias1": "duplicated-alias"}:
                return MockResponse(400, "")
            return MockResponse(200, "modify_user.json.resp")

        if method == "DELETE":
            if url == "https://example.com/admin/v1/users/ABCD01":
                return MockResponse(200, "delete_user_success.json.resp")
            if url == "https://example.com/admin/v1/users/invalid_id":
                return MockResponse(404)

        if url == "https://example.com/admin/v1/users/ABCD01/phones":
            return MockResponse(200, "get_phones_by_user_id_no_phones.json.resp")
        if url == "https://example.com/admin/v1/users/ABCD02/phones":
            return MockResponse(200, "get_phones_by_user_id_existing_phones.json.resp")
        if url == "https://example.com/admin/v1/users/invalid_id/phones":
            return MockResponse(404)

        if url == "https://example.com/admin/v1/users/enroll":
            if params.get("username") == "example-username-1":
                return MockResponse(200, "enroll_user_success.json.resp")
            if params.get("username") == "example-username-2":
                return MockResponse(200, "enroll_user_success.json.resp")
            if params.get("username") == "example-username-3":
                return MockResponse(400)

        if method == "POST" and url == "https://example.com/admin/v1/users":
            if params.get("username") == "user-example-1":
                return MockResponse(200, "add_user_success_1.json.resp")
            if params.get("username") == "user-example-2":
                return MockResponse(200, "add_user_success_2.json.resp")
            if params.get("username") == "user-example-3":
                return MockResponse(400)
            if params.get("username") == "user-example-5":
                return MockResponse(400)

        raise NotImplementedError("Not implemented", kwargs)
