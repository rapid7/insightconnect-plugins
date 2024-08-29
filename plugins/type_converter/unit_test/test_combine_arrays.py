import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.combine_arrays import CombineArrays
from icon_type_converter.actions.combine_arrays.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestCombineArrays(TestCase):
    def setUp(self) -> None:
        self.action = CombineArrays()

    @parameterized.expand(
        [
            (
                {
                    Input.ARRAY1: ["test1"],
                    Input.ARRAY2: [],
                    Input.ARRAY3: [],
                    Input.ARRAY4: [],
                    Input.ARRAY5: [],
                },
                {Output.COMBINED_ARRAY: ["test1"]},
            )
        ]
    )
    def test_combine_arrays(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
