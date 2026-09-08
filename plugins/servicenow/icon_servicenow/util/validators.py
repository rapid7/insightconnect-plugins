import re

from insightconnect_plugin_runtime.exceptions import PluginException

# A record is addressed by its sys_id, by an identifier ServiceNow shows in its place such as the
# incident number INC0010001, or by a reference value the instance carries in place of a generated
# sys_id - the location 'US-East' this plugin documents in the output of Get CI is one - so hyphens
# and underscores are as ordinary in an identifier as letters and digits are.
# What is excluded is everything the URL would read rather than the record lookup: a path separator
# or a dot segment aims the request at another table, since dot segments are resolved before the
# request is sent, and an ampersand, a hash or a caret adds parameters and encoded query operators of
# its own. Both patterns end in \Z rather than in $, which would let a trailing newline through.
RECORD_IDENTIFIER = re.compile(r"^[A-Za-z0-9_-]+\Z")

# Table names hold letters, digits and underscores, custom tables being prefixed with u_ or x_.
TABLE_NAME = re.compile(r"^[A-Za-z0-9_]+\Z")


def validate_record_identifier(value: str, label: str) -> str:
    """
    Checks that a value used to address a record can hold nothing but the record it names, so that it
    cannot aim the request at another table or add parameters of its own to it.

    :param value: Value to validate
    :type value: str
    :param label: Name the value is known by to the caller, used in the error message
    :type label: str
    :return: The validated value
    :rtype: str
    """
    if not RECORD_IDENTIFIER.match(value or ""):
        raise PluginException(
            cause=f"The {label} provided is not a valid ServiceNow record identifier.",
            assistance=f"A record is addressed by its system ID or number, which hold letters, digits, "
            f"hyphens and underscores only. Verify that '{value}' is the {label} of the record and try again.",
        )

    return value


def validate_table_name(value: str) -> str:
    """
    Checks that a value used as a table name can name nothing but a table, so that it cannot aim the
    request at another endpoint of the API.

    :param value: Value to validate
    :type value: str
    :return: The validated value
    :rtype: str
    """
    if not TABLE_NAME.match(value or ""):
        raise PluginException(
            cause="The table provided is not a valid ServiceNow table name.",
            assistance=f"A table name holds letters, digits and underscores only. Verify that '{value}' "
            "is the name of the table and try again.",
        )

    return value
