from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.add_user import AddUser
from komand_active_directory_ldap.actions.add_user.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionAddUser(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=AddUser())
    def test_add_user(self, action):
        actual = action.run(
            {
                Input.DOMAIN_NAME: "example.com",
                Input.FIRST_NAME: "firstname",
                Input.LAST_NAME: "lastname",
                Input.USER_OU: "CN=Users",
            }
        )
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=AddUser())
    def test_add_user_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DOMAIN_NAME: "example.com",
                    Input.FIRST_NAME: "firstname",
                    Input.LAST_NAME: "lastname",
                    Input.USER_OU: "CN=Users",
                    Input.ADDITIONAL_PARAMETERS: {"run_error": True},
                }
            )

        self.assertTrue("LDAP returned an error message." in context.exception.cause)
        self.assertTrue(
            "Creating new user failed, error returned by LDAP."
            in context.exception.assistance
        )
