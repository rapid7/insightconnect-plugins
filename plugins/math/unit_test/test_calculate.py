import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from jsonschema import validate
from komand_math.actions.calculate import Calculate
from komand_math.actions.calculate.schema import Input, Output
from parameterized import parameterized


class TestCalculate(TestCase):
    def setUp(self) -> None:
        self.action = Calculate()

    @parameterized.expand(
        [
            ({Input.EQUATION: "2 + 2"}, {Output.RESULT: 4}),
            ({Input.EQUATION: "10 - 2"}, {Output.RESULT: 8}),
            ({Input.EQUATION: "2 * 2 * 3"}, {Output.RESULT: 12}),
        ]
    )
    def test_calculate(self, input_parameters: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_parameters)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.EQUATION: "Wrong"},
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_calculate_error(self, input_parameters: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
