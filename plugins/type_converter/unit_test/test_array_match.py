import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.array_match import ArrayMatch
from icon_type_converter.actions.array_match.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestArrayMatch(TestCase):
    def setUp(self) -> None:
        self.action = ArrayMatch()

    @parameterized.expand(
        [
            (
                {Input.ARRAY1: ["test1", "test2"], Input.ARRAY2: ["test2", "test3"], Input.DEDUPLICATES: True},
                {Output.MATCHES_ARRAY: ["test2"], Output.COUNT: 1},
            )
        ]
    )
    def test_array_match(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
