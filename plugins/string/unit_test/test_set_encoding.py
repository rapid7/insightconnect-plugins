import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_string.actions.set_encoding import SetEncoding
from komand_string.actions.set_encoding.schema import Input, Output
from parameterized import parameterized


class TestSetEncoding(TestCase):
    def setUp(self) -> None:
        self.action = SetEncoding()

    @parameterized.expand(
        [
            (
                {Input.STRING: "MyTest", Input.ENCODING: "UTF-8", Input.ERROR_HANDLING: "ignore"},
                {Output.ENCODED: "MyTest"},
            )
        ]
    )
    def test_set_encoding(self, input_data: Dict[str, Any], expected: Dict[str, Any]) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                {Input.STRING: 2, Input.ENCODING: "UTF-8", Input.ERROR_HANDLING: "ignore"},
                "Encoding failed.",
                "Could not encode given string.",
            ),
            (
                {Input.STRING: ["test"], Input.ENCODING: "UTF-8", Input.ERROR_HANDLING: "ignore"},
                "Encoding failed.",
                "Could not encode given string.",
            ),
        ]
    )
    def test_set_encoding_error(self, input_data: Dict[str, Any], cause: str, assistance: str) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run(input_data)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
