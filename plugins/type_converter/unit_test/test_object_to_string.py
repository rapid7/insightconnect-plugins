import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.object_to_string import ObjectToString
from icon_type_converter.actions.object_to_string.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestObjectToString(TestCase):
    def setUp(self) -> None:
        self.action = ObjectToString()

    @parameterized.expand([({Input.INPUT: {"test": 1}}, {Output.OUTPUT: '{"test": 1}'})])
    def test_object_to_string(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
