import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.boolean_to_integer import BooleanToInteger
from icon_type_converter.actions.boolean_to_integer.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestBooleanToInteger(TestCase):
    def setUp(self) -> None:
        self.action = BooleanToInteger()

    @parameterized.expand(
        [
            (
                {Input.INPUT: True},
                {Output.OUTPUT: 1},
            ),
            (
                {Input.INPUT: False},
                {Output.OUTPUT: 0},
            ),
        ]
    )
    def test_boolean_to_integer(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
