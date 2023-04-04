from unittest import TestCase, mock
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.disable_users import DisableUsers
from komand_active_directory_ldap.actions.disable_users.schema import Input, Output
from unit_test.common import MockServer
from unit_test.common import MockConnection
from unit_test.common import default_connector


class TestActionDisableUsers(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUsers())
    def test_disable_users(self, action):
        actual = action.run({Input.DISTINGUISHED_NAMES: ["CN=Users,DC=example,DC=com"]})
        expected = {
            Output.SUCCESS: True,
            Output.SUCCESSFUL_DISABLEMENTS: ["CN=Users,DC=example,DC=com"],
            Output.UNSUCCESSFUL_DISABLEMENTS: [],
        }
        self.assertEqual(expected, actual)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUsers())
    def test_disable_user_empty_search(self, action):
        actual = action.run({Input.DISTINGUISHED_NAMES: ["CN=empty_search,DC=example,DC=com"]})
        expected = {
            Output.UNSUCCESSFUL_DISABLEMENTS: [
                {
                    "dn": "CN=empty_search,DC=example,DC=com",
                    "error": "The DN CN=empty_search,DC=example,DC=com was not found.",
                }
            ],
            Output.SUCCESSFUL_DISABLEMENTS: [],
            Output.SUCCESS: False,
        }
        self.assertEqual(expected, actual)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUsers())
    def test_disable_user_success_and_failure_search(self, action):
        actual = action.run(
            {Input.DISTINGUISHED_NAMES: ["CN=empty_search,DC=example,DC=com", "CN=Users,DC=example," "DC=com"]}
        )
        expected = {
            Output.UNSUCCESSFUL_DISABLEMENTS: [
                {
                    "dn": "CN=empty_search,DC=example,DC=com",
                    "error": "The DN CN=empty_search,DC=example,DC=com was not found.",
                }
            ],
            Output.SUCCESSFUL_DISABLEMENTS: ["CN=Users,DC=example,DC=com"],
            Output.SUCCESS: True,
        }
        self.assertEqual(expected, actual)

    @default_connector(action=DisableUsers())
    def test_empty_input(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAMES: []})
        self.assertEqual("Distinguished Names must contain at least one entry", context.exception.cause)
        self.assertEqual("Please enter one or more Distinguished Names", context.exception.assistance)
