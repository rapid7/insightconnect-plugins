import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.add_file_to_udso_list import AddFileToUdsoList
from icon_trendmicro_apex.actions.add_file_to_udso_list.schema import Input, Output
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestAddFileToUdsoList(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(AddFileToUdsoList())
        self.params = {
            Input.FILE: {"filename": "", "content": ""},
            Input.SCAN_ACTION: "QUARANTINE",
            Input.DESCRIPTION: "File Blacklisted from InsightConnect",
        }

    @patch("requests.request", side_effect=mock_request_200)
    def test_add_file_to_usdo_list(self, mock_put, mock_token):
        mocked_request(mock_put)
        response = self.action.run(self.params)

        expected = {Output.SUCCESS: True}
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
