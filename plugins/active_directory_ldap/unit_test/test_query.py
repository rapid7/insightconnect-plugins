from unittest import TestCase, mock

from komand_active_directory_ldap.actions.query import Query
from komand_active_directory_ldap.actions.query.schema import Input, Output

from common import MockConnection, MockServer, default_connector


class TestActionQuery(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=Query())
    def test_query(self, action):
        actual = action.run(
            {
                Input.SEARCH_BASE: "CN=Users,DC=example,DC=com",
                Input.SEARCH_FILTER: "(objectclass=*)",
            }
        )
        expected = {Output.COUNT: 1, Output.RESULTS: [{"dn": "DN=user"}]}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=Query())
    def test_query_false(self, action):
        actual = action.run(
            {
                Input.SEARCH_BASE: "CN=empty_search,DC=example,DC=com",
                Input.SEARCH_FILTER: "(objectclass=*)",
            }
        )
        expected = {Output.RESULTS: [], Output.COUNT: 0}

        self.assertEqual(actual, expected)
