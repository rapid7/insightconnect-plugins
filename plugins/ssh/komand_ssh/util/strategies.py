from abc import ABC, abstractmethod
from base64 import b64decode
from io import StringIO
from logging import Logger

from paramiko import RSAKey, SSHClient

from .constants import DEFAULT_ENCODING


class SSHConnectionStrategy(ABC):
    def __init__(self, client: SSHClient, logger: Logger) -> None:
        self.client = client
        self.logger = logger

    @abstractmethod
    def connect(self, host: str, port: int, username: str, password: str, key: str = None) -> SSHClient:
        pass


class ConnectUsingPasswordStrategy(SSHConnectionStrategy):
    def connect(self, host: str, port: int, username: str, password: str, key: str = None) -> SSHClient:
        self.logger.info("Connecting to SSH server via password...")
        self.client.connect(host, port, username, password)
        return self.client


class ConnectUsingRSAKeyStrategy(SSHConnectionStrategy):
    def connect(self, host: str, port: int, username: str, password: str, key: str = None) -> SSHClient:
        self.logger.info("Connecting to SSH server via RSA key...")
        key = b64decode(key).decode(DEFAULT_ENCODING)
        rsa_key = RSAKey.from_private_key(StringIO(key), password=password)
        self.client.connect(host, port, username, password, pkey=rsa_key)
        return self.client
