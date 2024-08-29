import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.string_to_boolean import StringToBoolean
from icon_type_converter.actions.string_to_boolean.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestStringToBoolean(TestCase):
    def setUp(self) -> None:
        self.action = StringToBoolean()

    @parameterized.expand(
        [
            (
                {Input.INPUT: "true"},
                {Output.OUTPUT: True},
            ),
            (
                {Input.INPUT: "false"},
                {Output.OUTPUT: False},
            ),
        ]
    )
    def test_string_to_boolean(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
