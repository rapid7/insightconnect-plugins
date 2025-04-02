from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.reset_password import ResetPassword
from komand_active_directory_ldap.actions.reset_password.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionResetPassword(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ResetPassword())
    def test_reset_password(self, action):
        actual = action.run(
            {
                Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com",
                Input.NEW_PASSWORD: "test_pass",
            }
        )
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ResetPassword())
    def test_reset_password_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DISTINGUISHED_NAME: "CN=LDAPInvalidDnError,DC=example,DC=com",
                    Input.NEW_PASSWORD: "test_pass",
                }
            )

        self.assertEqual(
            "LDAP returned an error in the response.", context.exception.cause
        )
        self.assertEqual(
            "LDAP failed to reset the password for this user",
            context.exception.assistance,
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ResetPassword())
    def test_reset_password_raise_when_ssl_false(self, action):
        action.connection.use_ssl = False
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com",
                    Input.NEW_PASSWORD: "test_pass",
                }
            )

        self.assertEqual("SSL must be enabled", context.exception.cause)
        self.assertEqual(
            "SSL must be enabled for the reset password action",
            context.exception.assistance,
        )
