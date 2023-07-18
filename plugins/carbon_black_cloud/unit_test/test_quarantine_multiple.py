import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from icon_carbon_black_cloud.actions.quarantine_multiple import QuarantineMultiple
from icon_carbon_black_cloud.actions.quarantine_multiple.schema import Input, Output

from mock import mock_request_201
from util import Util

STUB_PAYLOAD = {Input.AGENTS: ["ExampleAgent", "ExampleAgent2"], Input.QUARANTINE_STATE: True, Input.WHITELIST: []}


class TestQuarantineMultiple(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(QuarantineMultiple())

    @mock.patch("requests.post", side_effect=mock_request_201)
    def test_quarantine_multiple(self, mock_post: Mock) -> None:
        response = self.action.run(STUB_PAYLOAD)
        expected = {
            Output.COMPLETED: ["ExampleAgent"],
            Output.FAILED: [
                {
                    "error": "An error occurred during plugin execution!\n"
                    "\n"
                    "The object referenced in the request cannot be found. "
                    "Verify that your request contains objects that "
                    "haven’t been deleted. Verify that the organization "
                    "key in the URL is correct.",
                    "input_key": "ExampleAgent2",
                }
            ],
        }
        self.assertEqual(response, expected)
        mock_post.assert_called()
