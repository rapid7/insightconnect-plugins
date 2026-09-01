import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from os import path
import os
import base64


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.device = {}
        self.device_connect = None

    def connect_key(self, params={}):
        home_dir = path.expanduser("~")
        key_file = f"{home_dir}/.ssh"
        if not path.exists(key_file):
            os.makedirs(key_file)
            os.chmod(key_file, 0o700)
        key_file_path = path.join(key_file, "id_rsa")
        with open(key_file_path, "w+", encoding="utf-8") as private_key:
            private_key.write(base64.b64decode(params.get(Input.KEY).get("privateKey")).decode("utf-8"))
        os.chmod(key_file_path, 0o600)
        self.logger.info("Establishing connection")
        device = {
            "device_type": params.get(Input.DEVICE_TYPE),
            "ip": params.get(Input.HOST),
            "username": params.get(Input.CREDENTIALS).get("username"),
            "use_keys": True,
            "key_file": key_file_path,
            "password": params.get(Input.CREDENTIALS).get("password"),
            "port": params.get(Input.PORT),
            "secret": params.get(Input.SECRET).get("secretKey"),
            "allow_agent": True,
            "global_delay_factor": 4,
        }
        self.device_connect = ConnectHandler(**device)
        return self.device_connect

    def connect_password(self, params={}):
        self.logger.info("Establishing connection")
        device = {
            "device_type": params.get(Input.DEVICE_TYPE),
            "ip": params.get(Input.HOST),
            "username": params.get(Input.CREDENTIALS).get("username"),
            "password": params.get(Input.CREDENTIALS).get("password"),
            "port": params.get(Input.PORT),
            "secret": params.get(Input.SECRET).get("secretKey"),
            "global_delay_factor": 4,
        }
        self.device_connect = ConnectHandler(**device)
        return self.device_connect

    def client(self, host=None):
        if host:
            self.parameters[Input.HOST] = host

        if self.parameters.get(Input.KEY, {}).get("privateKey"):
            self.logger.info("Using key...")
            self.logger.info(self.parameters)
            return self.connect_key(self.parameters)
        else:
            self.logger.info("Using password...")
            return self.connect_password(self.parameters)

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        try:
            self.client(params.get("host"))
        except (ValueError, OSError) as error:
            raise ConnectionTestException(
                cause="Cannot connect/configure this device.",
                assistance="Please check provided connection data and try again.",
                data=error,
            )

    def test(self):
        try:
            self.client().write_channel("\n")
            return {"success": True}
        except (ValueError, EOFError, SSHException):
            return {"success": False}
