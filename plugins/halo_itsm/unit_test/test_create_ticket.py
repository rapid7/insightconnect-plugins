import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_halo_itsm.actions.create_ticket import CreateTicket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, CLEAN_TICKET, LOGGER_NAME, RAW_TICKET, MockResponse, Util, token_response


class TestCreateTicket(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateTicket())

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_TICKET]))
    def test_create_ticket(self, mock_request: MagicMock, _mock_post: MagicMock) -> None:
        params = {
            "summary": "Server is unresponsive",
            "tickettype_id": 1,
            "details": "Details",
            "client_id": 5,
            "user_id": 10,
            "site_id": 2,
        }
        result = self.action.run(params)

        self.assertEqual({"ticket": CLEAN_TICKET}, result)
        self.assertEqual(("POST", f"{BASE_URL}/api/tickets"), mock_request.call_args.args)
        self.assertEqual([params], mock_request.call_args.kwargs["json"])

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_TICKET]))
    def test_create_ticket_leaves_out_empty_and_zero_values(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        # Workflows send 0 for every optional id they do not set; Halo must not receive them.
        params = {
            "summary": "Server is unresponsive",
            "tickettype_id": 1,
            "agent_id": 0,
            "category_1": "",
            "category_2": "",
            "client_id": 0,
            "details": "",
            "impact": 0,
            "priority_id": 0,
            "site_id": 0,
            "status_id": 0,
            "urgency": 0,
            "user_id": 0,
        }
        self.action.run(params)

        self.assertEqual(
            [{"summary": "Server is unresponsive", "tickettype_id": 1}], mock_request.call_args.kwargs["json"]
        )

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(201, [RAW_TICKET]))
    def test_create_ticket_does_not_log_the_summary(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertLogs(LOGGER_NAME, level="INFO") as captured:
            self.action.run({"summary": "Confidential summary text", "tickettype_id": 1})

        self.assertNotIn("Confidential summary text", "\n".join(captured.output))

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(400, text="Please select a valid Client/Site/User"))
    def test_create_ticket_bad_request(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({"summary": "Server is unresponsive", "tickettype_id": 1})

        self.assertEqual("Bad request sent to the Halo ITSM API.", context.exception.cause)
        self.assertEqual("Please select a valid Client/Site/User", context.exception.data)
