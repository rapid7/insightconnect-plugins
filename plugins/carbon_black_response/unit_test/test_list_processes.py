import sys
import os

from unittest.mock import MagicMock

sys.path.append(os.path.abspath("../"))
from unittest import mock
from unittest import TestCase

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_carbon_black_response.actions.list_processes.schema import Input
from icon_carbon_black_response.connection.connection import Connection
from icon_carbon_black_response.actions.list_processes import ListProcesses
import json
import logging


class TestListProcesses(TestCase):
    def setUp(self):
        self.action = ListProcesses()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.carbon_black = self.mock_client

        self.params_data = {Input.QUERY: "www.carbonblack.com", Input.ROWS: 10, Input.START: 0}

    @mock.patch("icon_carbon_black_response.connection.connection.Connection")
    def test_list_processes_success(self, mock_connection):
        mock_connection.carbon_black = self.mock_client
        self.mock_client.get_object.return_value = {"results": {}}
        response = self.action.run(self.params_data)
        expected_response = {"processes": {}}
        self.assertEqual(expected_response, response)
