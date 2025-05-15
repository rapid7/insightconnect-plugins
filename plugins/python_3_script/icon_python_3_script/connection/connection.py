import sys
import os
from subprocess import CalledProcessError, TimeoutExpired, check_output, run  # noqa: B404

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from .schema import ConnectionSchema, Input
from typing import Dict, Any


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.dependencies, self.timeout = None, None
        self.script_credentials = None

    def connect(self, params={}) -> None:
        self.timeout = params.get(Input.TIMEOUT, 60)
        self.dependencies = params.get(Input.MODULES, [])
        self.script_credentials = {
            "username": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("username"),
            "password": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("password"),
            "secret_key": params.get(Input.SCRIPT_SECRET_KEY, {}).get("secretKey"),
            "secret_credential_1": params.get(Input.SECRET_CREDENTIAL_1, {}).get("secretKey"),
            "secret_credential_2": params.get(Input.SECRET_CREDENTIAL_2, {}).get("secretKey"),
            "secret_credential_3": params.get(Input.SECRET_CREDENTIAL_3, {}).get("secretKey"),
        }

    def test(self) -> Dict[str, Any]:
        self.logger.info("[*] Performing Python version check...")
        python_version = str(check_output(["python", "--version"]), "utf-8")  # noqa: B607,B603
        self.logger.info(python_version)

        if "Python 3." not in python_version:
            raise ConnectionTestException(cause="[-] Python 3 is not installed correctly")

        if self.dependencies:
            self.logger.info(f"[*] Installing user-specified dependencies ({self.dependencies})...")
            self.install_dependencies()
            self.logger.info("[*] Dependencies installed!\n")
        return {"success": True}

    @staticmethod
    def _set_python_userbase() -> None:
        os.environ.update({"PYTHONUSERBASE": "/var/cache/python_dependencies"})

    def install_dependencies(self) -> None:
        self._set_python_userbase()
        try:
            run(  # noqa: B603
                args=[sys.executable, "-m", "pip", "install"] + self.dependencies,
                capture_output=True,
                timeout=self.timeout,
                check=True,
            )
        except TimeoutExpired:
            raise ConnectionTestException(
                cause="Error: Installing Python dependencies exceeded timeout", assistance="Consider increasing timeout"
            )
        except CalledProcessError as error:
            raise ConnectionTestException(
                cause=f"Error: Non-zero exit code returned. Message: {error.output.decode('utf-8')}"
            )
