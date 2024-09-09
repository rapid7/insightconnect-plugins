import os
import sys

sys.path.append(os.path.abspath("../"))


from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_string.actions.split_to_object import SplitToObject
from komand_string.actions.split_to_object.schema import Input, Output
from parameterized import parameterized


class TestSplitToObject(TestCase):
    def setUp(self) -> None:
        self.action = SplitToObject()

    @parameterized.expand(
        [
            (
                {Input.STRING: "MyTest Example", Input.STRING_DELIMITER: " ", Input.BLOCK_DELIMITER: ""},
                {Output.OBJECT: {"MyTest": "Example"}},
            )
        ]
    )
    def test_split_to_object(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.STRING: 2},
                "Action failed! Unable to split string cleanly.",
                "Please try specifying the block delimiter for more multi-key:value input.",
            ),
            (
                {Input.STRING: ["test"], Input.STRING_DELIMITER: ""},
                "Action failed! Unable to split string cleanly.",
                "Please try specifying the block delimiter for more multi-key:value input.",
            ),
            (
                {Input.STRING: ["test"], Input.STRING_DELIMITER: "", Input.BLOCK_DELIMITER: "["},
                "Action failed! Unable to split string cleanly.",
                "Please try specifying the block delimiter for more multi-key:value input.",
            ),
            (
                {Input.STRING: "", Input.STRING_DELIMITER: ""},
                "Action failed! Missing required user input.",
                "Please provide the input string.",
            ),
        ]
    )
    def test_split_to_object_error(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
