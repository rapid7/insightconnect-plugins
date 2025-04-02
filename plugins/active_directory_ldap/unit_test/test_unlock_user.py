import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.enable_user.schema import Input, Output
from komand_active_directory_ldap.actions.unlock_user import UnlockUser
from komand_active_directory_ldap.connection import Connection

from common import MockConnection, MockServer, default_connector


class TestActionUnlockUser(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=UnlockUser())
    def test_unlock_user(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=UnlockUser())
    def test_unlock_user_empty_search(self, action):
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
    @default_connector(action=UnlockUser())
    def test_unlock_user_raise(self, action):
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
    @default_connector(action=UnlockUser())
    def test_unlock_user_wrong_result(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAME: "CN=wrong_result,DC=example,DC=com"})

        self.assertEqual(
            "The DN CN=wrong_result,DC=example,DC=com was not found.",
            context.exception.cause,
        )
        self.assertEqual(
            "Please provide a valid DN and try again.", context.exception.assistance
        )

    def test_unlock_user_integration(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = UnlockUser()

        test_conn.logger = log
        test_action.logger = log
        # Uncomment when you have a valid JSON file. Allows for debugging of the plugin and won't fail tests otherwise
        """
        try:
            with open("../tests/unlock_user.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = "Could not find or read sample tests from /tests directory"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        
        # self.assertEquals(True, results.get("success"))
        """
