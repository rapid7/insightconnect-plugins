import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.integer_to_number import IntegerToNumber
from icon_type_converter.actions.integer_to_number.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestIntegerToNumber(TestCase):
    def setUp(self) -> None:
        self.action = IntegerToNumber()

    @parameterized.expand([({Input.INPUT: 1}, {Output.OUTPUT: 1})])
    def test_integer_to_number(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
