import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.connection.connection import Connection
from komand_samanage.actions.create_user import CreateUser
from unit_test.util import Util, mock_request_200
from unittest.mock import patch
from parameterized import parameterized


@patch("komand_samanage.util.api.request", side_effect=mock_request_200)
class TestCreateUser(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateUser())

    @parameterized.expand(Util.load_parameters("create_user").get("parameters"))
    def test_create_user(self, mock_request, email, name, phone, mobile_phone, role, department, expected):
        actual = self.action.run(
            {
                "email": email,
                "name": name,
                "phone": phone,
                "mobile_phone": mobile_phone,
                "role": role,
                "department": department,
            }
        )
        self.assertEqual(actual, expected)
