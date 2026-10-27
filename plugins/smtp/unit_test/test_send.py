import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any
from email import message_from_string
from smtplib import SMTPException, SMTPRecipientsRefused, SMTPSenderRefused
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate
from parameterized import parameterized

from komand_smtp.actions.send import Send
from komand_smtp.actions.send.schema import Input
from util import DECODED_CONTENT, Util

SEND_PARAMS = {
    Input.EMAIL_FROM: "user@example.com",
    Input.EMAIL_TO: "recipient@example.com",
    Input.SUBJECT: "Subject",
    Input.MESSAGE: "Message",
    Input.HTML: False,
}


@patch("komand_smtp.connection.connection.SMTP")
class TestSend(TestCase):
    def setUp(self) -> None:
        self.action = Send()

    def _send(self, smtp_mock: MagicMock, extra_parameters: dict[str, Any]) -> list[object]:
        client = smtp_mock.return_value
        self.action.connection = Util.mock_connection(smtp_mock)
        result = self.action.run({**SEND_PARAMS, **extra_parameters})
        validate(result, self.action.output.schema)
        self.assertEqual({"result": "ok"}, result)
        client.quit.assert_called_once()
        message = message_from_string(client.sendmail.call_args[0][2])
        return [part for part in message.get_payload() if part.get_filename()]

    @parameterized.expand(
        [
            ("no_attachment", {}, []),
            ("empty_list", {Input.ATTACHMENTS: []}, []),
            ("empty_entry", {Input.ATTACHMENTS: [{}]}, []),
            ("single_attachment", {Input.ATTACHMENTS: [Util.file("a.txt")]}, ["a.txt"]),
            (
                "multiple",
                {Input.ATTACHMENTS: [Util.file("a.txt"), Util.file("b.txt"), Util.file("c.txt")]},
                ["a.txt", "b.txt", "c.txt"],
            ),
            (
                "skips_empty_content",
                {Input.ATTACHMENTS: [Util.file("a.txt"), Util.file("empty.txt", ""), {}]},
                ["a.txt"],
            ),
            (
                "whitespace_only_content_skipped",
                {Input.ATTACHMENTS: [Util.file("a.txt"), Util.file("ws.txt", " \n ")]},
                ["a.txt"],
            ),
            ("nbsp_kept_in_filename", {Input.ATTACHMENTS: [Util.file("a\u00a0b.txt")]}, ["a\u00a0b.txt"]),
            ("filename_with_spaces", {Input.ATTACHMENTS: [Util.file("my report.txt")]}, ["my report.txt"]),
        ]
    )
    def test_attachments(
        self, smtp_mock: MagicMock, _name: str, parameters: dict[str, Any], expected: list[str]
    ) -> None:
        parts = self._send(smtp_mock, parameters)
        self.assertEqual(expected, [part.get_filename() for part in parts])
        for part in parts:
            self.assertEqual(DECODED_CONTENT, part.get_payload(decode=True))

    def test_filename_is_quoted(self, smtp_mock: MagicMock) -> None:
        parts = self._send(smtp_mock, {Input.ATTACHMENTS: [Util.file("my report.txt")]})
        self.assertIn('filename="my report.txt"', parts[0]["Content-Disposition"])

    @parameterized.expand(
        [
            ("cc_and_bcc", {Input.CC: ["cc@example.com"], Input.BCC: ["bcc@example.com"]}),
            ("blank_entries_dropped", {Input.CC: ["", " cc@example.com "], Input.BCC: ["  ", "bcc@example.com"]}),
        ]
    )
    def test_recipients(self, smtp_mock: MagicMock, _name: str, parameters: dict[str, Any]) -> None:
        self._send(smtp_mock, parameters)
        self.assertEqual(
            ["recipient@example.com", "cc@example.com", "bcc@example.com"],
            smtp_mock.return_value.sendmail.call_args[0][1],
        )

    @parameterized.expand(
        [
            ("single", {Input.ATTACHMENTS: [Util.file("bad.txt", "not base64!")]}, "attachments[0]"),
            (
                "label_points_to_input_entry",
                {Input.ATTACHMENTS: [Util.file("a.txt"), Util.file("bad.txt", "!!")]},
                "attachments[1]",
            ),
        ]
    )
    def test_invalid_base64(self, smtp_mock: MagicMock, _name: str, parameters: dict[str, Any], label: str) -> None:
        with self.assertRaises(PluginException) as context:
            self._send(smtp_mock, parameters)
        self.assertEqual(f"Content of {label} is not valid Base64.", context.exception.cause)
        self.assertNotIn("bad.txt", str(context.exception))
        smtp_mock.return_value.sendmail.assert_not_called()

    @parameterized.expand(
        [
            ("smtp_exception", SMTPException("boom"), SEND_PARAMS),
            (
                "non_ascii_address",
                UnicodeEncodeError("ascii", "jöhn", 1, 2, "ordinal not in range"),
                {**SEND_PARAMS, Input.EMAIL_TO: "jöhn@example.com"},
            ),
        ]
    )
    def test_send_failure(self, smtp_mock: MagicMock, _name: str, error: Exception, parameters: dict[str, Any]) -> None:
        client = smtp_mock.return_value
        client.sendmail.side_effect = error
        self.action.connection = Util.mock_connection(smtp_mock)
        with self.assertRaises(PluginException) as context:
            self.action.run(parameters)
        self.assertEqual("Failed to send the email.", context.exception.cause)
        client.quit.assert_called_once()

    @parameterized.expand(
        [
            (
                "recipients_refused",
                {"side_effect": SMTPRecipientsRefused({"secret@example.com": (550, b"no such user")})},
                "Failed to send the email.",
                "SMTP codes: 550",
            ),
            (
                "sender_refused",
                {"side_effect": SMTPSenderRefused(553, b"bad sender", "secret@example.com")},
                "Failed to send the email.",
                "SMTP code: 553",
            ),
            (
                "partially_refused",
                {"return_value": {"secret@example.com": (452, b"Too many recipients")}},
                "The SMTP server refused some of the recipients.",
                "SMTP codes: 452",
            ),
        ]
    )
    def test_send_failure_hides_addresses(
        self, smtp_mock: MagicMock, _name: str, sendmail_kwargs: dict[str, Any], cause: str, expected: str
    ) -> None:
        client = smtp_mock.return_value
        self.action.connection = Util.mock_connection(smtp_mock)
        client.sendmail.configure_mock(**sendmail_kwargs)
        with self.assertRaises(PluginException) as context:
            self.action.run(SEND_PARAMS)
        self.assertEqual(cause, context.exception.cause)
        self.assertIn(expected, context.exception.data)
        self.assertNotIn("secret@example.com", context.exception.data)
        client.quit.assert_called_once()

    def test_connection_failure(self, smtp_mock: MagicMock) -> None:
        self.action.connection = MagicMock()
        self.action.connection.get.side_effect = PluginException(cause="Unable to connect.", assistance="Check host.")
        with self.assertRaises(PluginException) as context:
            self.action.run(SEND_PARAMS)
        self.assertEqual("Unable to connect.", context.exception.cause)

    def test_header_injection_fails_before_connecting(self, smtp_mock: MagicMock) -> None:
        self.action.connection = Util.mock_connection(smtp_mock)
        with self.assertRaises(PluginException) as context:
            self.action.run({**SEND_PARAMS, Input.SUBJECT: "x\r\nBcc: evil@example.com"})
        self.assertEqual("Failed to build the email.", context.exception.cause)
        self.action.connection.get.assert_not_called()

    @parameterized.expand(
        [
            ("long_ascii", "a" * 1200 + ".txt", 255, ".txt"),
            ("long_non_ascii", "й" * 300 + ".pdf", None, ".pdf"),
            ("long_extension", "b" * 300 + "." + "c" * 50, 255, None),
        ]
    )
    def test_long_filename_is_capped(
        self, smtp_mock: MagicMock, _name: str, filename: str, expected_length: int, extension: str | None
    ) -> None:
        parts = self._send(smtp_mock, {Input.ATTACHMENTS: [Util.file(filename)]})
        received = parts[0].get_filename()
        self.assertLessEqual(len(received), 255)
        self.assertLess(max(len(line) for line in parts[0]["Content-Disposition"].splitlines()), 998)

        # If expected_length is set, check that the filename has that length
        if expected_length:
            self.assertEqual(expected_length, len(received))

        # If extension is set, check that the filename ends with that extension
        if extension:
            self.assertTrue(received.endswith(extension))
