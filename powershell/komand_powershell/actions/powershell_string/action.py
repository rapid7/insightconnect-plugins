import komand
from .schema import PowershellStringInput, PowershellStringOutput
# Custom imports below
from komand_powershell.util import util


class PowershellString(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='powershell_string',
                description='Execute PowerShell script on a remote host or locally',
                input=PowershellStringInput(),
                output=PowershellStringOutput())

    def run(self, params={}):
        auth = self.connection.auth_type
        host_ip = params.get('address')
        powershell_script = params.get('script')
        username = self.connection.username
        password = self.connection.password
        port = self.connection.port
        # Set variables for Kerberos
        host_name = params.get('host_name')
        kdc = self.connection.kdc
        domain = self.connection.domain
        self.logger.debug(powershell_script)

        # This will run PowerShell on the linux VM
        if auth == 'None' or not host_ip:
            data = util.local(action=self, powershell_script=powershell_script)
            output = data['output']
            stderr = data['stderr']

            if output:
                output = self.safe_encode(output)

            if stderr:
                stderr = self.safe_encode(stderr)

            return {'stdout': output, 'stderr': stderr}

        # This code will run a PowerShell script with a NTLM connection
        if auth == 'NTLM':
            data = util.ntlm(action=self, host_ip=host_ip,
                             powershell_script=powershell_script,
                             username=username, password=password, port=port)
            output = data['output']
            stderr = data['stderr']

            if output:
                output = self.safe_encode(output)

            if stderr:
                stderr = self.safe_encode(stderr)

            return {'stdout': output, 'stderr': stderr}

        # This code will run a PowerShell script with a Kerberos account
        if auth == 'Kerberos':
            data = util.kerberos(action=self, host_ip=host_ip, kdc=kdc, domain=domain,
                                 host_name=host_name,
                                 powershell_script=powershell_script,
                                 password=password, username=username, port=port)
            output = data['output']
            stderr = data['stderr']

            if output:
                output = self.safe_encode(output)

            if stderr:
                stderr = self.safe_encode(stderr)

            return {'stdout': output, 'stderr': stderr}

    def safe_encode(self, in_byte):
        new_string = str(in_byte)
        return in_byte.replace("\u0000", "")

    def test(self):
        # TODO: Implement test function
        return {}
