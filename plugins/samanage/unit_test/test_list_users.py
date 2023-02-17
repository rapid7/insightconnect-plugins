import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.list_users import ListUsers
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestListUsers(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListUsers())

    @parameterized.expand(Util.load_parameters("list_users").get("parameters"))
    def test_list_users(self, mock_request, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
