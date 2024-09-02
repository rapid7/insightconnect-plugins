import os
import sys

sys.path.append(os.path.abspath("../"))


from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.boolean_to_string import BooleanToString
from icon_type_converter.actions.boolean_to_string.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestBooleanToString(TestCase):
    def setUp(self) -> None:
        self.action = BooleanToString()

    @parameterized.expand(
        [
            (
                {Input.INPUT: True},
                {Output.OUTPUT: "true"},
            ),
            (
                {Input.INPUT: False},
                {Output.OUTPUT: "false"},
            ),
        ]
    )
    def test_boolean_to_string(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
