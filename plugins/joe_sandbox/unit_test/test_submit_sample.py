import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.submit_sample.action import SubmitSample
from icon_joe_sandbox.actions.submit_sample.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestSubmitSample(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(SubmitSample())
        self.params = {
            Input.FILENAME: "test.csv",
            Input.SAMPLE: "VGVzdA==",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_submit_sample(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)
        expected = {Output.SUBMISSION_ID: "12345"}

        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
