from unittest import TestCase, mock
from komand.exceptions import PluginException
from komand_active_directory_ldap.actions.query_group_membership import QueryGroupMembership
from komand_active_directory_ldap.actions.query_group_membership.schema import Input, Output
from unit_test.common import MockServer
from unit_test.common import MockConnection
from unit_test.common import default_connector


class TestActionQueryGroupMembership(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group(self, action):
        actual = action.run({Input.SEARCH_BASE: "CN=Users,DC=example,DC=com", Input.GROUP_NAME: "Users"})
        expected = {Output.COUNT: 1, Output.RESULTS: [{"dn": "DN=user"}]}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=QueryGroupMembership())
    def test_query_group_false(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.SEARCH_BASE: "CN=empty_search,DC=example,DC=com", Input.GROUP_NAME: "Users"})

        self.assertEqual("LDAP returned unexpected response.", context.exception.cause)
        self.assertEqual(
            "Check that the provided inputs are correct and try again. If the issue persists please contact support.",
            context.exception.assistance,
        )
        self.assertEqual("list index out of range", str(context.exception.data))
