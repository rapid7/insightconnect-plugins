import os
import sys
from unittest import TestCase
from parameterized import parameterized
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))

from icon_rdap.util.helpers import to_camel_case, convert_keys_to_camel, extract_keys_from_dict, extract_asn_result


class TestHelpers(TestCase):
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
    def test_to_camel_case(self, test_name, string_to_modify, expected):
        actual = to_camel_case(string_to_modify)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["dict_to_camel1", {"snake_key": 4}, {"snakeKey": 4}],
            ["dict_to_camel2", {"camelCase": 4}, {"camelCase": 4}],
            ["dict_to_camel3", {"PascalCase": 4}, {"pascalCase": 4}],
            ["list_to_camel1", [{"snake_key": 4}], [{"snakeKey": 4}]],
            ["list_to_camel2", [{"camelCase": 4}], [{"camelCase": 4}]],
            ["list_to_camel3", [{"PascalCase": 4}], [{"pascalCase": 4}]],
        ]
    )
    def test_convert_keys_to_camel(self, test_name, to_modify, expected):
        actual = convert_keys_to_camel(to_modify)
        self.assertEqual(actual, expected)

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
    def test_extract_keys_from_dict(self, test_name, input_dict, keys_list, expected):
        actual = extract_keys_from_dict(input_dict, keys_list)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "asn_example",
                Util.read_file_to_dict("responses/helpers_ipwhois_lookup_rdap.json.resp"),
                Util.read_file_to_dict("expected/helpers_ipwhois_lookup_rdap.json.exp"),
            ],
            ["asn_empty", {}, {}],
        ]
    )
    def test_prepare_asn_result(self, test_name, asn_result, expected):
        actual = extract_asn_result(asn_result)
        self.assertDictEqual(actual, expected)
