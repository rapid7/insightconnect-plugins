import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.string_to_integer import StringToInteger
from icon_type_converter.actions.string_to_integer.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestStringToInteger(TestCase):
    def setUp(self) -> None:
        self.action = StringToInteger()

    @parameterized.expand(
        [
            (
                {Input.INPUT: "-1"},
                {Output.OUTPUT: -1},
            ),
            (
                {Input.INPUT: "0"},
                {Output.OUTPUT: 0},
            ),
            (
                {Input.INPUT: "1"},
                {Output.OUTPUT: 1},
            ),
        ]
    )
    def test_string_to_integer(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
