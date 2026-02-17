import os
import sys

sys.path.append(os.path.abspath("../"))

import base64
from typing import List
from unittest import TestCase

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sed.actions.process_bytes import ProcessBytes
from komand_sed.actions.process_bytes.schema import Input, Output
from komand_sed.util.constants import DEFAULT_ENCODING
from parameterized import parameterized

from util import Util


class TestProcessBytes(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ProcessBytes())

    @parameterized.expand(
        [
            ("basic_substitution", "hello world", ["s/world/universe/"], "", "hello universe"),
            ("multiple_expressions", "hello world", ["s/hello/hi/", "s/world/there/"], "", "hi there"),
            ("delete_line_with_pattern", "line1\nline2\nline3", ["/line2/d"], "", "line1\nline3"),
            ("global_replacement", "foo foo foo", ["s/foo/bar/g"], "", "bar bar bar"),
            ("binary_content", "test\x00data", ["s/test/modified/"], "", "modified\x00data"),
            ("empty_bytes", "", ["s/test/replaced/"], "", ""),
            ("no_match", "hello world", ["s/notfound/replacement/"], "", "hello world"),
        ]
    )
    def test_process_bytes(
        self, name: str, input_string: str, expression: List[str], options: str, expected_output: str
    ) -> None:
        # Convert expected output to base64 since that's what the action returns
        expected_base64 = base64.b64encode(expected_output.encode()).decode(DEFAULT_ENCODING)

        params = {Input.BYTES: input_string, Input.EXPRESSION: expression, Input.OPTIONS: options}

        result = self.action.run(params)
        self.assertEqual(result[Output.OUTPUT], expected_base64)

        # Verify the decoded content matches expected output
        decoded_result = base64.b64decode(result[Output.OUTPUT]).decode(DEFAULT_ENCODING)
        self.assertEqual(decoded_result, expected_output)

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
            ("invalid_expression_with_command_substitution", "test", ["$(ls)"], "", "Invalid input detected"),
            (
                "invalid_expression_with_etc_path",
                "test",
                ["s/test/replaced/; cat /etc/passwd"],
                "",
                "Invalid input detected",
            ),
            ("invalid_options_with_chmod", "test", ["s/test/replaced/"], "chmod +x", "Invalid input detected"),
        ]
    )
    def test_process_bytes_invalid_input(
        self, name: str, input_bytes: str, expression: List[str], options: str, expected_error: str
    ) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.BYTES: input_bytes, Input.EXPRESSION: expression, Input.OPTIONS: options})
        self.assertIn(expected_error, str(context.exception))

    def test_process_bytes_invalid_sed_syntax(self) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.BYTES: "test", Input.EXPRESSION: ["s/unclosed"], Input.OPTIONS: ""})
        self.assertIn("Sed command execution failed", str(context.exception))
