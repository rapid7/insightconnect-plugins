import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.list_tickets import ListTickets

from util import BASE_URL, CLEAN_TICKET, LOGGER_NAME, RAW_TICKET, MockResponse, Util, token_response


class TestListTickets(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListTickets())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, {"tickets": [RAW_TICKET, RAW_TICKET]}))
    def test_list_tickets(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        result = self.action.run({"status_id": 1, "agent_id": 15, "search": "unresponsive", "count": 10})

        self.assertEqual({"tickets": [CLEAN_TICKET, CLEAN_TICKET]}, result)
        self.assertEqual(("GET", f"{BASE_URL}/api/tickets"), mock_request.call_args.args)
        self.assertEqual(
            {"count": 10, "status_id": 1, "agent_id": 15, "search": "unresponsive"},
            mock_request.call_args.kwargs["params"],
        )

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, [RAW_TICKET]))
    def test_list_tickets_accepts_a_plain_list_and_defaults_the_count(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        result = self.action.run({})

        self.assertEqual({"tickets": [CLEAN_TICKET]}, result)
        self.assertEqual({"count": 50}, mock_request.call_args.kwargs["params"])

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, {"records": []}))
    def test_list_tickets_reads_the_records_key(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        self.assertEqual({"tickets": []}, self.action.run({}))

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, {"tickets": []}))
    def test_list_tickets_does_not_log_the_search_term(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            self.action.run({"search": "confidential search term"})

        self.assertNotIn("confidential search term", "\n".join(captured.output))
