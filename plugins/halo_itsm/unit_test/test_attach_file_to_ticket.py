import base64
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.attach_file_to_ticket import AttachFileToTicket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, MockResponse, Util, token_response

CONTENT = base64.b64encode(b"Name,Severity\r\nweb-01,High\r\n").decode("ascii")
RAW_ATTACHMENT = {"id": 77, "ticket_id": 101}


class TestAttachFileToTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AttachFileToTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ATTACHMENT]))
    def test_attach_file_to_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run({"ticket_id": 101, "filename": "report.txt", "content": CONTENT})

        self.assertEqual({"action": {"id": 77, "ticket_id": 101}}, result)
        self.assertEqual(("POST", f"{BASE_URL}/api/Attachment"), mock_request.call_args.args)
        # Halo wants a data URI; raw base64 makes it answer HTTP 500
        self.assertEqual(
            [{"ticket_id": 101, "filename": "report.txt", "data_base64": f"data:text/plain;base64,{CONTENT}"}],
            mock_request.call_args.kwargs["json"],
        )

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ATTACHMENT]))
    def test_attach_file_to_ticket_unknown_type_is_octet_stream(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        self.action.run({"ticket_id": 101, "filename": "report.unknown-extension", "content": CONTENT})

        sent = mock_request.call_args.kwargs["json"][0]["data_base64"]
        self.assertEqual(f"data:application/octet-stream;base64,{CONTENT}", sent)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ATTACHMENT]))
    def test_attach_file_to_ticket_strips_line_breaks(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        # The CSV plugin wraps its base64 every 76 characters; Halo rejects the line breaks
        wrapped = base64.encodebytes(b"x" * 200).decode("ascii")
        self.assertIn("\n", wrapped)
        unwrapped = "".join(wrapped.split())

        self.action.run({"ticket_id": 101, "filename": "report.txt", "content": wrapped})

        sent = mock_request.call_args.kwargs["json"][0]["data_base64"]
        self.assertEqual(f"data:text/plain;base64,{unwrapped}", sent)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ATTACHMENT]))
    def test_attach_file_to_ticket_keeps_a_data_uri_header(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        self.action.run({"ticket_id": 101, "filename": "report.csv", "content": f"data:text/csv;base64,{CONTENT}"})

        sent = mock_request.call_args.kwargs["json"][0]["data_base64"]
        self.assertEqual(f"data:text/csv;base64,{CONTENT}", sent)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ATTACHMENT]))
    def test_attach_file_to_ticket_accepts_but_does_not_send_note_and_hidden_flag(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        # Existing workflows still pass both; Halo attachments have neither
        self.action.run(
            {
                "ticket_id": 101,
                "filename": "report.txt",
                "content": CONTENT,
                "note": "Full list",
                "hiddenfromuser": True,
            }
        )

        self.assertEqual({"ticket_id", "filename", "data_base64"}, set(mock_request.call_args.kwargs["json"][0].keys()))

    @patch("requests.Session.request")
    @patch("requests.post", return_value=token_response())
    def test_attach_file_to_ticket_rejects_invalid_base64(self, _mock_post: MagicMock, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({"ticket_id": 101, "filename": "report.txt", "content": "not base64 !!"})

        self.assertEqual("Failed to decode file content.", context.exception.cause)
        mock_request.assert_not_called()
