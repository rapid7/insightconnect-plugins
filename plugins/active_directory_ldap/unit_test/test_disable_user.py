from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.disable_user import DisableUser
from komand_active_directory_ldap.actions.disable_user.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionDisableUser(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUser())
    def test_disable_user(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUser())
    def test_disable_user_empty_search(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAME: "CN=empty_search,DC=example,DC=com"})

        self.assertEqual(
            "The DN CN=empty_search,DC=example,DC=com was not found.",
            context.exception.cause,
        )
        self.assertEqual(
            "Please provide a valid DN and try again.", context.exception.assistance
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUser())
    def test_disable_user_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {Input.DISTINGUISHED_NAME: "CN=LDAPInvalidDnError,DC=example,DC=com"}
            )

        self.assertEqual("The DN was not found.", context.exception.cause)
        self.assertEqual(
            "The DN CN=LDAPInvalidDnError,DC=example,DC=com was not found.",
            context.exception.assistance,
        )

        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DISTINGUISHED_NAME: "CN=LDAPOperationsErrorResult,DC=example,DC=com"
                }
            )

        self.assertEqual("Server error occurred", context.exception.cause)
        self.assertEqual(
            "Verify your plugin connection inputs are correct and not malformed and try again. "
            "If the issue persists, please contact support.",
            context.exception.assistance,
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUser())
    def test_disable_user_wrong_result(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAME: "CN=wrong_result,DC=example,DC=com"})

        self.assertEqual(
            "The DN CN=wrong_result,DC=example,DC=com was not found.",
            context.exception.cause,
        )
        self.assertEqual(
            "Please provide a valid DN and try again.", context.exception.assistance
        )
