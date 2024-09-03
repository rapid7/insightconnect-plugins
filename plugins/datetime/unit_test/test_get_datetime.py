import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from freezegun import freeze_time
from jsonschema import validate
from komand_datetime.actions.get_datetime import GetDatetime
from komand_datetime.actions.get_datetime.schema import Input, Output
from parameterized import parameterized


class TestGetDatetime(TestCase):
    def setUp(self) -> None:
        self.action = GetDatetime()

    @parameterized.expand(
        [
            (
                {Input.FORMAT_STRING: "%d %b %Y %H:%M:%S", Input.USE_RFC3339_FORMAT: True},
                {Output.DATETIME: "2024-09-02T00:00:00.0Z", Output.EPOCH_TIMESTAMP: 1725235200},
            )
        ]
    )
    @freeze_time("2024-09-02")
    def test_get_datetime(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        self.assertEqual(response, expected)
        validate(response, self.action.output.schema)
