import sys

sys.path.append("../")

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_python_3_script.actions.run import Run
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from jsonschema import validate

from util import Util


@patch.object(Run, "_exec_python_function", side_effect=Util.mock_exec_python_function)
class TestRun(TestCase):
    @parameterized.expand(
        [
            [
                Util.read_file_to_dict(f"inputs/connection_with_credentials.json.inp"),
                Util.read_file_to_dict(f"inputs/run_with_credentials.json.inp"),
                Util.read_file_to_dict(f"payloads/run_with_credentials.json.exp"),
            ],
            [
                Util.read_file_to_dict(f"inputs/connection_no_credentials.json.inp"),
                Util.read_file_to_dict(f"inputs/run_no_credentials.json.inp"),
                Util.read_file_to_dict(f"payloads/run_no_credentials.json.exp"),
            ],
        ]
    )
    def test_run(
        self,
        mock_exec_python_function: MagicMock,
        connection_params: Dict[str, Any],
        action_params: Dict[str, Any],
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(Run(), connection_params)
        response = action.run(params=action_params)
        validate(response, action.output.schema)
        self.assertEqual(response, expected)

    def test_run_return_none(self, mock_exec_python_function: MagicMock) -> None:
        params = Util.read_file_to_dict(f"inputs/run.bad.json.inp")
        action = Util.default_connector(Run())
        with self.assertRaises(PluginException) as error:
            action.run(params=params)
        self.assertEqual(error.exception.cause, "Output type was None")
        self.assertEqual(error.exception.assistance, "Ensure that output has a non-None data type")

    def test_run_invalid_timeout(self, mock_exec_python_function: MagicMock) -> None:
        params = Util.read_file_to_dict(f"inputs/run.bad.timeout.json.inp")
        action = Util.default_connector(Run())
        with self.assertRaises(PluginException) as error:
            action.run(params=params)
        self.assertEqual(error.exception.cause, "Invalid timeout value specified.")
        self.assertEqual(
            error.exception.assistance, "Please make sure the timeout value is greater than 0 and try again."
        )

    @parameterized.expand(
        [
            ["def run(params={}):\n\treturn {'username': username}", "\t"],
            ["def run(params={}):\n\t\treturn {'username': username}", "\t\t"],
            ["def run(params={}):\n\t return {'username': username}", "\t "],
            ["def run(params={}):\n return {'username': username}", " "],
            ["def run(params={}):\n  return {'username': username}", "  "],
            ["def run(params={}):\n   return {'username': username}", "   "],
            ["def run(params={}):\n    return {'username': username}", "    "],
        ]
    )
    def test_check_indentation_character(
        self, mock_exec_python_function: MagicMock, function_: str, expected: str
    ) -> None:
        action = Util.default_connector(Run())
        response = action._check_indentation_character(function_)
        self.assertEqual(response, expected)
