import os
import sys
from typing import List

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sed.actions.process_string import ProcessString
from komand_sed.actions.process_string.schema import Input, Output
from komand_sed.util.helper import Helper
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
            ("alternate_delimiter", "hello world", ["s|world|universe|"], "", "hello universe"),
            ("transliteration", "hello", ["y/helo/HELO/"], "", "HELLO"),
            ("address_delete", "line1\nline2\nline3", ["2d"], "", "line1\nline3"),
            ("address_range_delete", "line1\nline2\nline3\nline4", ["2,3d"], "", "line1\nline4"),
            ("address_print", "line1\nline2\nline3", ["3p"], "", "line1\nline2\nline3\nline3"),
            ("option_n_with_pattern_print", "line1\nline2\nline3", ["/line2/p"], "-n", "line2\n"),
            ("escaped_delimiter", "foo/bar", ["s/foo\\/bar/baz/"], "", "baz"),
        ]
    )
    def test_process_string(
        self, name: str, input_string: str, expression: List[str], options: str, expected_output: str
    ) -> None:
        result = self.action.run({Input.STRING: input_string, Input.EXPRESSION: expression, Input.OPTIONS: options})
        self.assertEqual(result[Output.OUTPUT], expected_output)

    @parameterized.expand(
        [
            ("e_flag_rejection", "test", ["s/foo/bar/e"], "", "Invalid expression detected"),
            ("w_command_rejection", "test", ["w /tmp/file"], "", "Invalid expression detected"),
            ("r_command_rejection", "test", ["1r /etc/passwd"], "", "Invalid expression detected"),
            ("R_command_rejection", "test", ["R /tmp/file"], "", "Invalid expression detected"),
            ("W_command_rejection", "test", ["W /tmp/file"], "", "Invalid expression detected"),
            ("F_command_rejection", "test", ["F"], "", "Invalid expression detected"),
            ("Q_command_rejection", "test", ["Q"], "", "Invalid expression detected"),
            ("e_command_rejection", "test", ["e"], "", "Invalid expression detected"),
            ("semicolon_rejection", "test", ["s/foo/bar/;s/baz/qux/"], "", "Invalid expression detected"),
            ("disallowed_options_file_flag", "test", ["s/foo/bar/"], "--file=script.sed", "Invalid options detected"),
            ("disallowed_options_i_flag", "test", ["s/foo/bar/"], "-i", "Invalid options detected"),
            ("disallowed_options_f_flag", "test", ["s/foo/bar/"], "-f script.sed", "Invalid options detected"),
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
        self.assertIn("Invalid expression detected", str(context.exception))

    def test_sandbox_flag_in_command(self) -> None:
        """Verify --sandbox is present at index 1 in the built command."""
        helper = Helper()
        cmd = helper._build_sed_command(["s/foo/bar/"], "")
        self.assertEqual(cmd[0], "sed")
        self.assertEqual(cmd[1], "--sandbox")
