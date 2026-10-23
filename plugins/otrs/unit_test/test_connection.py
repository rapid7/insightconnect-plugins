import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from komand_otrs.util.constants import SESSION_ASSISTANCE, SESSION_CAUSE
from util import Util


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Util.connection()

    @parameterized.expand(
        [
            # OTRS 8+ replies to the first login with an access token
            ("access_token", ["access_token"], ["UserLogin"], "AccessToken"),
            # Older OTRS sends a session ID instead, so PyOTRS retries with a legacy login
            ("legacy_session_id", ["session_id", "session_id"], ["UserLogin", "UserLogin"], "SessionID"),
        ]
    )
    @patch("requests.request")
    def test_success(
        self, _name: str, replies: list[str], payload_keys: list[str], session_key: str, request_mock: MagicMock
    ) -> None:
        # Setup mock to return different responses for each call
        request_mock.side_effect = [Util.response(reply) for reply in replies]

        # This will trigger a login and set the session key
        self.assertEqual({"success": True}, self.connection.test())
        self.assertEqual(len(replies), request_mock.call_count)

        # Verify that the login was attempted with the correct parameters
        for request_call, payload_key in zip(request_mock.call_args_list, payload_keys):
            self.assertEqual(
                (
                    "POST",
                    "https://otrs.example.com/otrs/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session",
                ),
                request_call.args,
            )
            self.assertIn(payload_key, json.loads(request_call.kwargs.get("data")))
        self.assertEqual(session_key, self.connection.client.client._session_key)

        # Session is cleared after every call so a stale token is never reused
        client = self.connection.client.client
        self.assertIsNone(client.session_id_store.value)
        self.assertIsNone(client.result_json)
        self.assertEqual([], client.result)

    @parameterized.expand(
        [
            # Wrong credentials, reported by OTRS in the body
            ("auth_failure", ["session_error"], 200, "SessionCreate: Authorization failing!"),
            # Both login styles reply with nothing usable
            ("unknown_reply", ["empty", "empty"], 200, "OTRS returned neither an access token nor a session ID"),
            # Server-side failure before any login reply is parsed
            ("http_error", ["empty"], 500, "HTTP Status Code: 500"),
        ]
    )
    @patch("requests.request")
    def test_failure(
        self, _name: str, replies: list[str], status_code: int, data: str, request_mock: MagicMock
    ) -> None:
        # Setup mock to return different responses for each call
        request_mock.side_effect = [Util.response(reply, status_code) for reply in replies]

        # This should fail with a ConnectionTestException
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()

        # Verify the exception data
        self.assertEqual(SESSION_CAUSE, context.exception.cause)
        self.assertEqual(SESSION_ASSISTANCE, context.exception.assistance)
        self.assertIn(data, str(context.exception.data))
