import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.get_users import GetUsers
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetUsers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUsers())

    @parameterized.expand(Util.load_parameters("get_users").get("parameters"))
    def test_get_users(self, mock_request, name, expected):
        actual = self.action.run()
        self.assertEqual(actual, expected)
