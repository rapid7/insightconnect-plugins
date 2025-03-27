import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import EchoInput, EchoOutput, Input, Output

# Custom imports below
import smb


class Echo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="echo",
            description="Send a message to remote SMB/CIFS server and receive same message as reply if successful",
            input=EchoInput(),
            output=EchoOutput(),
        )

    def run(self, params={}):
        try:
            message = params.get(Input.MESSAGE).encode()
            echo_response = self.connection.conn.echo(message)
        except smb.smb_structs.OperationFailure as e:  # noqa: c-extension-no-member
            raise e
        except smb.base.SMBTimeout as e:  # noqa: c-extension-no-member
            raise PluginException(
                "Timeout reached when connecting to SMB endpoint. Validate network connectivity or "
                "extend connection timeout"
            ) from e
        except smb.base.NotReadyError as e:  # noqa: c-extension-no-member
            raise PluginException(
                "The SMB connection is not authenticated or the authentication has failed.  Verify the "
                "credentials of the connection in use."
            ) from e

        return {Output.RESPONSE: echo_response.decode()}
