import sys
import os

sys.path.append(os.path.abspath("../"))

import logging
from subprocess import CalledProcessError
from unittest import TestCase
from unittest.mock import patch, MagicMock

from icon_python_3_script.connection.connection import Connection
from icon_python_3_script.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from parameterized import parameterized

from util import Util


class TestConnection(TestCase):
    @parameterized.expand(
        [
            [
                "all_dependencies_installed",
                {"modules": ["requests", "json"], "timeout": 60},
                None,
                False,
            ],
            [
                "missing_dependencies_install_success",
                {"modules": ["requests", "numpy"], "timeout": 60},
                None,
                True,
            ],
            [
                "pip_install_fails",
                {"modules": ["invalid_package_xyz"], "timeout": 60},
                "CalledProcessError",
                True,
            ],
        ]
    )
    @patch("importlib.util.find_spec")
    @patch("subprocess.run")
    def test_ensure_dependencies(
        self,
        test_name: str,
        connect_params: dict,
        mock_error: str | None,
        should_call_pip: bool,
        mock_subprocess_run: MagicMock,
        mock_find_spec: MagicMock,
    ) -> None:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect(connect_params)

        if test_name == "all_dependencies_installed":
            mock_find_spec.return_value = MagicMock()
            connection.ensure_dependencies()
            mock_subprocess_run.assert_not_called()

        elif test_name == "missing_dependencies_install_success":
            mock_find_spec.side_effect = lambda pkg: None if pkg == "numpy" else MagicMock()
            connection.ensure_dependencies()
            mock_subprocess_run.assert_called_once()

        elif test_name == "pip_install_fails":
            mock_find_spec.return_value = None
            mock_subprocess_run.side_effect = CalledProcessError(1, "pip", stderr=b"Package not found")
            with self.assertRaises(PluginException) as context:
                connection.ensure_dependencies()
            self.assertEqual(context.exception.cause, "Error: Failed to install Python dependencies")
            self.assertIn("Package not found", context.exception.data)

    def test_ensure_dependencies_no_dependencies(self) -> None:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect({"modules": [], "timeout": 60})
        connection.ensure_dependencies()

    @patch("subprocess.run")
    def test_install_dependencies_connection_test_exception(self, mock_subprocess_run: MagicMock) -> None:
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connect_params = {"modules": ["requests"], "timeout": 60}
        connection.connect(connect_params)

        mock_subprocess_run.side_effect = CalledProcessError(1, "pip", stderr=b"Installation failed")
        with self.assertRaises(ConnectionTestException) as context:
            connection.install_dependencies()
        self.assertIn("Error:", context.exception.cause)
