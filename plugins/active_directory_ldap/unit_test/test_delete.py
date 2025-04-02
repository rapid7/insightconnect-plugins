from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.delete import Delete
from komand_active_directory_ldap.actions.delete.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionDelete(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=Delete())
    def test_delete(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=Delete())
    def test_delete_raise(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAME: "with_error"})

        self.assertTrue("Something unexpected occurred." in context.exception.cause)
        self.assertTrue(
            "failed: error message test description" in context.exception.assistance
        )
