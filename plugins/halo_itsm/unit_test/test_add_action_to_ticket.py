import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.add_action_to_ticket import AddActionToTicket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, MockResponse, Util, token_response

RAW_ACTION = {
    "id": 501,
    "ticket_id": 101,
    "who": "John Smith",
    "note": "Investigated the issue",
    "hiddenfromuser": True,
    "outcome": "Ongoing",
    "datetime": "2025-07-10T10:30:00Z",
}


class TestAddActionToTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddActionToTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ACTION]))
    def test_add_action_to_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run(
            {"ticket_id": 101, "note": "Investigated the issue", "outcome": "Ongoing", "hiddenfromuser": True}
        )

        # Halo returns the action date as "datetime"; the plugin reports it as actiondate
        self.assertEqual(
            {
                "action": {
                    "id": 501,
                    "ticket_id": 101,
                    "who": "John Smith",
                    "note": "Investigated the issue",
                    "hiddenfromuser": True,
                    "outcome": "Ongoing",
                    "actiondate": "2025-07-10T10:30:00Z",
                }
            },
            result,
        )
        self.assertEqual(("POST", f"{BASE_URL}/api/Actions"), mock_request.call_args.args)
        self.assertEqual(
            [{"hiddenfromuser": True, "note": "Investigated the issue", "outcome": "Ongoing", "ticket_id": 101}],
            mock_request.call_args.kwargs["json"],
        )

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_ACTION]))
    def test_add_action_to_ticket_with_html_note(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        self.action.run({"ticket_id": 101, "note_html": "<p>Investigated</p>"})

        self.assertEqual(
            [{"hiddenfromuser": False, "note_html": "<p>Investigated</p>", "ticket_id": 101}],
            mock_request.call_args.kwargs["json"],
        )

    @patch("requests.Session.request")
    @patch("requests.post")
    def test_add_action_to_ticket_needs_a_note(self, mock_post: MagicMock, mock_request: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({"ticket_id": 101})

        self.assertEqual("No note content provided.", context.exception.cause)
        mock_post.assert_not_called()
        mock_request.assert_not_called()
