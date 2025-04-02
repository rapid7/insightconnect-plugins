from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.modify_groups import ModifyGroups
from komand_active_directory_ldap.actions.modify_groups.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionModifyGroups(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyGroups())
    def test_add_group(self, action):
        actual = action.run(
            {
                Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com",
                Input.GROUP_DN: "CN=Group,DC=example,DC=com",
                Input.ADD_REMOVE: "add",
            }
        )
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyGroups())
    def test_remove_group(self, action):
        actual = action.run(
            {
                Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com",
                Input.GROUP_DN: "CN=Group,DC=example,DC=com",
                Input.ADD_REMOVE: "remove",
            }
        )
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyGroups())
    def test_modify_group_group_not_found(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com",
                    Input.GROUP_DN: "CN=empty_group,DC=example,DC=com",
                }
            )

        self.assertEqual(
            "Either the user or group distinguished name was not found.",
            context.exception.cause,
        )
        self.assertEqual(
            "Please check that the distinguished names are correct",
            context.exception.assistance,
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyGroups())
    def test_modify_group_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.DISTINGUISHED_NAME: "CN=LDAPInvalidDnError,DC=example,DC=com",
                    Input.GROUP_DN: "CN=Group,DC=example,DC=com",
                }
            )

        self.assertEqual("The DN was not found.", context.exception.cause)
        self.assertEqual(
            "The DN CN=LDAPInvalidDnError,DC=example,DC=com was not found.",
            context.exception.assistance,
        )
