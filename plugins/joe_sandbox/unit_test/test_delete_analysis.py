import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.delete_analysis import DeleteAnalysis
from icon_joe_sandbox.actions.delete_analysis.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestDeleteAnalysis(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DeleteAnalysis())
        self.params = {Input.WEBID: "abc"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_delete_analysis(self, mock_delete):
        mocked_request(mock_delete)
        response = self.action.run()

        expected = {Output.DELETED: "abc"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
