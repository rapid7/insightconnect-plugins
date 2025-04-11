from typing import Any, Dict

import insightconnect_plugin_runtime

# Custom imports below
import paramiko
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_ssh.util.policies import CustomMissingKeyPolicy
from komand_ssh.util.strategies import ConnectUsingPasswordStrategy, ConnectUsingRSAKeyStrategy

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.use_key = None
        self.key = None

    def connect(self, params={}) -> None:
        self.logger.info("Connecting...")
        self.host = params.get(Input.HOST, "").strip()
        self.port = params.get(Input.PORT, 22)
        self.username = params.get(Input.USERNAME, "").strip()
        self.password = params.get(Input.PASSWORD, {}).get("secretKey", "").strip()
        self.use_key = params.get(Input.USE_KEY, False)
        self.key = params.get(Input.KEY, {}).get("secretKey", "").strip()

    def client(self, host: str = None) -> paramiko.SSHClient:
        # Create fresh client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(CustomMissingKeyPolicy())

        # Update host only if entered and different from host in connection
        if host and host != self.host:
            self.host = host

        # Select connection strategy
        connection_strategy = ConnectUsingRSAKeyStrategy if self.use_key else ConnectUsingPasswordStrategy

        # Return SSH client
        try:
            return connection_strategy(ssh_client, self.logger).connect(
                self.host, self.port, self.username, self.password, self.key
            )
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def test(self) -> Dict[str, Any]:
        try:
            client = self.client(self.host)
            client.close()
            return {"success": True}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
