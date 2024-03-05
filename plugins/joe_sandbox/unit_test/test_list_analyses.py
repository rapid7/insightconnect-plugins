import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_joe_sandbox.actions.list_analyses import ListAnalyses
from icon_joe_sandbox.actions.list_analyses.schema import Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request, MagicMock


class TestListAnalyses(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListAnalyses())

    @patch("requests.request", side_effect=mock_request_200)
    def test_list_analyses(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run()

        expected = {Output.ANALYSES: [{"webid": "1"}, {"webid": "2"}, {"webid": "3"}, {"webid": "4"}]}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
