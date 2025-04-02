from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.force_password_reset import ForcePasswordReset
from komand_active_directory_ldap.actions.force_password_reset.schema import (
    Input,
    Output,
)

from common import MockConnection, MockServer, default_connector


class TestActionForcePasswordReset(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ForcePasswordReset())
    def test_force_password_reset(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ForcePasswordReset())
    def test_force_password_reset_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {Input.DISTINGUISHED_NAME: "CN=LDAPInvalidDnError,DC=example,DC=com"}
            )

        self.assertEqual("LDAP returned an error.", context.exception.cause)
        self.assertEqual(
            "Error was returned when trying to force password reset for this user.",
            context.exception.assistance,
        )
