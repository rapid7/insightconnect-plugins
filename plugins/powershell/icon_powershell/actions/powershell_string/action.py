import insightconnect_plugin_runtime
from .schema import PowershellStringInput, PowershellStringOutput, Input, Component

# Custom imports below
from icon_powershell.util import util


class PowershellString(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="powershell_string",
            description=Component.DESCRIPTION,
            input=PowershellStringInput(),
            output=PowershellStringOutput(),
        )

    def run(self, params={}):
        host_ip = params.get(Input.ADDRESS)
        powershell_script = params.get(Input.SCRIPT)
        host_name = params.get(Input.HOST_NAME)

        powershell_script = util.add_credentials_to_script(powershell_script, self.connection.script_credentials)

        return util.run_powershell_script(
            auth=self.connection.auth_type,
            action=self,
            host_ip=host_ip,
            kdc=self.connection.kdc,
            domain=self.connection.domain,
            host_name=host_name,
            powershell_script=powershell_script,
            password=self.connection.password,
            username=self.connection.username,
            port=self.connection.port,
        )

    @staticmethod
    def safe_encode(in_byte: str) -> str:
        return in_byte.replace("\u0000", "")
