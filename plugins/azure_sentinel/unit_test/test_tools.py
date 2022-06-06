import sys
from pathlib import Path
from unittest import TestCase
import datetime
from parameterized import parameterized
from icon_azure_sentinel.util.tools import return_non_empty, generate_query_params

sys.path.append(str(Path("../").absolute()))

STUB_DATE_TIME = datetime.datetime(2022, 5, 6, 0, 0, 0, 0)
STUB_TEST_MAIL = "user@example.com"


class TestTools(TestCase):
    def test_return_non_empty_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}})

    def test_return_non_empty_with_empty_list_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}, "7": []}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}})

    def test_return_non_empty_with_list_ok(self):
        input_dict = {"1": {"2": None, "3": {}}, "4": {"5": "6"}, "7": ["8", "9"]}
        self.assertEqual(return_non_empty(input_dict), {"4": {"5": "6"}, "7": ["8", "9"]})

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
                    "filter": f"properties/status eq 'Active' and properties/createdTimeUtc ge {STUB_DATE_TIME.isoformat()}Z and properties/lastModifiedTimeUtc ge {STUB_DATE_TIME.isoformat()}Z and properties/owner/assignedTo eq '{STUB_TEST_MAIL}'"
                },
            ),
            (
                "All",
                STUB_DATE_TIME,
                STUB_DATE_TIME,
                STUB_TEST_MAIL,
                {
                    "filter": f"properties/createdTimeUtc ge {STUB_DATE_TIME.isoformat()}Z and properties/lastModifiedTimeUtc ge {STUB_DATE_TIME.isoformat()}Z and properties/owner/assignedTo eq '{STUB_TEST_MAIL}'"
                },
            ),
            (
                "All",
                None,
                STUB_DATE_TIME,
                STUB_TEST_MAIL,
                {
                    "filter": f"properties/lastModifiedTimeUtc ge {STUB_DATE_TIME.isoformat()}Z and properties/owner/assignedTo eq '{STUB_TEST_MAIL}'"
                },
            ),
            (
                "Active",
                None,
                None,
                None,
                {"filter": f"properties/status eq 'Active'"},
            ),
            (
                "All",
                None,
                STUB_DATE_TIME,
                None,
                {"filter": f"properties/lastModifiedTimeUtc ge {STUB_DATE_TIME.isoformat()}Z"},
            ),
            (
                "All",
                None,
                None,
                STUB_TEST_MAIL,
                {"filter": f"properties/owner/assignedTo eq '{STUB_TEST_MAIL}'"},
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
