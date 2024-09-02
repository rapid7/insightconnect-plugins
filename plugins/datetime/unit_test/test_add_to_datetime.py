import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from jsonschema import validate
from komand_datetime.actions.add_to_datetime import AddToDatetime
from komand_datetime.actions.add_to_datetime.schema import Input, Output
from parameterized import parameterized


class TestAddToDatetime(TestCase):
    def setUp(self) -> None:
        self.action = AddToDatetime()

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIME: "22 Jul 2020 21:20:33",
                    Input.YEARS: 1,
                    Input.MONTHS: 0,
                    Input.DAYS: 0,
                    Input.HOURS: 0,
                    Input.MINUTES: 0,
                    Input.SECONDS: 0,
                },
                {Output.DATE: "2021-07-22T21:20:33.0Z"},
            )
        ]
    )
    def test_add_to_datetime(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.BASE_TIME: "",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_add_to_datetime_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
