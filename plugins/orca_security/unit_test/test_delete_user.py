import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.delete_user import DeleteUser
from icon_orca_security.actions.delete_user.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestDeleteUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteUser())

    @parameterized.expand(Util.load_parameters("delete_user").get("parameters"))
    def test_delete_user(self, mock_request, name, email, expected):
        actual = self.action.run({Input.DELETE_INVITE_EMAIL: email})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("delete_user_bad").get("parameters"))
    def test_delete_user_bad(self, mock_request, name, email, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.DELETE_INVITE_EMAIL: email})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
