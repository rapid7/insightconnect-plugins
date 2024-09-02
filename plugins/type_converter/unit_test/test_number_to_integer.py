import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.number_to_integer import NumberToInteger
from icon_type_converter.actions.number_to_integer.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestNumberToInteger(TestCase):
    def setUp(self) -> None:
        self.action = NumberToInteger()

    @parameterized.expand([({Input.INPUT: 1}, {Output.OUTPUT: 1})])
    def test_number_to_integer(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
