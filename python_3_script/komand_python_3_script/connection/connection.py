import komand
from .schema import ConnectionSchema, Input

# Custom imports below
from subprocess import run, check_output, TimeoutExpired, CalledProcessError
import os


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.dependencies, self.timeout = None, None

    def connect(self, params={}):
        self.timeout = params.get(Input.TIMEOUT)
        self.dependencies = params.get(Input.MODULES)

    def test(self):
        self.logger.info("[*] Performing Python version check...\n")

        check = str(check_output(["python", "--version"]), "utf-8")
        self.logger.info(check)

        if "Python 3." not in check:
            raise Exception("[-] Python 3 is not installed correctly")

        if not self.dependencies:
            return {}

        self.logger.info(f"[*] Installing user-specified dependencies ({self.dependencies})...\n")
        self.install_dependencies()
        self.logger.info("[*] Dependencies installed!\n")

    @staticmethod
    def _set_pythonuserbase():
        os.environ.update({"PYTHONUSERBASE": "/var/cache/python_dependencies"})

    def install_dependencies(self):
        dependencies = " ".join(self.dependencies)
        command = f"pip install --user {dependencies}"

        self._set_pythonuserbase()

        try:
            run(args=command.split(" "), capture_output=True, timeout=self.timeout, check=True)
        except TimeoutExpired as e:
            raise Exception("Error: Installing Python dependencies exceeded timeout") from e
        except CalledProcessError as e:
            raise Exception("Error: Non-zero exit code returned. Message: %s" % e.output.decode("UTF8")) from e
