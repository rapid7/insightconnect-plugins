from typing import Any
from unittest.mock import MagicMock

from komand_smtp.connection.schema import Input as ConnectionInput

CONTENT = "UmFwaWQ3IEluc2lnaHRDb25uZWN0"
DECODED_CONTENT = b"Rapid7 InsightConnect"

CONNECTION_PARAMS = {
    ConnectionInput.HOST: "smtp.example.com",
    ConnectionInput.PORT: 25,
    ConnectionInput.USE_SSL: True,
    ConnectionInput.CREDENTIALS: {"username": "user", "password": "pass"},
}


class Util:
    @staticmethod
    def file(name: str, content: str = CONTENT) -> dict[str, str]:
        return {"filename": name, "content": content}

    @staticmethod
    def mock_connection(smtp_mock: MagicMock) -> MagicMock:
        """Return an action connection mock that hands out the patched SMTP client"""
        smtp_mock.return_value.sendmail.return_value = {}  # smtplib returns the refused recipients
        connection = MagicMock()
        connection.get.return_value = smtp_mock.return_value
        return connection
