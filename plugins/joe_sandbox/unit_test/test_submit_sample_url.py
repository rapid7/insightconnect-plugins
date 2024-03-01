import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.submit_sample_url import SubmitSampleUrl
from icon_joe_sandbox.actions.submit_sample_url.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestSubmitSampleUrl(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SubmitSampleUrl())
        self.params = {
            Input.SAMPLE_URL: "https://www.example.com",
            Input.PARAMETERS: "",
            Input.ADDITIONAL_PARAMETERS: "",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_submit_sample_url(self, mock_post):
        mocked_request(mock_post)
        response = self.action.run()

        expected = {Output.SUBMISSION_ID: "abc"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
