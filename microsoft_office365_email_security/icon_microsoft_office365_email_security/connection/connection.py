import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
# Custom imports below
import subprocess
import os


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.username = params.get(Input.CREDENTIALS).get("username")
        self.password = params.get(Input.CREDENTIALS).get("password")
        self.o365_uri = params.get(Input.OFFICE_365_URL, 'https://ps.compliance.protection.outlook.com/powershell-liveid/')

    def test(self):
        self.logger.info(f"Connecting with: {self.username}")

        powershell = subprocess.Popen(['pwsh',
                                       '-ExecutionPolicy',
                                       'Unrestricted',
                                       '-File',
                                       '/powershell/Connection-Test.ps1',
                                       '-Username',
                                       self.username,
                                       '-Password',
                                       self.password],
                                      cwd=os.getcwd(),
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

        out, err = powershell.communicate()
        if err:
            self.logger.error(err)
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.UNAUTHORIZED
            )
