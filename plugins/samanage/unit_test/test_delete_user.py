import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.delete_user import DeleteUser
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestDeleteUser(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DeleteUser())

    @parameterized.expand(Util.load_parameters("delete_user").get("parameters"))
    def test_delete_user(self, mock_request, user_id, expected):
        actual = self.action.run({"user_id": user_id})
        self.assertEqual(actual, expected)
