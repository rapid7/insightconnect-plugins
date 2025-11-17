import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from icon_zscaler.util.constants import Assistance, Cause
from icon_zscaler.util.helpers import (
    clean_dict,
    remove_password_from_result,
    prepare_groups,
    prepare_department,
    to_camel_case,
    convert_dict_keys_to_camel_case,
    filter_dict_keys,
    find_custom_url_category_by_name,
    find_url_category_by_id,
)

class TestHelpers(TestCase):
    @parameterized.expand(
        [
            ["empty_dict", {}, {}],
            [
                "clean_dict",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
            ],
            [
                "to_be_cleaned",
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    "team": {"id": 1234, "name": "John"},
                    "empty_string": "",
                },
                {"key": "value", "next": {"request_i": "123"}, "team": {"id": 1234, "name": "John"}},
            ],
        ]
    )
    def test_clean_dict(self, test_name, input_params, expected):
        actual = clean_dict(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["contains_password", {"id": 123, "password": "password123"}, {"id": 123}],
            ["no_password", {"id": 123}, {"id": 123}],
        ]
    )
    def test_remove_password(self, test_name, input_params, expected):
        actual = remove_password_from_result(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["one_department_found", [{"name": "Department Name"}], "Department Name", {"name": "Department Name"}],
        ]
    )
    def test_prepare_department(self, test_name, found_results, search_name, expected):
        actual = prepare_department(found_results, search_name)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found_department",
                [],
                "Not exist",
                Cause.DEPARTMENT_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "search_name_in_comments",
                [{"comments": "Department Name"}],
                "Department Name",
                Cause.DEPARTMENT_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "two_departments_found",
                [{"name": "Department 1"}, {"name": "Department 2"}],
                "Department",
                Cause.DEPARTMENT_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_prepare_department_raise_exception(self, test_name, found_results, search_name, cause, assistance):
        with self.assertRaises(PluginException) as error:
            prepare_department(found_results, search_name)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            ["one_group_found", [{"name": "Group Name"}], ["Group Name"], [{"name": "Group Name"}]],
            [
                "all_groups_found",
                [{"name": "Group Name 1"}, {"name": "Group Name 2"}],
                ["Group Name 1", "Group Name 2"],
                [{"name": "Group Name 1"}, {"name": "Group Name 2"}],
            ],
        ]
    )
    def test_prepare_groups(self, test_name, found_results, search_names, expected):
        actual = prepare_groups(found_results, search_names)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found_group",
                [],
                ["Group Name 1", "Group Name 2"],
                Cause.GROUP_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "one_valid_group",
                [{"name": "Group Name 1"}],
                ["Group Name 1", "Group Name 2"],
                Cause.GROUP_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "two_groups_found",
                [{"name": "Group Name 1"}, {"name": "Group Name 2"}],
                ["Group Name"],
                Cause.GROUP_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "search_name_in_comments",
                [{"name": "Group Name", "comments": "Search comment"}],
                ["Search comment"],
                Cause.GROUP_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_prepare_groups_raise_exception(self, test_name, found_results, search_names, cause, assistance):
        with self.assertRaises(PluginException) as error:
            prepare_groups(found_results, search_names)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            ["snake1", "camel_case_string", "camelCaseString"],
            ["snake2", "my_new_camel", "myNewCamel"],
            ["snake3", "my0_snake", "my0Snake"],
            ["single_word", "word", "word"],
            ["word_with_digit1", "word1", "word1"],
            ["word_with_digit1", "word1", "word1"],
            ["word_capitalized1", "wordABC", "wordAbc"],
            ["word_capitalized2", "word9ABC9", "word9Abc9"],
            ["camel_case", "myCamelCase", "myCamelCase"],
            ["pascal_case", "PascalCase", "pascalCase"],
            ["empty", "", ""],
        ]
    )
    def test_to_camel_case(self, test_name, string_to_convert, expected):
        actual = to_camel_case(string_to_convert)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["dict_to_camel1", {"snake_key": 4}, {"snakeKey": 4}],
            ["dict_to_camel2", {"camelCase": 4}, {"camelCase": 4}],
            ["dict_to_camel3", {"PascalCase": 4}, {"pascalCase": 4}],
        ]
    )
    def test_convert_dict_keys_to_camel_case(self, test_name, dict_to_convert, expected):
        actual = convert_dict_keys_to_camel_case(dict_to_convert)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "keys_from_dict",
                {"key1": 4, "key2": 9, "key3": "example"},
                ["key1", "key3"],
                {"key1": 4, "key3": "example"},
            ],
            ["empty_keys_from_dict", {"key1": 4, "key2": 9, "key3": "example"}, [], {}],
            ["keys_from_empty_dict", {}, ["key1", "key3"], {}],
        ]
    )
    def test_filter_dict_keys(self, test_name, dict_to_modify, keys_list, expected):
        actual = filter_dict_keys(dict_to_modify, keys_list)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "existing_url_category_name",
                "Test Category",
                Util.read_file_to_dict("responses/list_url_categories_only_custom.json.resp"),
                Util.read_file_to_dict("responses/get_url_category_by_name_custom.json.resp"),
            ]
        ]
    )
    def test_find_custom_url_category_by_name(self, test_name, url_category_name, url_categories_list, expected):
        actual = find_custom_url_category_by_name(url_category_name, url_categories_list)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "non_existing_url_category_name",
                "Non existing name",
                Util.read_file_to_dict("responses/list_url_categories_only_custom.json.resp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "empty_url_category_name",
                "",
                Util.read_file_to_dict("responses/list_url_categories_only_custom.json.resp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            ["empty_url_categories_list", "Test Category", [], Cause.CATEGORY_NOT_FOUND, Assistance.VERIFY_INPUT],
        ]
    )
    def test_find_custom_url_category_by_name_raise_exception(
        self, test_name, category_name, categories_list, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            find_custom_url_category_by_name(category_name, categories_list)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "existing_url_category_id",
                "RADIO_STATIONS",
                Util.read_file_to_dict("responses/list_url_categories_all.json.resp"),
                Util.read_file_to_dict("responses/get_url_category_by_name_predefined.json.resp"),
            ]
        ]
    )
    def test_find_url_category_by_id(self, test_name, url_category_id, url_categories_list, expected):
        actual = find_url_category_by_id(url_category_id, url_categories_list)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "non_existing_url_category_id",
                "NON_EXISTING_ID",
                Util.read_file_to_dict("responses/list_url_categories_all.json.resp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            [
                "empty_url_category_id",
                "",
                Util.read_file_to_dict("responses/list_url_categories_all.json.resp"),
                Cause.CATEGORY_NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
            ["empty_url_categories_list", "RADIO_STATIONS", [], Cause.CATEGORY_NOT_FOUND, Assistance.VERIFY_INPUT],
        ]
    )
    def test_find_url_category_by_id_raise_exception(
        self, test_name, category_name, categories_list, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            find_url_category_by_id(category_name, categories_list)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
