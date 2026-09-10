import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any
from unittest import TestCase

from icon_servicenow.util.validators import validate_record_identifier, validate_table_name
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


class TestValidateRecordIdentifier(TestCase):
    @parameterized.expand(
        [
            ["system_id", "9de5069c5afe602b2ea0a04b66beb2c0"],
            ["incident_number", "INC0010001"],
            ["security_incident_number", "SIR0001001"],
            # A record the instance carries under a reference value rather than a generated sys_id is
            # addressed by that value, and Get CI documents one of them - the location 'US-East'.
            ["reference_value_with_a_hyphen", "US-East"],
            ["reference_value_with_an_underscore", "us_east_1"],
        ]
    )
    def test_validate_record_identifier(self, test_name: str, value: str) -> None:
        self.assertEqual(validate_record_identifier(value, "system ID"), value)

    @parameterized.expand(
        [
            # requests resolves dot segments before the request is sent, so a value holding them aims
            # the request at a table of the caller's choosing rather than at the record.
            ["dot_segments", "../../table/sys_user"],
            ["dot_segments_after_a_system_id", "9de5069c5afe602b2ea0a04b66beb2c0/../../../table/sys_user"],
            ["path_separator", "incident/sys_user"],
            # A value holding a query separator, an ampersand or a hash adds parameters of its own to
            # the URL, and one holding a caret adds operators to the encoded query.
            ["query_separator", "j1?sysparm_query=active=true"],
            ["parameter_separator", "j1&sysparm_fields=sys_id"],
            ["fragment", "j1#truncated"],
            ["encoded_query_operator", "j1^element=comments"],
            ["encoded_query_operator_percent_encoded", "j1%5Eelement=comments"],
            ["whitespace", "9de5069c 5afe602b"],
            ["trailing_newline", "9de5069c5afe602b2ea0a04b66beb2c0\n"],
            ["empty", ""],
            ["none", None],
        ]
    )
    def test_validate_record_identifier_raise_exception(self, test_name: str, value: Any) -> None:
        with self.assertRaises(PluginException) as error:
            validate_record_identifier(value, "system ID")
        self.assertEqual(error.exception.cause, "The system ID provided is not a valid ServiceNow record identifier.")


class TestValidateTableName(TestCase):
    @parameterized.expand(
        [
            ["table", "incident"],
            ["table_with_underscores", "cmdb_ci_computer"],
            ["custom_table", "u_custom_table"],
            ["scoped_table", "x_rapid7_app_record"],
        ]
    )
    def test_validate_table_name(self, test_name: str, value: str) -> None:
        self.assertEqual(validate_table_name(value), value)

    @parameterized.expand(
        [
            ["dot_segments", "incident/../../../oauth_token.do"],
            ["path_separator", "incident/9de5069c5afe602b2ea0a04b66beb2c0"],
            ["query_separator", "incident?sysparm_query=active=true"],
            ["trailing_newline", "incident\n"],
            ["empty", ""],
            ["none", None],
        ]
    )
    def test_validate_table_name_raise_exception(self, test_name: str, value: Any) -> None:
        with self.assertRaises(PluginException) as error:
            validate_table_name(value)
        self.assertEqual(error.exception.cause, "The table provided is not a valid ServiceNow table name.")
