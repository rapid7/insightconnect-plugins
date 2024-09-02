import os
import sys

sys.path.append(os.path.abspath("../"))


from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.to_utc import ToUtc
from komand_datetime.actions.to_utc.schema import Input, Output
from parameterized import parameterized


class TestToUtc(TestCase):
    def setUp(self) -> None:
        self.action = ToUtc()

    @parameterized.expand(
        [
            (
                {Input.BASE_TIME: "22 Jul 2020 21:20:33", Input.TIMEZONE: "US/Eastern"},
                {Output.CONVERTED_DATE: "2020-07-23T01:20:33.0Z"},
            )
        ]
    )
    def test_to_utc(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
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
    def test_to_utc_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
