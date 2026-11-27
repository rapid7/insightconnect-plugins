import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

import requests
from icon_halo_itsm.util.api import HaloItsmApi
from icon_halo_itsm.util.helpers import clean_action, clean_ticket
from insightconnect_plugin_runtime.exceptions import PluginException

from util import BASE_URL, CLEAN_TICKET, LOGGER_NAME, RAW_TICKET, MockResponse, token_response


class TestHaloItsmApi(TestCase):
    def setUp(self) -> None:
        self.api = HaloItsmApi(BASE_URL, "client-id", "client-secret", "", logging.getLogger(LOGGER_NAME))

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", side_effect=[MockResponse(401, text="expired"), MockResponse(200, RAW_TICKET)])
    def test_an_expired_token_is_renewed_once(self, mock_request: MagicMock, mock_post: MagicMock) -> None:
        self.assertEqual(101, self.api.get_ticket(101)["id"])

        self.assertEqual(2, mock_post.call_count)
        self.assertEqual(2, mock_request.call_count)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(401, text="still unauthorised"))
    def test_a_second_401_is_reported_and_not_retried_again(
        self, mock_request: MagicMock, _mock_post: MagicMock
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.api.get_ticket(101)

        self.assertEqual("Invalid credentials provided.", context.exception.cause)
        self.assertEqual(2, mock_request.call_count)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(418, text="teapot"))
    def test_an_unlisted_status_code_is_named(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.api.get_ticket(101)

        self.assertEqual("Unexpected status code: 418.", context.exception.cause)
        self.assertEqual("teapot", context.exception.data)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, text="<html>not json</html>"))
    def test_a_body_that_is_not_json_is_reported(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException) as context:
            self.api.get_ticket(101)

        self.assertEqual("<html>not json</html>", context.exception.data)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", side_effect=requests.exceptions.Timeout())
    def test_a_timeout_is_reported(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        with self.assertRaises(PluginException):
            self.api.get_ticket(101)

    @patch("requests.post", return_value=token_response())
    @patch("requests.Session.request", return_value=MockResponse(200, [RAW_TICKET]))
    def test_update_ticket_leaves_the_callers_dict_alone(self, _mock_request: MagicMock, _mock_post: MagicMock) -> None:
        ticket_data = {"summary": "New summary"}

        self.api.update_ticket(101, ticket_data)

        self.assertEqual({"summary": "New summary"}, ticket_data)


class TestHelpers(TestCase):
    def test_clean_ticket_drops_none_and_unknown_fields(self) -> None:
        self.assertEqual(CLEAN_TICKET, clean_ticket(RAW_TICKET))

    def test_clean_ticket_of_nothing_is_empty(self) -> None:
        self.assertEqual({}, clean_ticket({}))
        self.assertEqual({}, clean_ticket(None))

    def test_clean_action_reads_the_date_from_datetime(self) -> None:
        self.assertEqual(
            {"id": 1, "actiondate": "2025-07-10T10:30:00Z"}, clean_action({"id": 1, "datetime": "2025-07-10T10:30:00Z"})
        )

    def test_clean_action_prefers_actiondate(self) -> None:
        raw_action = {"actiondate": "2025-07-11T08:00:00Z", "datetime": "2025-07-10T10:30:00Z"}

        self.assertEqual({"actiondate": "2025-07-11T08:00:00Z"}, clean_action(raw_action))
