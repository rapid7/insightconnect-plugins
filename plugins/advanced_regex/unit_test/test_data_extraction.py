import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_advanced_regex.actions.data_extraction import DataExtraction
from icon_advanced_regex.actions.data_extraction.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestDataExtraction(TestCase):
    def setUp(self) -> None:
        self.action = DataExtraction()

    @parameterized.expand(
        [
            # Test 1: Basic match
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "lorem",
                    Input.IN_STRING: "Lorem ipsum dolor sit amet, consectetur \nadipiscing elit. Aliquam sapien ex, lorems odales",
                    Input.MULTILINE: False,
                },
                {Output.MATCHES: [{"value": ["lorem"]}]},
            ),
            # Test 2: Case-insensitive match
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: True,
                    Input.IN_REGEX: "LOREM",
                    Input.IN_STRING: "Lorem ipsum dolor sit amet, lorem LOREM",
                    Input.MULTILINE: False,
                },
                {
                    Output.MATCHES: [
                        {"value": ["Lorem"]},
                        {"value": ["lorem"]},
                        {"value": ["LOREM"]},
                    ]
                },
            ),
            # Test 3: Multiline match
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "^dolor",
                    Input.IN_STRING: "Lorem ipsum\ndolor sit amet",
                    Input.MULTILINE: True,
                },
                {Output.MATCHES: [{"value": ["dolor"]}]},
            ),
            # Test 4: Dotall match
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: True,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: "ipsum.*elit",
                    Input.IN_STRING: "ipsum dolor\nsit amet, elit",
                    Input.MULTILINE: False,
                },
                {Output.MATCHES: [{"value": ["ipsum dolor\nsit amet, elit"]}]},
            ),
            # Test 5: ASCII flag match
            (
                {
                    Input.ASCII: True,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: r"\w+",
                    Input.IN_STRING: "test me",
                    Input.MULTILINE: False,
                },
                {
                    Output.MATCHES: [
                        {"value": ["test"]},
                        {"value": ["me"]},
                    ]
                },
            ),
            # Test 6: Extract digits
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: r"\d+",
                    Input.IN_STRING: "Example 1234 EXAMPLE TEST 2023-06-01",
                    Input.MULTILINE: False,
                },
                {
                    Output.MATCHES: [
                        {"value": ["1234"]},
                        {"value": ["2023"]},
                        {"value": ["06"]},
                        {"value": ["01"]},
                    ]
                },
            ),
            # Test 7: Multiple matches in same group
            (
                {
                    Input.ASCII: False,
                    Input.DOTALL: False,
                    Input.IGNORECASE: False,
                    Input.IN_REGEX: r"(\d+)-(\w+)",
                    Input.IN_STRING: "123-abc 456-def",
                    Input.MULTILINE: False,
                },
                {
                    Output.MATCHES: [
                        {"value": ["123-abc", "123", "abc"]},
                        {"value": ["456-def", "456", "def"]},
                    ]
                },
            ),
        ]
    )
    def test_data_extraction(self, parameters: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
