import sys
import os

from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
from unittest import mock
from unittest import TestCase
from carbon_black_response.icon_carbon_black_response.actions.list_sensors.schema import Input
from carbon_black_response.icon_carbon_black_response.actions.list_sensors import ListSensors


class TestListSensors(TestCase):
    def setUp(self):
        self.action = ListSensors()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.carbon_black = self.mock_client

        self.params_data = {
            Input.ID: "1234",
            Input.HOSTNAME: "cb-response-example",
            Input.IP: "192.0.2.0",
            Input.GROUPID: "50",
        }

    @mock.patch("icon_carbon_black_response.connection.connection.Connection")
    def test_list_sensors_success(self, mock_connection):
        mock_connection.carbon_black = self.mock_client
        self.mock_client.get_object.return_value = {"computer_name": "cb-response-example", "found": True}
        response = self.action.run(self.params_data)
        expected_response = {"sensors": [{"computer_name": "cb-response-example", "found": True}]}
        self.assertEqual(expected_response, response)
