import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.subtract_from_datetime import SubtractFromDatetime
from komand_datetime.actions.subtract_from_datetime.schema import Input, Output
from parameterized import parameterized


class TestSubtractFromDatetime(TestCase):
    def setUp(self) -> None:
        self.action = SubtractFromDatetime()

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIME: "2020-07-02T21:20:33.0Z",
                    Input.HOURS: 1,
                    Input.YEARS: 0,
                    Input.MONTHS: 0,
                    Input.DAYS: 0,
                    Input.MINUTES: 0,
                    Input.SECONDS: 0,
                },
                {Output.DATE: "2020-07-02T20:20:33.0Z"},
            )
        ]
    )
    def test_subtract_from_datetime(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIME: "wrong date",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_subtract_from_datetime_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)