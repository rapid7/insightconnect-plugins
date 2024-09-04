import os
import sys

sys.path.append(os.path.abspath("../"))


from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_datetime.actions.epoch_from_date import EpochFromDate
from komand_datetime.actions.epoch_from_date.schema import Input, Output
from parameterized import parameterized


class TestEpochFromDate(TestCase):
    def setUp(self) -> None:
        self.action = EpochFromDate()

    @parameterized.expand(
        [
            (
                {Input.DATETIME: "2021-07-22T21:20:33.0Z"},
                {Output.EPOCH: 1626988833},
            )
        ]
    )
    def test_epoch_from_date(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)

    @parameterized.expand(
        [
            (
                {
                    Input.DATETIME: "asd",
                },
                PluginException.causes[PluginException.Preset.UNKNOWN],
                PluginException.assistances[PluginException.Preset.UNKNOWN],
            )
        ]
    )
    def test_epoch_from_date_exception(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
