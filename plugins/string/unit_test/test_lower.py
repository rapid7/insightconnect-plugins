import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_string.actions.lower import Lower
from komand_string.actions.lower.schema import Input, Output
from parameterized import parameterized


class TestLower(TestCase):
    def setUp(self) -> None:
        self.action = Lower()

    @parameterized.expand(
        [({Input.STRING: "MyTest"}, {Output.LOWER: "mytest"}), ({Input.STRING: "test"}, {Output.LOWER: "test"})]
    )
    def test_lower(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
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
            ({Input.STRING: ""}, "Action failed! Missing required user input.", "Please provide the input string."),
        ]
    )
    def test_lower_error(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
