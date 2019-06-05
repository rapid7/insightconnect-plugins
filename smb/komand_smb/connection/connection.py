import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from smb.SMBConnection import SMBConnection
import socket


class Connection(komand.Connection):

    def __init__(self):
        self.conn = None
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        username = params["credentials"]["username"]
        password = params["credentials"]["password"]
        host = params["host"]
        port = params["port"]
        netbios_name = params["netbios_name"]
        domain = params.get("domain", None)
        use_ntvlm_v2 = params.get("use_ntlmv2", True)
        is_direct_tcp = True

        if domain:
            self.conn = SMBConnection(username, password, "InsightConnect", netbios_name, domain=domain,
                                      use_ntlm_v2=use_ntvlm_v2, is_direct_tcp=is_direct_tcp)
        else:
            self.conn = SMBConnection(username, password, "InsightConnect", netbios_name, use_ntlm_v2=use_ntvlm_v2,
                                      is_direct_tcp=is_direct_tcp)

        try:
            result = self.conn.connect(host, port, timeout=params.get(Input.TIMEOUT))
            if not result:
                error = "Failed to authenticate to SMB endpoint. Validate credentials and connection details."
                raise Exception(error)
        except socket.timeout:
            raise Exception("Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                            "extend connection timeout")
        except Exception as e:
            self.logger.error(f"Error connecting to SMB endpoint: {e}")
            raise

    def test(self):
        from komand.exceptions import ConnectionTestException

        message = "Hello World"
        try:
            echo_response = self.conn.echo(message.encode())
        except Exception as e:
            raise ConnectionTestException(cause="Connectivity test to SMB server failed.", assistance=e)

        if echo_response.decode() == message:
            self.logger.info("Connectivity test to SMB server was successful")
            return
        else:
            raise ConnectionTestException(cause="Connectivity test to SMB server failed.", assistance="echo response was not as expected")
