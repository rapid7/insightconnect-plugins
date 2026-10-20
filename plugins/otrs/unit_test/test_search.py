import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema.validators import validate

from komand_otrs.actions.search import Search
from komand_otrs.actions.search.schema import Input
from komand_otrs.util.constants import SESSION_CAUSE
from util import Util

PARAMETERS = {
    Input.QUEUE: "Raw",
    Input.CUST_ID: "example-customer",
    Input.EXTERNAL_PARAMS: [{"Title": "Test Ticket"}],
}


@patch("requests.request")
class TestSearch(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Search())

    def test_search(self, request_mock: MagicMock) -> None:
        # Login, then the search itself
        request_mock.side_effect = [Util.response("access_token"), Util.response("ticket_search")]
        result = self.action.run(PARAMETERS)
        validate(result, self.action.output.schema)
        self.assertEqual({"ticket_ids": ["5", "4", "3", "2"]}, result)

        # Search is a GET, so the filters travel in the query string, not the body
        self.assertEqual(
            {
                "AccessToken": "dummy-access-token",
                "Queues": "Raw",
                "CustomerID": "example-customer",
                "Title": "Test Ticket",
            },
            request_mock.call_args.kwargs.get("params"),
        )

    def test_search_session_failure(self, request_mock: MagicMock) -> None:
        # Setup mock to return the same response for each call
        request_mock.return_value = Util.response("session_error")

        # This should fail with a PluginException
        with self.assertRaises(PluginException) as context:
            self.action.run(PARAMETERS)

        # Verify the exception data
        self.assertEqual(SESSION_CAUSE, context.exception.cause)
