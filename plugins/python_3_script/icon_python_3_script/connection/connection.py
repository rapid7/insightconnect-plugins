import sys
import tempfile
from pathlib import Path
from subprocess import CalledProcessError, TimeoutExpired, check_output, run  # noqa: B404

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_python_3_script.util.constants import DEFAULT_CONNECTION_TIMEOUT, DEFAULT_ENCODING
from icon_python_3_script.util.util import (
    environment_dir,
    environment_interpreter_path,
    environment_key,
    environment_ready,
)

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.dependencies, self.timeout = [], DEFAULT_CONNECTION_TIMEOUT
        self.script_credentials = None
        self.interpreter = sys.executable

    def connect(self, params={}) -> None:
        self.timeout = params.get(Input.TIMEOUT, DEFAULT_CONNECTION_TIMEOUT)
        self.dependencies = params.get(Input.MODULES, [])
        self.script_credentials = {
            "username": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("username", ""),
            "password": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("password", ""),
            "secret_key": params.get(Input.SCRIPT_SECRET_KEY, {}).get("secretKey", ""),
            "secret_credential_1": params.get(Input.SECRET_CREDENTIAL_1, {}).get("secretKey", ""),
            "secret_credential_2": params.get(Input.SECRET_CREDENTIAL_2, {}).get("secretKey", ""),
            "secret_credential_3": params.get(Input.SECRET_CREDENTIAL_3, {}).get("secretKey", ""),
        }

        # Only point at a virtual environment when there are modules to install
        if self.dependencies:
            self.interpreter = str(environment_interpreter_path(environment_key(self.dependencies)))
        else:
            self.interpreter = sys.executable

    def test(self) -> dict[str, bool]:
        self.logger.info("[*] Performing Python version check...")
        python_version_output = str(check_output(["python", "--version"]), DEFAULT_ENCODING)  # noqa: B607,B603
        self.logger.info(python_version_output)

        # Ensure Python 3 is installed
        if "Python 3." not in python_version_output:
            raise ConnectionTestException(cause="[-] Python 3 is not installed correctly")

        # If we need to install additional dependencies, just install them
        if self.dependencies:
            self.logger.info(f"[*] Installing user-specified dependencies ({self.dependencies})...")
            self.install_dependencies()
            self.logger.info("[*] Dependencies installed!\n")
        return {"success": True}

    def _run_pip_install(self) -> None:
        # Reject anything pip would interpret as an option
        # Only package specifiers are permitted
        invalid_specifiers = [module for module in self.dependencies if module.strip().startswith("-")]
        if invalid_specifiers:
            raise RuntimeError(
                f"Invalid module specifier(s): {invalid_specifiers}. "
                "Entries starting with '-' are not allowed; provide package names only."
            )

        # Create virtual environment in a temporary directory first
        environment_hash = environment_key(self.dependencies)
        final_directory = environment_dir(environment_hash)
        final_directory.parent.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory(dir=str(final_directory.parent), prefix=".tmp_") as temporary_directory:
            temporary_directory = Path(temporary_directory)
            try:
                # Create virtual environment
                run(  # noqa: B603
                    args=[sys.executable, "-m", "venv", "--system-site-packages", str(temporary_directory)],
                    capture_output=True,
                    check=True,
                )

                # Install dependencies in temporary venv
                run(  # noqa: B603
                    args=[str(temporary_directory / "bin" / "python"), "-m", "pip", "install", "--no-input"]
                    + self.dependencies,
                    capture_output=True,
                    timeout=self.timeout,
                    check=True,
                )
            except TimeoutExpired:
                raise RuntimeError("Installing Python dependencies exceeded timeout. Consider increasing timeout.")
            except CalledProcessError as error:
                stderr = error.stderr.decode(DEFAULT_ENCODING) if error.stderr else ""
                raise RuntimeError(f"Non-zero exit code returned. Message: {stderr}")

            # Atomically promote to the final location only when fully installed
            # The Path.rename is atomic on POSIX within the same filesystem
            # If another worker already placed a complete environment just reuse it
            if not final_directory.exists():
                temporary_directory.rename(final_directory)

    def install_dependencies(self) -> None:
        try:
            self._run_pip_install()
        except RuntimeError as error:
            raise ConnectionTestException(cause=f"Error: {str(error)}")

    def ensure_dependencies(self) -> None:
        # Ensure dependencies are installed and if so return
        if not self.dependencies or environment_ready(environment_key(self.dependencies)):
            return

        # In case no required dependencies are installed, just install them
        self.logger.info("[*] Missing environment detected. Installing...")
        try:
            self._run_pip_install()
            self.logger.info("[*] Dependencies installed successfully!")
        except RuntimeError as error:
            raise PluginException(
                cause="Error: Failed to install Python dependencies",
                assistance="Check the error details and ensure all package names are correct.",
                data=str(error),
            )
