import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
import base64
import paramiko
import io
from typing import Dict, Any


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.host = None

    def connect_key(self, params: Dict[str, Any]) -> paramiko.SSHClient:
        self.logger.info("Connecting via key...")
        key = base64.b64decode(params.get(Input.KEY, {}).get("secretKey")).strip().decode("utf-8")
        fd = io.StringIO(key)
        rsa_key = paramiko.RSAKey.from_private_key(fd, password=params.get(Input.PASSWORD, {}).get("secretKey"))

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # noqa B507
        ssh_client.load_system_host_keys()

        ssh_client.connect(
            params.get(Input.HOST), params.get(Input.PORT), username=params.get(Input.USERNAME), pkey=rsa_key
        )
        return ssh_client

    def connect_password(self, params: Dict[str, Any]) -> paramiko.SSHClient:
        self.logger.info("Connecting via password")
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # noqa B507
        ssh_client.load_system_host_keys()
        ssh_client.connect(
            params.get(Input.HOST),
            params.get(Input.PORT),
            params.get(Input.USERNAME),
            params.get(Input.PASSWORD, {}).get("secretKey"),
        )
        return ssh_client

    def client(self, host: str = None) -> paramiko.SSHClient:
        if host:
            self.parameters["host"] = host
        if self.parameters.get(Input.USE_KEY):
            return self.connect_key(self.parameters)
        else:
            return self.connect_password(self.parameters)

    def connect(self, params={}) -> None:
        self.logger.info("Connecting...")
        self.host = params.get(Input.HOST)

    def test(self) -> Dict[str, Any]:
        try:
            client = self.client(self.host)
            client.close()
            return {"success": True}
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
