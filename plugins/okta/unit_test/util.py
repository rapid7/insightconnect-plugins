import json
import logging
import os
import sys
from typing import Dict

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from komand_okta.connection import Connection
from komand_okta.connection.schema import Input

first_request = True


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, custom_params: Dict = {}):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.OKTAURL: "example.okta.com",
            Input.OKTAKEY: {"secretKey": "okta-secret-key"},
        }
        params.update(custom_params)
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
    def mock_wrapper(url=""):
        return Util.mock_request(url=url)

    @staticmethod
    def mock_empty_response(**kwargs):
        return MockResponse(200, "get_logs_empty_response.resp", {"link": ""})

    @staticmethod
    def mock_request(*args, **kwargs):
        method = kwargs.get("method")
        url = kwargs.get("url")
        params = kwargs.get("params")
        json_data = kwargs.get("json")
        global first_request
        if url == "https://example.okta.com/api/v1/logs":
            resp_args = {
                "status_code": 200,
                "filename": "get_logs.json.resp",
                "headers": {
                    "link": '<https://example.okta.com/nextLink?q=next> rel="next"',
                    "x-rate-limit-reset": 1609459200,
                },
            }
            if params.get("since") == "2023-04-27T07:49:21.777Z":
                resp_args["filename"], resp_args["headers"] = "get_logs_single_event.json.resp", {
                    "link": "",
                    "x-rate-limit-reset": 1609459200,
                }
            if params.get("since") == "2023-04-27T07:49:21.888Z":  # Engage rate limit
                resp_args["filename"], resp_args["headers"], resp_args["status_code"] = (
                    "get_logs_empty_response.resp",
                    {"x-rate-limit-limit": 60, "x-rate-limit-reset": 1609459200},
                    429,
                )
            return MockResponse(**resp_args)
        if url == "https://example.okta.com/nextLink?q=next":
            return MockResponse(
                200, "get_logs_next_page.json.resp", {"link": '<https://example.okta.com/nextLink?q=next> rel="next"'}
            )
        if url == "https://example.okta.com/api/v1/groups/12345/users" and first_request:
            first_request = False
            return MockResponse(200, "get_users_in_group.json.resp")
        elif url == "https://example.okta.com/api/v1/groups/12345/users" and not first_request:
            first_request = True
            return MockResponse(200, "get_users_in_group2.json.resp")
        if url == "https://example.okta.com/api/v1/groups/12345":
            return MockResponse(200, "get_group.json.resp")
        if url == "https://example.okta.com/api/v1/users/user@example.com":
            return MockResponse(200, "get_user.json.resp")
        if url == "https://example.okta.com/api/v1/users/invalid@example.com":
            return MockResponse(404)
        if method == "DELETE":
            if url == "https://example.okta.com/api/v1/groups/123456/users/12345":
                return MockResponse(204)
            if url == "https://example.okta.com/api/v1/groups/invalid_group/users/12345":
                return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/12345/lifecycle/reset_factors":
            return MockResponse(200, "reset_factors.json.resp")
        if url == "https://example.okta.com/api/v1/users/12345/lifecycle/expire_password":
            if params == {"tempPassword": False}:
                return MockResponse(200, "expire_password.json.resp")
            if params == {"tempPassword": True}:
                return MockResponse(200, "expire_password_with_temp_password.json.resp")
        if url == "https://example.okta.com/api/v1/users/12345/lifecycle/reset_password":
            if params == {"sendEmail": False, "revokeSessions": False}:
                return MockResponse(200, "reset_password.json.resp")
            if params == {"sendEmail": True, "revokeSessions": False}:
                return MockResponse(200, "reset_password_with_send_email.json.resp")
            if params == {"sendEmail": False, "revokeSessions": True}:
                return MockResponse(200, "reset_password_with_revoke_sessions.json.resp")
        if url == "https://example.okta.com/api/v1/users/invalid_user/lifecycle/expire_password":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/invalid_user/lifecycle/reset_password":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/zones":
            return MockResponse(200, "get_zones.json.resp")
        if method == "PUT" and url == "https://example.okta.com/api/v1/zones/56789":
            gateways = kwargs.get("json", {}).get("gateways", [])
            if {"type": "RANGE", "value": "1.1.1.1"} in gateways:
                return MockResponse(200, "update_blacklist_zone.json.resp")
            if {"type": "RANGE", "value": "1.1.1.1-1.1.1.1"} in gateways:
                return MockResponse(200, "update_blacklist_zone.json.resp")
            if {"type": "CIDR", "value": "1.1.1.1/24"} in gateways:
                return MockResponse(200, "update_blacklist_zone_cidr.json.resp")
            if {"type": "RANGE", "value": "2001:db8:1:1:1:1:1:2"} in gateways:
                return MockResponse(200, "update_blacklist_zone_ipv6.json.resp")
            if gateways == [{"type": "CIDR", "value": "1.2.3.4/24"}]:
                return MockResponse(200, "update_blacklist_zone_remove_ipv4.json.resp")
            if gateways == [{"type": "RANGE", "value": "1.2.3.4-1.2.3.4"}]:
                return MockResponse(200, "update_blacklist_zone_remove_cidr.json.resp")
        if method == "POST" and url == "https://example.okta.com/api/v1/apps/123456/users":
            if kwargs.get("json") == {"id": "invalid"}:
                return MockResponse(404)
            return MockResponse(200, "assign_user_to_app_sso.json.resp")
        if method == "POST" and url == "https://example.okta.com/api/v1/apps/invalid/users":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/groups":
            if params == {"q": "Test"}:
                return MockResponse(200, "list_groups_with_query.json.resp")
            if params == {"q": "Invalid"}:
                return MockResponse(200, "list_groups_empty.json.resp")
            return MockResponse(200, "list_groups.json.resp")

        if url == "https://example.okta.com/api/v1/users":
            if json_data.get("profile").get("email") == "user_bad@sample.com":
                return MockResponse(400, "")
            if json_data.get("groupIds") == ["12345"]:
                return MockResponse(200, "create_user_with_provider.json.resp")
            if json_data.get("credentials").get("password") == {"value": "randomPASS1"}:
                return MockResponse(200, "create_user_with_password.json.resp")
            if json_data.get("credentials").get("provider") == {"name": "OKTA", "type": "OKTA"}:
                return MockResponse(200, "create_user_with_provider.json.resp")

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S1/factors":
            return MockResponse(200, "get_factors_existing_user.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S2/factors":
            return MockResponse(200, "get_factors_existing_user_without_factors.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors":
            return MockResponse(404)

        if url == "https://example.okta.com/api/v1/groups/00g1a1qwertYuiopA0h1/users/00u1m1qwertYUiopA0S1":
            return MockResponse(204)
        if url == "https://example.okta.com/api/v1/groups/00g1a1qwertYuiopA0h2/users/00u1m1qwertYUiopA0S1":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/groups/00g1a1qwertYuiopA0h1/users/00u1m1qwertYUiopA0S2":
            return MockResponse(204)
        if url == "https://example.okta.com/api/v1/groups/00g1a1qwertYuiopA0h1/users/00u1m1qwertYUiopA0S3":
            return MockResponse(404)

        if url == "https://example.okta.com/api/v1/users/user1@example.com" and method == "GET":
            return MockResponse(200, "get_user1.json.resp")
        if url == "https://example.okta.com/api/v1/users/user2@example.com" and method == "GET":
            return MockResponse(200, "get_user2.json.resp")
        if url == "https://example.okta.com/api/v1/users/user11@example.com" and method == "GET":
            return MockResponse(404)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S1" and method == "DELETE":
            return MockResponse(204)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S1/lifecycle/deactivate":
            return MockResponse(200, "deactivate_user_success.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S2/lifecycle/deactivate":
            return MockResponse(404)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S1/lifecycle/suspend":
            return MockResponse(200, "suspend_user_success.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S2/lifecycle/suspend":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/lifecycle/suspend":
            return MockResponse(400)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/lifecycle/unsuspend":
            return MockResponse(200, "unsuspend_user_success.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S2/lifecycle/unsuspend":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S1/lifecycle/unsuspend":
            return MockResponse(400)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d9/verify":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S2/factors/aaa1qwerty0UIOPaS0d1/verify":
            return MockResponse(404)

        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d1/verify":
            return MockResponse(201, "send_push_verify_challenge1.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d2/verify":
            return MockResponse(201, "send_push_verify_challenge2.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d3/verify":
            return MockResponse(201, "send_push_verify_challenge3.json.resp")
        if url == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d8/verify":
            return MockResponse(200, "send_push_verify_challenge_not_push.json.resp")

        if (
            url
            == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d1/transactions/abcde.ABCDEFGH"
        ):
            return MockResponse(200, "send_push_verify_poll_status_success.json.resp")
        if (
            url
            == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d2/transactions/asdfg.QWERTYUI"
        ):
            return MockResponse(200, "send_push_verify_poll_status_rejected.json.resp")
        if (
            url
            == "https://example.okta.com/api/v1/users/00u1m1qwertYUiopA0S3/factors/aaa1qwerty0UIOPaS0d3/transactions/mmmmm.AAAAAAAA"
        ):
            return MockResponse(200, "send_push_verify_poll_status_waiting.json.resp")

        if url == "https://example.okta.com/api/v1/users/1234/groups":
            return MockResponse(200, "get_user_groups_by_id_success.json.resp")
        if url == "https://example.okta.com/api/v1/users/user@example.com/groups":
            return MockResponse(200, "get_user_groups_by_login_success.json.resp")
        if url == "https://example.okta.com/api/v1/users/123456/groups":
            return MockResponse(200, "get_user_groups_empty.json.resp")
        if url == "https://example.okta.com/api/v1/users/12345/groups":
            return MockResponse(404)
        if url == "https://example.okta.com/api/v1/users/user2@example.com/groups":
            return MockResponse(404)

        raise NotImplementedError("Not implemented", kwargs)


class MockResponse:
    def __init__(self, status_code: int, filename: str = None, headers: dict = {}):
        self.status_code = status_code
        self.text = ""
        self.headers = headers
        if filename:
            self.text = Util.read_file_to_string(f"responses/{filename}")

    def json(self):
        return json.loads(self.text)
