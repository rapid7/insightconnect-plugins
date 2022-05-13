import datetime
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from parameterized import parameterized

from icon_microsoft_defender_incidents.util.tools import generate_query_params, return_non_empty

STUB_DATE_TIME = datetime.datetime(2022, 5, 6, 0, 0, 0, 0)
STUB_TEST_MAIL = "user@example.com"


class TestTools(TestCase):
    @parameterized.expand(
        [
            ({"test": {"test2": None, "test3": "Test", "test4": "", "test5": []}}, {"test": {"test3": "Test"}}),
            ({"test": [{"test5": ""}, {"test2": [], "test3": "Test", "test4": {}}]}, {"test": [{"test3": "Test"}]}),
        ]
    )
    def test_return_non_empty(self, input_dict, output_dict):
        self.assertEqual(return_non_empty(input_dict), output_dict)

    @parameterized.expand(
        [
            (
                "Active",
                STUB_DATE_TIME,
                STUB_DATE_TIME,
                STUB_TEST_MAIL,
                {
                    "$filter": f"status eq 'Active' and createdTime ge {STUB_DATE_TIME.isoformat()}Z and lastUpdateTime ge {STUB_DATE_TIME.isoformat()}Z and assignedTo eq '{STUB_TEST_MAIL}'"
                },
            ),
            (
                "All",
                STUB_DATE_TIME,
                STUB_DATE_TIME,
                STUB_TEST_MAIL,
                {
                    "$filter": f"createdTime ge {STUB_DATE_TIME.isoformat()}Z and lastUpdateTime ge {STUB_DATE_TIME.isoformat()}Z and assignedTo eq '{STUB_TEST_MAIL}'"
                },
            ),
            (
                "All",
                None,
                STUB_DATE_TIME,
                STUB_TEST_MAIL,
                {"$filter": f"lastUpdateTime ge {STUB_DATE_TIME.isoformat()}Z and assignedTo eq '{STUB_TEST_MAIL}'"},
            ),
            (
                "Active",
                None,
                None,
                None,
                {"$filter": f"status eq 'Active'"},
            ),
            (
                "All",
                None,
                STUB_DATE_TIME,
                None,
                {"$filter": f"lastUpdateTime ge {STUB_DATE_TIME.isoformat()}Z"},
            ),
            (
                "All",
                None,
                None,
                STUB_TEST_MAIL,
                {"$filter": f"assignedTo eq '{STUB_TEST_MAIL}'"},
            ),
            (
                "All",
                None,
                None,
                None,
                None,
            ),
        ]
    )
    def test_generate_query_params(self, status, created_time, last_updated_time, assigned_to, output):
        self.assertEqual(generate_query_params(status, created_time, last_updated_time, assigned_to), output)
