import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.integer_to_boolean import IntegerToBoolean
from icon_type_converter.actions.integer_to_boolean.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestIntegerToBoolean(TestCase):
    def setUp(self) -> None:
        self.action = IntegerToBoolean()

    @parameterized.expand(
        [
            (
                {Input.INPUT: 1},
                {Output.OUTPUT: True},
            ),
            (
                {Input.INPUT: 0},
                {Output.OUTPUT: False},
            ),
        ]
    )
    def test_integer_to_boolean(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
