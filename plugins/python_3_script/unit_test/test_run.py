import os
import subprocess
import sys
from pathlib import Path

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_python_3_script.actions.run import Run
from icon_python_3_script.util.util import extract_output_from_stdout
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util

# Fixed UUID used across subprocess tests to produce a deterministic execution ID
FIXED_UUID = "test-uuid-1234-5678-abcd-ef0123456789"
EXECUTION_ID = f"Python3Script-ActionRun-{FIXED_UUID}"
SUCCESS_OUTPUT_BYTES = EXECUTION_ID.encode() + b'{"result": "success"}'

STUB_FUNCTION = "def run(params={}):\n\treturn {'result': 'success'}"
STUB_PARAMETERS = {"test_input": "value"}
STUB_CREDENTIALS = {
    "username": "test_user",
    "password": "test_pass",
    "secret_key": "secret123",
    "secret_credential_1": "cred1",
    "secret_credential_2": "cred2",
    "secret_credential_3": "cred3",
}


class TestRun(TestCase):
    def setUp(self) -> None:
        self.uuid_patcher = patch("icon_python_3_script.actions.run.action.uuid4", return_value=FIXED_UUID)
        self.uuid_patcher.start()

        mock_path = MagicMock()
        mock_path.name = f"{EXECUTION_ID}.py"
        mock_path.is_file.return_value = True
        self.create_file_patcher = patch.object(Run, "_create_execution_file", return_value=mock_path)
        self.mock_create_file = self.create_file_patcher.start()

    def tearDown(self) -> None:
        self.uuid_patcher.stop()
        self.create_file_patcher.stop()
        for leftover in Path(__file__).parent.glob("Python3Script-ActionRun-*.py"):
            leftover.unlink(missing_ok=True)

    @parameterized.expand(
        [
            [
                Util.read_file_to_dict("inputs/connection_with_credentials.json.inp"),
                Util.read_file_to_dict("inputs/run_with_credentials.json.inp"),
                Util.read_file_to_dict("payloads/run_with_credentials.json.exp"),
            ],
            [
                Util.read_file_to_dict("inputs/connection_no_credentials.json.inp"),
                Util.read_file_to_dict("inputs/run_no_credentials.json.inp"),
                Util.read_file_to_dict("payloads/run_no_credentials.json.exp"),
            ],
        ]
    )
    @patch.object(Run, "_execute_function_as_process", side_effect=Util.mock_execute_function_as_process)
    def test_run(
        self,
        connection_params: Dict[str, Any],
        action_params: Dict[str, Any],
        expected: Dict[str, Any],
        mock_execute: MagicMock,
    ) -> None:
        # Run action with mocked subprocess and verify output matches expected result
        action = Util.default_connector(Run(), connection_params)
        response = action.run(params=action_params)
        validate(response, action.output.schema)
        self.assertEqual(response, expected)

    @patch.object(Run, "_execute_function_as_process", side_effect=Util.mock_execute_function_as_process)
    def test_run_return_none(self, mock_execute: MagicMock) -> None:
        # Verify None output raises PluginException
        params = Util.read_file_to_dict("inputs/run.bad.json.inp")
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException) as error:
            action.run(params=params)

        self.assertEqual(error.exception.cause, "Output type was None")
        self.assertEqual(error.exception.assistance, "Ensure that output has a non-None data type")

    @patch.object(Run, "_execute_function_as_process", side_effect=Util.mock_execute_function_as_process)
    def test_run_invalid_timeout(self, mock_execute: MagicMock) -> None:
        # Verify invalid timeout raises PluginException
        params = Util.read_file_to_dict("inputs/run.bad.timeout.json.inp")
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException) as error:
            action.run(params=params)

        self.assertEqual(error.exception.cause, "Invalid timeout value specified.")
        self.assertEqual(
            error.exception.assistance, "Please make sure the timeout value is greater than 0 and try again."
        )

    @patch.object(Run, "_execute_function_as_process", return_value={"result": "success"})
    def test_ensure_dependencies_called_with_dependencies(self, mock_execute: MagicMock) -> None:
        # Verify ensure_dependencies is called when modules are specified
        connection_params = {"modules": ["requests"], "timeout": 60}
        action_params = Util.read_file_to_dict("inputs/run_no_credentials.json.inp")
        action = Util.default_connector(Run(), connection_params)

        with patch.object(action.connection, "ensure_dependencies") as mock_ensure_deps:
            action.run(params=action_params)

        mock_ensure_deps.assert_called_once()

    @patch.object(Run, "_execute_function_as_process", return_value={"result": "success"})
    def test_ensure_dependencies_not_called_without_dependencies(self, mock_execute: MagicMock) -> None:
        # Verify ensure_dependencies is not called when no modules are specified
        connection_params = {"modules": [], "timeout": 60}
        action_params = Util.read_file_to_dict("inputs/run_no_credentials.json.inp")
        action = Util.default_connector(Run(), connection_params)

        with patch.object(action.connection, "ensure_dependencies") as mock_ensure_deps:
            action.run(params=action_params)

        mock_ensure_deps.assert_not_called()

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_success_returns_parsed_output(self, mock_check_output: MagicMock) -> None:
        # Verify successful subprocess execution returns parsed output
        mock_check_output.return_value = SUCCESS_OUTPUT_BYTES
        action = Util.default_connector(Run())
        result = action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=30)
        self.assertEqual(result, {"result": "success"})

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_temp_file_cleaned_up_on_success_and_failure(self, mock_check_output: MagicMock) -> None:
        # Verify temporary execution file is deleted on timeout
        mock_check_output.side_effect = subprocess.TimeoutExpired("cmd", 1800)
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException):
            action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=30)

        self.mock_create_file.return_value.unlink.assert_called_once()

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_timeout_multiplied_to_seconds(self, mock_check_output: MagicMock) -> None:
        # Verify timeout parameter is converted from minutes to seconds
        mock_check_output.return_value = SUCCESS_OUTPUT_BYTES
        action = Util.default_connector(Run())
        action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=5)
        self.assertEqual(mock_check_output.call_args[1]["timeout"], 5 * 60)

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_credentials_mapped_to_env_vars(self, mock_check_output: MagicMock) -> None:
        # Verify connection credentials are mapped to subprocess environment variables
        mock_check_output.return_value = SUCCESS_OUTPUT_BYTES
        action = Util.default_connector(Run())
        action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=30)
        env = mock_check_output.call_args[1]["env"]
        self.assertEqual(env["SCRIPT_USERNAME"], "test_user")
        self.assertEqual(env["SCRIPT_PASSWORD"], "test_pass")
        self.assertEqual(env["SCRIPT_SECRET_KEY"], "secret123")

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_missing_credentials_default_to_empty_string(self, mock_check_output: MagicMock) -> None:
        # Verify missing credentials default to empty strings in subprocess environment
        mock_check_output.return_value = SUCCESS_OUTPUT_BYTES
        action = Util.default_connector(Run())
        action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, {}, timeout=30)
        env = mock_check_output.call_args[1]["env"]
        self.assertEqual(env["SCRIPT_USERNAME"], "")
        self.assertEqual(env["SCRIPT_PASSWORD"], "")
        self.assertEqual(env["SCRIPT_SECRET_KEY"], "")

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_script_error_raises_plugin_exception_without_execution_id(
        self, mock_check_output: MagicMock
    ) -> None:
        # Verify script errors are wrapped in PluginException without execution ID in message
        stderr = f"{EXECUTION_ID}\nError: Script execution failed".encode()
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "cmd", stderr=stderr)
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException) as context:
            action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=30)

        self.assertNotIn("Python3Script-ActionRun", context.exception.cause)
        self.assertIn("Script execution failed", context.exception.cause)

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_timeout_raises_plugin_exception(self, mock_check_output: MagicMock) -> None:
        # Verify subprocess timeout is caught and wrapped in PluginException
        mock_check_output.side_effect = subprocess.TimeoutExpired("cmd", 1800)
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException) as context:
            action._execute_function_as_process(STUB_FUNCTION, STUB_PARAMETERS, STUB_CREDENTIALS, timeout=30)

        self.assertEqual(context.exception.cause, "Function timed out after 30 minutes.")

    @patch("icon_python_3_script.actions.run.action.subprocess.check_output")
    def test_subprocess_generic_exception_raises_plugin_exception(self, mock_check_output: MagicMock) -> None:
        # Verify generic OS errors are caught and wrapped in PluginException
        mock_check_output.side_effect = OSError("File not found")
        action_params = Util.read_file_to_dict("inputs/run_no_credentials.json.inp")
        action = Util.default_connector(Run())

        with self.assertRaises(PluginException) as context:
            action.run(params=action_params)

        self.assertIn("Could not run supplied script", context.exception.cause)
        self.assertIn("File not found", str(context.exception.data))

    @parameterized.expand(
        [
            ["json_dict", '{"key": "value"}', {"key": "value"}],
            ["number", "42", 42],
            ["list", "[1, 2, 3]", [1, 2, 3]],
            [
                "yaml_multiline",
                "\nresults:\n  - item1\n  - item2\nstatus: done\n",
                {"results": ["item1", "item2"], "status": "done"},
            ],
        ]
    )
    def test_extract_output_parses_supported_types(self, test_name: str, payload: str, expected: Any) -> None:
        # Verify extract_output handles various data types (dict, int, list, YAML)
        execution_id = "Python3Script-ActionRun-test"
        result = extract_output_from_stdout(execution_id + payload, execution_id)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ["none_uppercase", "None"],
            ["none_lowercase", "none"],
        ]
    )
    def test_extract_output_none_variants_return_none(self, test_name: str, payload: str) -> None:
        # Verify extract_output returns None for "None" and "none" strings
        execution_id = "Python3Script-ActionRun-test"
        self.assertIsNone(extract_output_from_stdout(execution_id + payload, execution_id))

    def test_extract_output_missing_prefix_returns_none(self) -> None:
        # Verify extract_output returns None when execution ID prefix is not found
        result = extract_output_from_stdout("Some output without the prefix", "Python3Script-ActionRun-missing")
        self.assertIsNone(result)


class TestRunEndToEnd(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Run())

    def tearDown(self) -> None:
        # Remove any execution files left by a failed or interrupted test
        for leftover in Path(__file__).parent.glob("Python3Script-ActionRun-*.py"):
            leftover.unlink(missing_ok=True)

    @parameterized.expand(
        [
            [
                "returns_dict",
                "def run(params={}):\n    return {'result': params.get('value')}",
                {"value": "hello"},
                {"result": "hello"},
            ],
            [
                "returns_list",
                "def run(params={}):\n    return params.get('items', [])",
                {"items": [1, 2, 3]},
                [1, 2, 3],
            ],
            [
                "no_input_params",
                "def run(params={}):\n    return {'static': True}",
                {},
                {"static": True},
            ],
        ]
    )
    def test_run_executes_real_subprocess(
        self, test_name: str, function_: str, input_params: dict, expected: Any
    ) -> None:
        # Run actual subprocess without mocking and verify output
        parameters = {"function": function_, "input": input_params, "timeout": 1}
        result = self.action.run(params=parameters)
        self.assertEqual(result, expected)

    def test_run_script_runtime_error_raises_plugin_exception(self) -> None:
        # Verify script runtime errors are caught and wrapped in PluginException
        parameters = {
            "function": "def run(params={}):\n    raise ValueError('bad input')",
            "input": {},
            "timeout": 1,
        }

        with self.assertRaises(PluginException):
            self.action.run(params=parameters)
