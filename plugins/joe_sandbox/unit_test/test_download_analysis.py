import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.download_analysis import DownloadAnalysis
from icon_joe_sandbox.actions.download_analysis.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestDownloadAnalysis(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DownloadAnalysis())
        self.params = {Input.WEBID: "abc", Input.TYPE: "html", Input.RUN: 0}

    @patch("requests.request", side_effect=mock_request_200)
    def test_download_analysis(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run()

        expected = {Output.RESOURCE_NAME: "name", Output.RESOURCE_CONTENT: "content"}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
