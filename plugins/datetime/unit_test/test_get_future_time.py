import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.get_future_time import GetFutureTime
from komand_datetime.actions.get_future_time.schema import Input, Output
from parameterized import parameterized


class TestGetFutureTime(TestCase):
    def setUp(self) -> None:
        self.action = GetFutureTime()

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIMESTAMP: "2020-07-02T21:20:33.0Z",
                    Input.TIME_UNIT: "Days",
                    Input.TIME_ZONE: "UTC",
                    Input.TIME_AMOUNT: 20,
                },
                {Output.TIMESTAMP: "2020-07-22T21:20:33.0Z"},
            )
        ]
    )
    def test_get_future_time(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIMESTAMP: "wrong date",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_get_future_time_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
