import sys
import os

from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
from unittest import mock
from unittest import TestCase
from icon_carbon_black_response.actions.list_binaries.schema import Input
from icon_carbon_black_response.actions.list_binaries import ListBinaries


class TestListProcesses(TestCase):
    def setUp(self):
        self.action = ListBinaries()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.carbon_black = self.mock_client

        self.params_data = {Input.QUERY: "domain:www.carbonblack.com", Input.ROWS: 10, Input.START: 0}

    @mock.patch("icon_carbon_black_response.connection.connection.Connection")
    def test_list_binaries_success(self, mock_connection):
        mock_connection.carbon_black = self.mock_client
        self.mock_client.get_object.return_value = {
            "results": {"binaries": [{"host_count": 1}]},
            "meta_data": {"page": 1},
        }
        response = self.action.run(self.params_data)
        expected_response = {"binaries": {"binaries": [{"host_count": 1}]}}
        self.assertEqual(expected_response, response)
