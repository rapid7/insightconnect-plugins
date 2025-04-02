from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.actions.query_group_membership import (
    QueryGroupMembership,
)
from komand_active_directory_ldap.actions.query_group_membership.schema import (
    Input,
    Output,
)

from common import MockConnection, MockServer, default_connector


class TestActionQueryGroupMembership(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group(self, action):
        actual = action.run(
            {Input.SEARCH_BASE: "CN=Users,DC=example,DC=com", Input.GROUP_NAME: "Users"}
        )
        expected = {Output.COUNT: 1, Output.RESULTS: [{"dn": "DN=user"}]}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group_false(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.SEARCH_BASE: "CN=empty_search,DC=example,DC=com",
                    Input.GROUP_NAME: "Users",
                }
            )

        self.assertEqual("The specified group was not found.", context.exception.cause)
        self.assertEqual(
            "Please check that the provided group name and search base are correct and try again.",
            context.exception.assistance,
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group_bad_response(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.SEARCH_BASE: "CN=bad_response,DC=example,DC=com",
                    Input.GROUP_NAME: "Users",
                }
            )

        self.assertEqual("The specified group was not found.", context.exception.cause)
        self.assertEqual(
            "Please check that the provided group name and search base are correct and try again.",
            context.exception.assistance,
        )

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group_no_response(self, action):
        with self.assertRaises(PluginException) as context:
            action.run(
                {
                    Input.SEARCH_BASE: "CN=no_response,DC=example,DC=com",
                    Input.GROUP_NAME: "Users",
                }
            )

        self.assertEqual("The specified group was not found.", context.exception.cause)
        self.assertEqual(
            "Please check that the provided group name and search base are correct and try again.",
            context.exception.assistance,
        )
