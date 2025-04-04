from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

import socket
import uuid
from smbprotocol.connection import Connection as SMBProtoConnection
from smbprotocol.session import Session
from smbprotocol.tree import TreeConnect


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        self.conn = None
        self.session = None
        self.host = None
        self.port = None
        self.domain = None
        self.username = None
        self.password = None
        self.timeout = None
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.host = params.get("host")
        self.port = params.get("port")
        self.domain = params.get("domain", "")
        self.username = params["credentials"]["username"]
        self.password = params["credentials"]["password"]
        self.timeout = params.get(Input.TIMEOUT, 30)

        try:
            self.conn = SMBProtoConnection(guid=uuid.uuid4(), server_name=self.host, port=self.port)
            self.conn.connect(timeout=self.timeout)

            self.session = Session(self.conn, self.username, self.password, self.domain)
            self.session.connect()

            tree = TreeConnect(self.session, rf"\\{self.host}\IPC$")
            tree.connect()

            self.logger.info("Successfully authenticated to SMB server.")

        except socket.timeout:
            raise PluginException(
                cause="Timeout reached when connecting to SMB endpoint.",
                assistance="Ensure the server can allow connections or increase the timeout duration",
            )
        except PluginException as error:
            self.logger.error(f"Error connecting to SMB server: {error}")
            raise

    def _connect_to_smb_share(self, share_name):
        try:
            tree = TreeConnect(self.session, rf"\\{self.host}\{share_name}")
            tree.connect()
            self.logger.info(f"Successfully connected to SMB server: {share_name}")
            return tree

        except PluginException as error:
            self.logger.error(f"Failed to connect to SMB server: '{share_name}': {error}")
            raise PluginException(f"Unable to connect to SMB server: '{share_name}'. Error: {error}")

    def test(self):
        try:
            tree = TreeConnect(self.session, rf"\\{self.conn.server_name}\IPC$")
            tree.connect()
            self.logger.info("Connectivity test to SMB server was successful")
            return

        except PluginException as error:
            raise ConnectionTestException(cause="Connection test to SMB server failed.", assistance=error)
