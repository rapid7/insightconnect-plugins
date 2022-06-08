import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from parameterized import parameterized

from unit_test.util import Util
from komand_powershell.util.util import add_credentials_to_script
from komand_powershell.actions.powershell_string.schema import Input


class TestUtil(TestCase):
    @parameterized.expand(
        [
            ("without_credentials", "new_username", "new_password", "new_secret_key", False, "first line\nsecond line"),
            (
                "with_credentials",
                "new_username",
                "new_password",
                "new_secret_key",
                True,
                "$username = 'new_username'\n$password = 'new_password' | ConvertTo-SecureString -asPlainText -Force\n$secret_key = 'new_secret_key'\nfirst line\nsecond line",
            ),
        ]
    )
    def test_add_credentials_to_script(self, name, username, password, secret_key, add_credentials, expected):
        actual = add_credentials_to_script(
            powershell_script="first line\nsecond line",
            params={
                Input.USERNAME_AND_PASSWORD: {"username": username, "password": password},
                Input.SECRET_KEY: {"secretKey": secret_key},
                Input.ADD_CREDENTIALS_TO_SCRIPT: add_credentials,
            },
        )
        self.assertEqual(actual, expected)
