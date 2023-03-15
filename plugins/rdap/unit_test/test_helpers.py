import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List, Union
from unittest import TestCase

from icon_rdap.util.helpers import (
    convert_keys_to_camel,
    extract_asn_result,
    extract_keys_from_dict,
    extract_nameservers,
    parse_address_information,
    parse_entities,
    parse_vcards,
    to_camel_case,
)
from parameterized import parameterized

from unit_test.util import Util


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

    @parameterized.expand(
        [
            (
                Util.read_file_to_dict("responses/helpers_vcards.json.resp").get("vcardArray")[1],
                {
                    "kind": "individual",
                    "language": "en",
                    "organization": "Example",
                    "title": "Research Scientist",
                    "role": "Project Lead",
                    "email": "joe.user@example.com",
                    "key": "https://www.example.com/joe.user/joe.asc",
                    "url": "https://example.org",
                    "fullname": "Joe User",
                    "phone": "+1-555-555-1234",
                    "geolocation": "46.772673,-71.282945",
                    "timezone": "-05:00",
                },
            )
        ]
    )
    def test_parse_vcards(self, vcards_list: List[List[Union[str, Dict[str, Any]]]], expected: Dict[str, Any]) -> None:
        result = parse_vcards(vcards_list)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (
                ["Example Office Box", "Test 1234", "Some street", "MyCity", "REGION", "123-123", "MyCountry"],
                {
                    "postOfficeBox": "Example Office Box",
                    "extendedAddress": "Test 1234",
                    "streetAddress": "Some street",
                    "locality": "MyCity",
                    "region": "REGION",
                    "postalCode": "123-123",
                    "countryName": "MyCountry",
                },
            ),
            (["", "", "", "", "", "", "MyCountry"], {"countryName": "MyCountry"}),
        ]
    )
    def test_parse_address_information(self, address_rdap_list: List[str], expected: Dict[str, Any]) -> None:
        result = parse_address_information(address_rdap_list)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (
                Util.read_file_to_dict("responses/helpers_entities.json.resp").get("entities"),
                [
                    {
                        "roles": ["registrar"],
                        "kind": "individual",
                        "title": "Research Scientist",
                        "role": "Project Lead",
                        "email": "user@example.com",
                        "fullname": "Joe User",
                        "handle": "XXXX",
                        "address": {
                            "extendedAddress": "Suite 1234",
                            "streetAddress": "Somewhere",
                            "locality": "Sample",
                            "region": "Other 1",
                            "postalCode": "Test 1",
                            "countryName": "Example Country Name 1",
                        },
                        "phone": "+1-555-555-1234",
                        "organization": "Example",
                        "language": "en",
                    },
                    {
                        "roles": ["abuse"],
                        "kind": "individual",
                        "title": "Research Scientist",
                        "role": "Project Lead",
                        "email": "user2@example.com",
                        "fullname": "User 2 ",
                        "address": {
                            "extendedAddress": "Suite 1234",
                            "streetAddress": "Somewhere",
                            "locality": "Sample",
                            "region": "Other",
                            "postalCode": "Test",
                            "countryName": "Example Country Name 2",
                        },
                        "phone": "+1-555-555-1234",
                        "organization": "Example",
                        "language": "en",
                    },
                ],
            )
        ]
    )
    def test_parse_entities(self, entity: List[Dict[str, Any]], expected: List[Dict[str, Any]]) -> None:
        result = parse_entities(entity)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (
                Util.read_file_to_dict("responses/domain_lookup_found_domain.json.resp").get("nameservers", []),
                ["A.IANA-SERVERS.NET", "B.IANA-SERVERS.NET"],
            )
        ]
    )
    def test_extract_nameservers(self, nameserver: List[Dict[str, Any]], expected: List[str]) -> None:
        results = extract_nameservers(nameserver)
        self.assertEqual(results, expected)
