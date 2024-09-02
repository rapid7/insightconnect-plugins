import os
import sys

sys.path.append(os.path.abspath("../"))


from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.date_from_epoch import DateFromEpoch
from komand_datetime.actions.date_from_epoch.schema import Input, Output
from parameterized import parameterized


class TestDateFromEpoch(TestCase):
    def setUp(self) -> None:
        self.action = DateFromEpoch()

    @parameterized.expand(
        [
            (
                {
                    Input.EPOCH: "1595452833",
                },
                {Output.DATE: "2020-07-22T21:20:33.0Z"},
            )
        ]
    )
    def test_date_from_epoch(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.EPOCH: "123456789101283719273891273981273",
                },
                "The given epoch is out of range.",
                "This action supports seconds, milliseconds, microseconds, and nanoseconds. Please check that the given epoch is correct.",
            ),
            (
                {
                    Input.EPOCH: "abcdef",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            ),
        ]
    )
    def test_date_from_epoch_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
