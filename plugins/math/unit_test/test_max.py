import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_math.actions.max import Max
from komand_math.actions.max.schema import Input, Output
from parameterized import parameterized


class TestMax(TestCase):
    def setUp(self) -> None:
        self.action = Max()

    @parameterized.expand(
        [
            ({Input.NUMBERS: [1, 2, 3, 4]}, {Output.MAX: 4}),
            ({Input.NUMBERS: [-2, 10.5, 100.5, 20, 2012]}, {Output.MAX: 2012}),
            ({Input.NUMBERS: [0, 0]}, {Output.MAX: 0}),
        ]
    )
    def test_max(self, input_parameters: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.NUMBERS: 0},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_max_error(self, input_parameters: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
