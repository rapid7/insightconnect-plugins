import sys
import os
from unittest import TestCase
from icon_google_directory.actions.get_all_domain_users import GetAllDomainUsers
from icon_google_directory.actions.get_all_domain_users.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestGetAllDomainUsers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAllDomainUsers())

    @parameterized.expand(
        [
            [
                "success",
                "example.com",
                [
                    {"email": "user@example.com", "name": "Test User"},
                    {"email": "user2@example.com", "name": "Example User"},
                ],
            ],
            ["empty_list", "empty_list", []],
        ]
    )
    def test_get_all_domain_users(self, name, domain, expected):
        actual = self.action.run({Input.DOMAIN: domain})
        expected = {Output.USERS: expected}
        self.assertEqual(actual, expected)
