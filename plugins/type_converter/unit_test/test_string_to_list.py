import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from icon_type_converter.actions.string_to_list import StringToList
from icon_type_converter.actions.string_to_list.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized


class TestStringToList(TestCase):
    def setUp(self) -> None:
        self.action = StringToList()

    @parameterized.expand(
        [
            (
                {Input.INPUT: "My Example String", Input.DELIMITER: " "},
                {Output.OUTPUT: ["My", "Example", "String"]},
            )
        ]
    )
    def test_string_to_list(self, input_: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_)
        self.assertEqual(expected, response)
        validate(response, self.action.output.schema)
