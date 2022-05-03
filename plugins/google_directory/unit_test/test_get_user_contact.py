import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_google_directory.actions.get_user_contact import GetUserContact
from icon_google_directory.actions.get_user_contact.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

STUB_ACTION_OUTPUT = {
    "contact": {
        "addresses": [
            {"country": "England", "street": "1 Test street"},
            {
                "country": "England",
                "postal_code": "31-222",
            },
            {"country": "England", "postal_code": "31-111", "street": "3 Test street"},
            {"postal_code": "31-333", "street": "4 Test street"},
        ],
        "phone_numbers": ["111111111", "222222222", "333333333"],
        "email_addresses": ["user@example.com", "user2@example.com", "user@example2.com"],
    }
}


class TestGetUserContact(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserContact())

    @parameterized.expand([["user@example.com", STUB_ACTION_OUTPUT]])
    def test_get_user_contact(self, email, expected):
        response = self.action.run({Input.EMAIL: email})
        self.assertEqual(response, expected)
