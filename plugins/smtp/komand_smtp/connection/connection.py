import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from typing import Any

# Custom imports below
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from komand_smtp.util.helpers import close_client


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.params = {}
        self.client = None

    def get(self) -> SMTP:
        host = self.params.get(Input.HOST, "").strip()
        port = self.params.get(Input.PORT, 25)
        use_ssl = self.params.get(Input.USE_SSL, True)
        credentials = self.params.get(Input.CREDENTIALS) or {}
        username = credentials.get("username", "").strip()
        password = credentials.get("password", "")

        self.logger.info(f"Connecting to {host}:{port}")
        client = None
        try:
            # Connect to the SMTP server
            client = SMTP(host, port, timeout=60)
            client.ehlo()

            # Upgrade to TLS if required
            if use_ssl:
                client.starttls()

            # Login if credentials were provided
            if username and password:
                client.login(username, password)
        except SMTPAuthenticationError as error:
            if client:
                close_client(client)
            raise PluginException(
                cause="Authentication to the SMTP server failed.",
                assistance="Verify that the username and password in the connection are correct.",
                data=error,
            )
        except (SMTPException, OSError, UnicodeError) as error:
            if client:
                close_client(client)
            raise PluginException(
                cause=f"Unable to connect to the SMTP server at {host}:{port}.",
                assistance="Verify the host, port and SSL settings of the connection and that the server is reachable.",
                data=error,
            )

        self.client = client
        return client

    def connect(self, params: dict[str, Any] = {}) -> None:
        self.params = params

    def test(self) -> dict[str, bool]:
        try:
            close_client(self.get())
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
