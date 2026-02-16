import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_tr.actions.replace import Replace
from komand_tr.actions.replace.schema import Input


class TestReplace(TestCase):
    def setUp(self):
        self.action = Replace()

    @parameterized.expand(
        [
            [
                "with_two_arguments",
                "hello world",
                "a-z A-Z",
                "HELLO WORLD",
            ],
            [
                "with_three_arguments",
                "hello world",
                "-s [:lower:] 'X'",
                "X X",
            ],
        ]
    )
    def test_replace(self, name, text, expression, expected):
        response = self.action.run(
            {
                Input.TEXT: text,
                Input.EXPRESSION: expression,
            }
        )
        self.assertEqual(response.get("result"), expected)

    def test_replace_exception(self):
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.TEXT: "hello world",
                    Input.EXPRESSION: "--help",
                }
            )
        self.assertIn("Unsupported tr option.", str(context.exception))

    def test_replace_exception_for_command_injection(self):
        with self.assertRaises(PluginException) as context:
            self.action.run(
                {
                    Input.TEXT: "hello world",
                    Input.EXPRESSION: "-d x; whoami ; cat /etc/passwd #",
                }
            )
        self.assertIn("Text processing failed", str(context.exception))
