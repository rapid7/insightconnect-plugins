import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_google_directory.actions.unsuspend_user import UnsuspendUser
from icon_google_directory.actions.unsuspend_user.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized


class TestUnsuspendUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UnsuspendUser())

    @parameterized.expand([["success", "user@example.com", True]])
    def test_unsuspend_user(self, name, email, expected):
        actual = self.action.run({Input.EMAIL: email})
        expected = {Output.SUCCESS: expected}
        self.assertEqual(actual, expected)
