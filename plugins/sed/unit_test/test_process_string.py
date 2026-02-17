import os
import sys
from typing import List

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sed.actions.process_string import ProcessString
from komand_sed.actions.process_string.schema import Input, Output
from parameterized import parameterized

from util import Util


class TestProcessString(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ProcessString())

    @parameterized.expand(
        [
            ("basic_substitution", "hello world", ["s/world/universe/"], "", "hello universe"),
            ("multiple_expressions", "hello world", ["s/hello/hi/", "s/world/there/"], "", "hi there"),
            ("delete_line_with_pattern", "line1\nline2\nline3", ["/line2/d"], "", "line1\nline3"),
            ("global_replacement", "foo foo foo", ["s/foo/bar/g"], "", "bar bar bar"),
            ("empty_string", "", ["s/test/replaced/"], "", ""),
            ("no_match", "hello world", ["s/notfound/replacement/"], "", "hello world"),
        ]
    )
    def test_process_string(
        self, name: str, input_string: str, expression: List[str], options: str, expected_output: str
    ) -> None:
        result = self.action.run({Input.STRING: input_string, Input.EXPRESSION: expression, Input.OPTIONS: options})
        self.assertEqual(result[Output.OUTPUT], expected_output)

    @parameterized.expand(
        [
            ("invalid_expression_with_semicolon", "test", ["s/test/replaced/; ls"], "", "Invalid input detected"),
            (
                "invalid_expression_with_pipe",
                "test",
                ["s/test/replaced/ | cat /etc/passwd"],
                "",
                "Invalid input detected",
            ),
            ("invalid_expression_with_backticks", "test", ["`whoami`"], "", "Invalid input detected"),
            (
                "invalid_options_with_dangerous_pattern",
                "test",
                ["s/test/replaced/"],
                "rm -rf",
                "Invalid input detected",
            ),
            ("invalid_expression_with_dollar_sign", "test", ["$(ls)"], "", "Invalid input detected"),
            (
                "invalid_expression_with_etc_path",
                "test",
                ["s/test/replaced/; cat /etc/passwd"],
                "",
                "Invalid input detected",
            ),
        ]
    )
    def test_process_string_invalid_input(
        self, name: str, input_string: str, expression: List[str], options: str, expected_error: str
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.STRING: input_string, Input.EXPRESSION: expression, Input.OPTIONS: options})
        self.assertIn(expected_error, str(context.exception))

    def test_process_string_invalid_sed_syntax(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.STRING: "test", Input.EXPRESSION: ["s/unclosed"], Input.OPTIONS: ""})
        self.assertIn("Sed command execution failed", str(context.exception))
