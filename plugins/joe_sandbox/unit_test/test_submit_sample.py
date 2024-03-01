import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.submit_sample import SubmitSample
from icon_joe_sandbox.actions.submit_sample.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestSubmitSample(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SubmitSample())
        self.params = {
            Input.SAMPLE: b'ZGhkCg==',
            Input.PARAMETERS: "",
            Input.COOKBOOK: "",
            Input.ADDITIONAL_PARAMETERS: "",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_submit_sample(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run()

        expected = {Output.WEBIDS: ["abc", "def"]}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
