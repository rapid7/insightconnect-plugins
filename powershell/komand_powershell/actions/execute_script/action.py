import komand
from .schema import ExecuteScriptInput, ExecuteScriptOutput
import base64
from komand_powershell.util import util


class ExecuteScript(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='execute_script',
                description='Execute PowerShell script on a remote host or locally',
                input=ExecuteScriptInput(),
                output=ExecuteScriptOutput())

    def run(self, params={}):
        auth = self.connection.auth_type
        host_ip = params.get('address')
        encoded_powershell_script = params.get('script')
        username = self.connection.username
        password = self.connection.password
        port = self.connection.port
        # Set variables for Kerberos
        host_name = params.get('host_name')
        kdc = self.connection.kdc
        domain = self.connection.domain

        try:
            powershell_script = base64.b64decode(encoded_powershell_script)
        except base64.binascii.Error as e:
            self.logger.error('Base64 input' + encoded_powershell_script)
            raise Exception('While decoding the base64 into bytes the following error occurred' + e)
        except:
            self.logger.error('Base64 input ' + encoded_powershell_script)
            raise Exception('Something went wrong decoding the base64 script into bytes. See log for more information')
        try:
            powershell_script = powershell_script.decode('utf-8')
        except base64.binascii.Error as e:
            self.logger.error('Base64 input ' + encoded_powershell_script)
            self.logger.error('Base64 decoded as bytes' + powershell_script)
            raise Exception('While decoding the bytes into utf-8 the following error occurred' + e)
        except UnicodeDecodeError as e:
            self.logger.error('Base64 input ' + encoded_powershell_script)
            self.logger.error('Base64 decoded as bytes' + powershell_script)
            raise Exception('While decoding the bytes into utf-8 the following error occurred' + e)
        except:
            self.logger.error('Base64 input ' + encoded_powershell_script)
            self.logger.error('Base64 decoded as bytes' + powershell_script)
            raise Exception('Something went wrong decoding the base64 script bytes into utf-8.'
                            ' See log for more information')

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
        return str(new_string.encode("ascii", "ignore"), "utf-8")

    def test(self):
        # TODO: Implement test function
        return {}
