import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from smtplib import SMTPAuthenticationError, SMTPConnectError
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from komand_smtp.connection.connection import Connection
from komand_smtp.connection.schema import Input
from util import CONNECTION_PARAMS


@patch("komand_smtp.connection.connection.SMTP")
class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger()

    @parameterized.expand(
        [
            ("ssl_with_credentials", {}, 1, [call("user", "pass")]),
            ("no_credentials", {Input.CREDENTIALS: None, Input.USE_SSL: False}, 0, []),
        ]
    )
    def test_success(
        self, smtp_mock: MagicMock, _name: str, overrides: dict, starttls_calls: int, login_calls: list
    ) -> None:
        self.connection.connect({**CONNECTION_PARAMS, **overrides})
        self.assertEqual({"success": True}, self.connection.test())
        client = smtp_mock.return_value
        self.assertEqual(starttls_calls, client.starttls.call_count)
        self.assertEqual(login_calls, client.login.call_args_list)

    @parameterized.expand(
        [
            ("auth_failure", SMTPAuthenticationError(535, b"denied"), "Authentication to the SMTP server failed."),
            ("os_error", OSError("unreachable"), "Unable to connect to the SMTP server at smtp.example.com:25."),
        ]
    )
    def test_failure(self, smtp_mock: MagicMock, _name: str, error: Exception, cause: str) -> None:
        smtp_mock.return_value.ehlo.side_effect = error
        self.connection.connect(CONNECTION_PARAMS)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(cause, context.exception.cause)
