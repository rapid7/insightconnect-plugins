import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.time_elapsed import TimeElapsed
from komand_datetime.actions.time_elapsed.schema import Input, Output
from parameterized import parameterized


class TestTimeElapsed(TestCase):
    def setUp(self) -> None:
        self.action = TimeElapsed()

    @parameterized.expand(
        [
            (
                {
                    Input.FIRST_TIME: "2020-07-22T21:20:33.0Z",
                    Input.SECOND_TIME: "2022-07-22T21:20:33.0Z",
                    Input.RESULT_UNIT: "Years",
                },
                {Output.DIFFERENCE: 2, Output.TIME_UNIT: "Years"},
            )
        ]
    )
    def test_time_elapsed(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.FIRST_TIME: "wrong date",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_time_elapsed_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
