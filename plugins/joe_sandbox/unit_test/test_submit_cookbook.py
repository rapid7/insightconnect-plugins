import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.submit_cookbook import SubmitCookbook
from icon_joe_sandbox.actions.submit_cookbook.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestSubmitCookbook(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SubmitCookbook())
        self.params = {
            Input.COOKBOOK: "bytesbytesbytesbytesbytesbytesbytesbytes",
            Input.PARAMETERS: "",
            Input.ADDITIONAL_PARAMETERS: "",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_submit_cookbook(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run()

        expected = {Output.SUBMISSION_ID: "abc"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
