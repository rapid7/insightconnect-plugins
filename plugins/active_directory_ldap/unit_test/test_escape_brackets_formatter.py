from unittest import TestCase

from komand_active_directory_ldap.util.utils import ADUtils
from parameterized import parameterized


class TestHostFormatter(TestCase):
    @parameterized.expand(
        [
            (
                "(objectCategory=This is a (Test) here)",
                "(objectCategory=This is a \\28Test\\29 here)",
            ),
            (
                "(&(objectCategory=This is a (Test) here)(TestField=*))",
                "(&(objectCategory=This is a \\28Test\\29 here)(TestField=*))",
            ),
            (
                "(objectTest=NUL)(!(TestField=test\\))",
                "(objectTest=NUL)(!(TestField=test\\))",
            ),
            (
                "(objectCategory=My Testing ( Category ))",
                "(objectCategory=My Testing \\28 Category \\29)",
            ),
        ]
    )
    def test_host_formatter(self, query: str, expected_result: str):
        result = ADUtils.escape_brackets_for_query(query)
        self.assertEqual(expected_result, result)
