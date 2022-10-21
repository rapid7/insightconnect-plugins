import os
from subprocess import CalledProcessError, TimeoutExpired, check_output, run  # noqa: B404

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.dependencies, self.timeout = None, None
        self.script_credentials = None

    def connect(self, params={}):
        self.timeout = params.get(Input.TIMEOUT)
        self.dependencies = params.get(Input.MODULES)
        self.script_credentials = {
            "username": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("username"),
            "password": params.get(Input.SCRIPT_USERNAME_AND_PASSWORD, {}).get("password"),
            "secret_key": params.get(Input.SCRIPT_SECRET_KEY, {}).get("secretKey"),
        }

    def test(self):
        connection_test_output = {"success": True}

        self.logger.info("[*] Performing Python version check...")
        check = str(check_output(["python", "--version"]), "utf-8")  # noqa: B607,B603
        self.logger.info(check)

        if "Python 3." not in check:
            raise ConnectionTestException(cause="[-] Python 3 is not installed correctly")

        if not self.dependencies:
            return connection_test_output

        self.logger.info(f"[*] Installing user-specified dependencies ({self.dependencies})...")
        self.install_dependencies()
        self.logger.info("[*] Dependencies installed!\n")
        return connection_test_output

    @staticmethod
    def _set_pythonuserbase():
        os.environ.update({"PYTHONUSERBASE": "/var/cache/python_dependencies"})

    def install_dependencies(self):
        dependencies = " ".join(self.dependencies)
        command = f"pip install --user {dependencies}"

        self._set_pythonuserbase()

        try:
            run(args=command.split(" "), capture_output=True, timeout=self.timeout, check=True)  # noqa: B603
        except TimeoutExpired:
            raise ConnectionTestException(
                cause="Error: Installing Python dependencies exceeded timeout", assistance="Consider increasing timeout"
            )
        except CalledProcessError as error:
            raise ConnectionTestException(
                cause=f"Error: Non-zero exit code returned. Message: {error.output.decode('UTF8')}"
            )
