import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from paramiko import SSHClient
import paramiko


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.username = params.get(Input.USERNAME_PASSWORD).get("username")
        self.password = params.get(Input.USERNAME_PASSWORD).get("password")
        self.host = params.get(Input.SERVER)

    def test(self):
        self.logger.info("Testing connection to server...")
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh connect
        ssh.connect(self.host,
                    username=self.username,
                    password=self.password,
                    look_for_keys=False,
                    timeout=30)

        # ssh and run nmimport.pl
        test_command = f"pwd"
        stdin, stdout, stderr = ssh.exec_command(test_command)

        # This will hang if the output is excessive. Around 1000 records is the limit this will reasonablly read back from.
        stdout_str = stdout.read(1000)
        stderr_str = stderr.read(1000)

        ssh.close()

        self.logger.info("Test complete.")
        self.logger.info(f"STDOUT: {stdout_str.decode('utf-8').strip()}")
        self.logger.info(f"STDERR: {stderr_str.decode('utf-8').strip()}")

        if not stderr_str:
            return {"success": True}
        else:
            raise ConnectionTestException(cause="SSH to Firepower returned an error.",
                                          assistance=f"{stderr_str.decode('utf-8').strip()}")




