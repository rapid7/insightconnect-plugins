import os
import sys

sys.path.append(os.path.abspath("../"))

from subprocess import CalledProcessError, TimeoutExpired
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_python_3_script.util.util import environment_interpreter_path, environment_key
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from parameterized import parameterized

from util import Util


class TestConnection(TestCase):
    @parameterized.expand(
        [
            ("no_modules_uses_base_interpreter", []),
            ("with_modules_uses_environment_interpreter", ["requests"]),
        ]
    )
    def test_interpreter_selection(self, test_name: str, modules: list) -> None:
        # Verify interpreter selection based on module list
        connection = Util.make_connection(modules=modules)

        # Set expected interpreter based on test case
        if modules:
            expected_interpreter = str(environment_interpreter_path(environment_key(modules)))
        else:
            expected_interpreter = sys.executable

        # Assert correct interpreter was selected
        self.assertEqual(connection.interpreter, expected_interpreter)

    @parameterized.expand(
        [
            ("promotes_environment_when_absent", False, 1),
            ("discards_environment_on_collision", True, 0),
        ]
    )
    @patch("icon_python_3_script.connection.connection.tempfile.TemporaryDirectory")
    @patch("pathlib.Path.rename")
    @patch("icon_python_3_script.connection.connection.run")
    @patch("icon_python_3_script.connection.connection.environment_dir")
    def test_run_pip_install_promotion(
        self,
        test_name: str,
        environment_exists: bool,
        expected_rename_calls: int,
        mock_environment_dir: MagicMock,
        mock_run: MagicMock,
        mock_rename: MagicMock,
        mock_temporary_directory: MagicMock,
    ) -> None:
        # Set up environment mocks based on whether it exists
        mock_environment_dir.return_value = Util.final_directory_mock(exists=environment_exists)
        mock_temporary_directory.return_value = Util.temporary_directory_mock()
        connection = Util.make_connection(modules=["requests"])

        # Run pip install and verify environment promotion
        connection._run_pip_install()

        # Assert pip was called twice and environment was created once
        self.assertEqual(mock_run.call_count, 2)
        self.assertEqual(mock_rename.call_count, expected_rename_calls)

    @parameterized.expand(
        [
            ("pip_failure", CalledProcessError(1, "pip", stderr=b"package not found"), "package not found"),
            ("timeout", TimeoutExpired(cmd="pip", timeout=60), "timeout"),
        ]
    )
    @patch("icon_python_3_script.connection.connection.tempfile.TemporaryDirectory")
    @patch("icon_python_3_script.connection.connection.run")
    @patch("icon_python_3_script.connection.connection.environment_dir")
    def test_run_pip_install_wraps_errors(
        self,
        test_name: str,
        install_error: Exception,
        expected_message: str,
        mock_environment_dir: MagicMock,
        mock_run: MagicMock,
        mock_temporary_directory: MagicMock,
    ) -> None:
        # Verify subprocess errors are wrapped in RuntimeError
        mock_environment_dir.return_value = Util.final_directory_mock(exists=False)
        mock_temporary_directory.return_value = Util.temporary_directory_mock()
        mock_run.side_effect = [MagicMock(), install_error]
        connection = Util.make_connection(modules=["bad_package"])

        # Assert error is caught and wrapped
        with self.assertRaises(RuntimeError) as context:
            connection._run_pip_install()

        # Assert correct error message
        self.assertIn(expected_message, str(context.exception).lower())

    @parameterized.expand(
        [
            ("index_url", ["--index-url=http://evil.example"]),
            ("editable", ["-e", "git+ssh://example/repo"]),
            ("short_option", ["-r requirements.txt"]),
        ]
    )
    @patch("icon_python_3_script.connection.connection.run")
    def test_run_pip_install_rejects_injection(self, test_name: str, modules: list, mock_run: MagicMock) -> None:
        # Verify pip option injection is rejected
        connection = Util.make_connection(modules=modules)

        # Assert injection is detected and blocked
        with self.assertRaises(RuntimeError) as context:
            connection._run_pip_install()

        # Assert correct error message
        self.assertIn("Invalid module specifier", str(context.exception))
        mock_run.assert_not_called()

    @parameterized.expand(
        [
            ("no_modules_skips_install", [], False, False),
            ("environment_ready_skips_install", ["requests"], True, False),
            ("missing_environment_triggers_install", ["requests"], False, True),
        ]
    )
    @patch("icon_python_3_script.connection.connection.environment_ready")
    @patch("icon_python_3_script.connection.connection.Connection._run_pip_install")
    def test_ensure_dependencies_install_decision(
        self,
        test_name: str,
        modules: list,
        environment_ready: bool,
        expect_install: bool,
        mock_run_pip_install: MagicMock,
        mock_environment_ready: MagicMock,
    ) -> None:
        # Verify install is only triggered when needed
        mock_environment_ready.return_value = environment_ready
        connection = Util.make_connection(modules=modules)

        # Run ensure_dependencies and verify install behavior
        connection.ensure_dependencies()

        # Assert install was not called
        self.assertEqual(mock_run_pip_install.called, expect_install)

    @patch("icon_python_3_script.connection.connection.environment_ready", return_value=False)
    @patch(
        "icon_python_3_script.connection.connection.Connection._run_pip_install",
        side_effect=RuntimeError("install failed"),
    )
    def test_ensure_dependencies_pip_failure(
        self, mock_run_pip_install: MagicMock, mock_environment_ready: MagicMock
    ) -> None:
        # Verify pip failures are wrapped in PluginException
        connection = Util.make_connection(modules=["bad_package"])

        # Assert RuntimeError is caught and wrapped in PluginException
        with self.assertRaises(PluginException) as context:
            connection.ensure_dependencies()

        # Assert correct exception data
        self.assertEqual(context.exception.cause, "Error: Failed to install Python dependencies")
        self.assertIn("install failed", context.exception.data)

    @patch(
        "icon_python_3_script.connection.connection.Connection._run_pip_install",
        side_effect=RuntimeError("Installation failed"),
    )
    def test_install_dependencies_raises_exception(self, mock_run_pip_install: MagicMock) -> None:
        # Verify installation failures raise ConnectionTestException
        connection = Util.make_connection(modules=["requests"])

        # Assert RuntimeError is caught and wrapped in ConnectionTestException
        with self.assertRaises(ConnectionTestException) as context:
            connection.install_dependencies()

        # Assert correct exception data
        self.assertIn("Error:", context.exception.cause)
        self.assertIn("Installation failed", context.exception.cause)
