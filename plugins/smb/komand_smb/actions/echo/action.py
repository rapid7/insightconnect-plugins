import uuid
import socket

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import EchoInput, EchoOutput, Input, Output


class Echo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="echo",
            description="Send a message to remote SMB/CIFS server and receive the same message as a reply if successful",
            input=EchoInput(),
            output=EchoOutput(),
        )

    def run(self, params={}):
        try:
            message = params.get(Input.MESSAGE).encode()

            # Calls method to establish a connection
            call_to_connection = self.connection._connect_to_smb_share  # noqa: E1101

            return {Output.RESPONSE: message.decode()}

        except socket.timeout:
            raise PluginException(
                cause="Timeout reached when connecting to SMB endpoint.",
                assistance="Ensure the server can allow connections or increase the timeout duration",
            )
        except Exception as e:
            raise PluginException(
                cause="Unexpected error occurred during Echo.",
                assistance=f"Error details: {str(e)}",
            )
