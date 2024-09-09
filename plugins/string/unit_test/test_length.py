import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from jsonschema import validate
from komand_string.actions.length import Length
from komand_string.actions.length.schema import Input, Output
from parameterized import parameterized


class TestLength(TestCase):
    def setUp(self) -> None:
        self.action = Length()

    @parameterized.expand([({Input.STRING: ""}, {Output.LENGTH: 0}), ({Input.STRING: "MyTest"}, {Output.LENGTH: 6})])
    def test_length(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.STRING: 2},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_length_error(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
