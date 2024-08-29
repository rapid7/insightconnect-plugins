import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.array_diff import ArrayDiff
from icon_type_converter.actions.array_diff.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestArrayDiff(TestCase):
    def setUp(self) -> None:
        self.action = ArrayDiff()

    @parameterized.expand(
        [
            (
                {Input.ARRAY1: ["test1", "test2"], Input.ARRAY2: ["test2"]},
                {Output.DIFFERENCE_ARRAY: ["test1"]},
            )
        ]
    )
    def test_array_diff(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
