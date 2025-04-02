from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.disable_users import DisableUsers
from komand_active_directory_ldap.actions.disable_users.schema import Input, Output
from parameterized import parameterized

from common import MockConnection, MockServer, default_connector


class TestActionDisableUsers(TestCase):
    @parameterized.expand(
        [
            (
                {Input.DISTINGUISHED_NAMES: ["CN=empty_search,DC=example,DC=com"]},
                {
                    Output.FAILED: [
                        {
                            "dn": "CN=empty_search,DC=example,DC=com",
                            "error": "An error occurred during plugin "
                            "execution!\n"
                            "\n"
                            "The DN "
                            "CN=empty_search,DC=example,DC=com was "
                            "not found. Please provide a valid DN "
                            "and try again.",
                        }
                    ],
                    Output.COMPLETED: [],
                },
            ),
            (
                {
                    Input.DISTINGUISHED_NAMES: [
                        "CN=empty_search,DC=example,DC=com",
                        "CN=Users,DC=example," "DC=com",
                    ]
                },
                {
                    Output.FAILED: [
                        {
                            "dn": "CN=empty_search,DC=example,DC=com",
                            "error": "An error occurred during plugin "
                            "execution!\n"
                            "\n"
                            "The DN "
                            "CN=empty_search,DC=example,DC=com was "
                            "not found. Please provide a valid DN "
                            "and try again.",
                        }
                    ],
                    Output.COMPLETED: ["CN=Users,DC=example,DC=com"],
                },
            ),
            (
                {Input.DISTINGUISHED_NAMES: ["CN=Users,DC=example,DC=com"]},
                {
                    Output.FAILED: [],
                    Output.COMPLETED: ["CN=Users,DC=example,DC=com"],
                },
            ),
        ]
    )
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=DisableUsers())
    def test_disable_users(self, _input, expected, action):
        actual = action.run(_input)
        self.assertEqual(expected, actual)

    @default_connector(action=DisableUsers())
    def test_empty_input(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAMES: []})
        self.assertEqual(
            "Distinguished Names must contain at least one entry",
            context.exception.cause,
        )
        self.assertEqual(
            "Please enter one or more Distinguished Names", context.exception.assistance
        )
