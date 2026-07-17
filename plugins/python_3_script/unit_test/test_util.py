import os
import sys

sys.path.append(os.path.abspath("../"))

from pathlib import Path
from typing import Any
from unittest import TestCase
from unittest.mock import patch

from icon_python_3_script.util.constants import ENVIRONMENT_BASE_DIRECTORY
from icon_python_3_script.util.util import (
    _canonical_spec,
    environment_dir,
    environment_interpreter_path,
    environment_key,
    environment_ready,
    extract_output_from_stdout,
)
from parameterized import parameterized


class TestCanonicalSpec(TestCase):
    def test_numpy_version_equivalence(self) -> None:
        # Verify whitespace and case differences don't affect canonical spec
        self.assertEqual(_canonical_spec("numpy==1.26"), _canonical_spec("numpy == 1.26"))
        self.assertEqual(_canonical_spec("numpy==1.26"), _canonical_spec("NumPy==1.26"))

    def test_different_versions_differ(self) -> None:
        # Verify different version specs produce different canonical specs
        self.assertNotEqual(_canonical_spec("numpy"), _canonical_spec("numpy>1"))
        self.assertNotEqual(_canonical_spec("numpy==1.25"), _canonical_spec("numpy==1.26"))

    def test_extras_differ(self) -> None:
        # Verify package extras change the canonical spec
        self.assertNotEqual(_canonical_spec("requests[security]"), _canonical_spec("requests"))

    def test_malformed_specification_no_raise(self) -> None:
        # Verify malformed specs don't crash, return string
        result = _canonical_spec("not!valid!@#$")
        self.assertIsInstance(result, str)


class TestEnvironmentKey(TestCase):
    def test_order_independent(self) -> None:
        # Verify key is same regardless of module list order
        self.assertEqual(environment_key(["numpy", "pandas"]), environment_key(["pandas", "numpy"]))

    def test_deduplication(self) -> None:
        # Verify duplicate modules produce same key as single module
        self.assertEqual(environment_key(["numpy", "numpy"]), environment_key(["numpy"]))

    def test_whitespace_equivalence(self) -> None:
        # Verify whitespace differences don't affect key
        self.assertEqual(environment_key(["numpy==1.26"]), environment_key(["numpy == 1.26"]))

    def test_case_equivalence(self) -> None:
        # Verify case differences don't affect key
        self.assertEqual(environment_key(["NumPy==1.26"]), environment_key(["numpy==1.26"]))

    def test_different_version_constraints_differ(self) -> None:
        # Verify different version specs produce different keys
        self.assertNotEqual(environment_key(["numpy"]), environment_key(["numpy>1"]))
        self.assertNotEqual(environment_key(["numpy==1.25"]), environment_key(["numpy==1.26"]))

    def test_empty_list_stable(self) -> None:
        # Verify empty list produces consistent key
        self.assertEqual(environment_key([]), environment_key([]))

    def test_returns_hexadecimal_string(self) -> None:
        # Verify key is 64-character hexadecimal hash
        key = environment_key(["numpy"])
        self.assertEqual(len(key), 64)
        int(key, 16)


class TestEnvironmentDirAndInterpreterPath(TestCase):
    def test_environment_directory_and_interpreter_paths(self) -> None:
        # Verify correct directory and interpreter paths are derived from key
        key = "abc123"
        self.assertEqual(environment_dir(key), Path(ENVIRONMENT_BASE_DIRECTORY) / key)
        self.assertEqual(environment_interpreter_path(key), Path(ENVIRONMENT_BASE_DIRECTORY) / key / "bin" / "python")


class TestEnvironmentReady(TestCase):
    @patch("icon_python_3_script.util.util.environment_interpreter_path")
    def test_ready_when_interpreter_exists(self, mock_path) -> None:
        # Verify environment is ready when interpreter file exists
        key = environment_key(["numpy"])
        mock_path.return_value.is_file.return_value = True
        self.assertTrue(environment_ready(key))

    @patch("icon_python_3_script.util.util.environment_interpreter_path")
    def test_not_ready_when_interpreter_missing(self, mock_path) -> None:
        # Verify environment is not ready when interpreter file is missing
        key = environment_key(["numpy"])
        mock_path.return_value.is_file.return_value = False
        self.assertFalse(environment_ready(key))


class TestExtractOutputFromStdout(TestCase):
    @parameterized.expand(
        [
            (
                "dict_output",
                "Python3Script-ActionRun-123",
                '{"key": "value", "nested": {"inner": "data"}}',
                {"key": "value", "nested": {"inner": "data"}},
            ),
            ("list_output", "Python3Script-ActionRun-list", "[1, 2, 3]", [1, 2, 3]),
            ("scalar_number_output", "Python3Script-ActionRun-789", "42", 42),
            ("scalar_string_output", "Python3Script-ActionRun-456", '"simple_string"', "simple_string"),
        ]
    )
    def test_extract_output_parses_content(self, test_name: str, execution_id: str, stdout: str, expected: Any) -> None:
        # Verify extract_output correctly parses various data types from stdout
        result = extract_output_from_stdout(execution_id + stdout, execution_id)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ("none_uppercase", "Python3Script-ActionRun-none", "None"),
            ("none_lowercase", "Python3Script-ActionRun-none-lower", "none"),
            ("prefix_not_found", "Python3Script-ActionRun-missing", "Some output without the prefix"),
        ]
    )
    def test_extract_output_returns_none(self, test_name: str, execution_id: str, stdout: str) -> None:
        # Verify extract_output returns None for None values and missing prefixes
        result = extract_output_from_stdout(stdout, execution_id)
        self.assertIsNone(result)
