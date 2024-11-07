import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.add_user import AddUser
from icon_orca_security.actions.add_user.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestAddUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddUser())

    @parameterized.expand(Util.load_parameters("add_user").get("parameters"))
    def test_add_user(
        self, mock_request, name, email, role, all_cloud_accounts, cloud_accounts, should_send_email, expected
    ):
        actual = self.action.run(
            {
                Input.INVITE_USER_EMAIL: email,
                Input.ROLE: role,
                Input.ALL_CLOUD_ACCOUNTS: all_cloud_accounts,
                Input.CLOUD_ACCOUNTS: cloud_accounts,
                Input.SHOULD_SEND_EMAIL: should_send_email,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("add_user_bad").get("parameters"))
    def test_add_user_bad(
        self, mock_request, name, email, role, all_cloud_accounts, cloud_accounts, should_send_email, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.INVITE_USER_EMAIL: email,
                    Input.ROLE: role,
                    Input.ALL_CLOUD_ACCOUNTS: all_cloud_accounts,
                    Input.CLOUD_ACCOUNTS: cloud_accounts,
                    Input.SHOULD_SEND_EMAIL: should_send_email,
                }
            )
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
