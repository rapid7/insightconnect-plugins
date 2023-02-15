import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.list_incidents import ListIncidents
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from komand_samanage.connection.schema import Input
from parameterized import parameterized


@patch('komand_samanage.util.api.request', side_effect=mock_request_200)
class TestListIncidents(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListIncidents())

    @parameterized.expand(Util.load_parameters("list_incidents").get("parameters"))
    def test_list_incidents(self, mock_request, expected):

        actual = self.action.run()
        self.assertEqual(actual, expected)
