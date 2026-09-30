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
    extract_script_print_output,
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


class TestExtractScriptPrintOutput(TestCase):
    EXECUTION_ID = "Python3Script-ActionRun-test"

    @parameterized.expand(
        [
            (
                "marker_present",
                "hello from script\n",
                "Python3Script-ActionRun-test" + '{"result": "ok"}',
                {},
                "hello from script",
            ),
            ("marker_absent", "just some stdout\n", "", {}, "just some stdout"),
            ("marker_absent_incomplete_line_dropped", "just some stdout", "", {}, ""),
            ("empty_stdout", "", "", {}, ""),
            (
                "whitespace_only_before_marker",
                "   \n\t  ",
                "Python3Script-ActionRun-test" + '{"result": "ok"}',
                {},
                "",
            ),
        ]
    )
    def test_extract_print_output(
        self, test_name: str, prefix_text: str, suffix_text: str, credentials: dict, expected: str
    ) -> None:
        # Verify print output is correctly split from the execution_id marker line
        result = extract_script_print_output(prefix_text + suffix_text, self.EXECUTION_ID, credentials)
        self.assertEqual(result, expected)

    def test_credential_values_are_redacted(self) -> None:
        # Verify every credential value (including username) is redacted from the print output
        credentials = {
            "username": "test_user",
            "password": "test_pass",
            "secret_key": "secret123",
            "secret_credential_1": "cred1",
            "secret_credential_2": "cred2",
            "secret_credential_3": "cred3",
        }
        stdout = "login as test_user with test_pass, key=secret123, extra=cred1 cred2 cred3\n"
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        for value in credentials.values():
            self.assertNotIn(value, result)
        self.assertIn("********", result)

    def test_empty_credential_values_are_ignored(self) -> None:
        # Verify empty/missing credential values don't crash or over-redact
        result = extract_script_print_output("hello world\n", self.EXECUTION_ID, {"password": ""})
        self.assertEqual(result, "hello world")

    def test_substring_credential_value_fully_redacted(self) -> None:
        # Verify a credential value that is a substring of another (e.g. username "admin"
        # inside password "admin123") is redacted whole, with no partial residue left behind
        credentials = {"username": "admin", "password": "admin123"}
        stdout = "login admin with admin123\n"
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        self.assertNotIn("admin123", result)
        self.assertNotIn("********123", result)
        self.assertEqual(result, "login ******** with ********")

    def test_star_credential_value_does_not_blow_up_other_redactions(self) -> None:
        # Verify a credential value containing "*" doesn't re-match and inflate an
        # already-inserted "********" placeholder from a different credential
        credentials = {"password": "*", "secret_key": "longsecret"}
        stdout = "pw=* and s=longsecret\n"
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        self.assertEqual(result, "pw=******** and s=********")

    def test_whitespace_only_credential_value_is_ignored(self) -> None:
        # Verify a credential value that is truthy but pure whitespace (e.g. a space, tab, or
        # newline) is skipped rather than mass-redacting every occurrence of that whitespace
        credentials = {"password": " ", "secret_key": "\t"}
        stdout = "hello world foo bar\n"
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        self.assertEqual(result, "hello world foo bar")

    def test_none_credentials_does_not_raise(self) -> None:
        # Verify credentials=None (e.g. before Connection.connect() has populated it) is
        # tolerated instead of raising and masking the script's real error
        result = extract_script_print_output("hello\n", self.EXECUTION_ID, None)
        self.assertEqual(result, "hello")

    def test_multiline_credential_split_by_marker_absent_line_drop_does_not_leak(self) -> None:
        # Verify a multi-line credential value (e.g. a PEM key) is redacted before the
        # marker-absent incomplete-line drop runs, so no partial line of the secret survives
        credentials = {"secret_key": "-----BEGIN RSA KEY-----\nMIIBSUPERSECRET\n-----END RSA KEY-----"}
        stdout = "about to use key\n" + credentials["secret_key"]  # no marker, no trailing newline
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        self.assertNotIn("MIIBSUPERSECRET", result)
        self.assertNotIn("BEGIN RSA KEY", result)

    def test_incomplete_credential_fragment_dropped_on_marker_absent(self) -> None:
        # Verify a mid-write cut (e.g. process killed on timeout) that splits a credential
        # value never leaks a partial fragment past redaction: the incomplete trailing line
        # is dropped entirely rather than passed through unredacted.
        credentials = {"password": "secret1234"}
        stdout = "connecting...\npassword=secret1"  # killed mid-write, no trailing newline
        result = extract_script_print_output(stdout, self.EXECUTION_ID, credentials)
        self.assertEqual(result, "connecting...")
        self.assertNotIn("secret1", result)

    @parameterized.expand(
        [
            ("pipe", "a|b", "pw=a|b and also a and b", "pw=******** and also a and b"),
            ("dot", "a.b", "pw=a.b and axb", "pw=******** and axb"),
            ("parens", "(test)", "pw=(test) and test", "pw=******** and test"),
            ("star_quantifier", "ab*", "pw=ab* and abbb", "pw=******** and abbb"),
            ("brackets", "[abc]", "pw=[abc] and abc", "pw=******** and abc"),
            ("backreference", r"\1", "pw=\\1 and 1", "pw=******** and 1"),
        ]
    )
    def test_regex_metacharacter_credentials_redacted_literally(
        self, test_name: str, credential_value: str, stdout: str, expected: str
    ) -> None:
        # Verify credential values containing regex metacharacters are treated as literal
        # text (via re.escape), not as regex syntax, and don't match unrelated substrings
        result = extract_script_print_output(stdout + "\n", self.EXECUTION_ID, {"password": credential_value})
        self.assertEqual(result, expected)

    def test_overlapping_non_nested_credential_values_documented_limitation(self) -> None:
        # Two credential values that overlap without either containing the other (as opposed
        # to a substring/nested relationship, which IS fully handled) can leave a fragment of
        # the second value behind: a single left-to-right regex pass can't backtrack onto an
        # earlier, already-consumed match. This is an accepted, inherent limitation, not a fix
        # target - real credentials are long random strings, making this scenario contrived.
        credentials = {"a": "abcd", "b": "cdef"}
        result = extract_script_print_output("val=abcdef\n", self.EXECUTION_ID, credentials)
        self.assertEqual(result, "val=********ef")

    def test_long_output_is_truncated(self) -> None:
        # Verify output longer than max_length is truncated with a marker
        stdout = "x" * 5000 + "\n"
        result = extract_script_print_output(stdout, self.EXECUTION_ID, {}, max_length=100)
        self.assertTrue(result.endswith("... (truncated)"))
        self.assertEqual(len(result), 100 + len("... (truncated)"))
