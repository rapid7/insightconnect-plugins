import sys
import os
from unittest import TestCase
from icon_google_directory.actions.suspend_user import SuspendUser
from icon_google_directory.actions.suspend_user.schema import Input, Output
from unit_test.util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


class TestSuspendUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SuspendUser())

    @parameterized.expand([["success", "user@example.com", True]])
    def test_suspend_user(self, name, email, expected):
        actual = self.action.run({Input.EMAIL: email})
        expected = {Output.SUCCESS: expected}
        self.assertEqual(actual, expected)
