import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_string.actions.split_to_list import SplitToList
from komand_string.actions.split_to_list.schema import Input, Output
from parameterized import parameterized


class TestSplitToList(TestCase):
    def setUp(self) -> None:
        self.action = SplitToList()

    @parameterized.expand(
        [
            (
                {Input.STRING: "MyTest Example", Input.DELIMITER: " "},
                {Output.LIST: ["MyTest", "Example"]},
            )
        ]
    )
    def test_split_to_list(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.STRING: 2},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
            (
                {Input.STRING: ["test"]},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
            (
                {Input.STRING: "", Input.DELIMITER: ""},
                "Action failed! Missing required user input.",
                "Please provide the input string.",
            ),
        ]
    )
    def test_split_to_list_error(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
