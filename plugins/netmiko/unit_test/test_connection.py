import sys
import os

sys.path.append(os.path.abspath("../"))

import base64
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import MagicMock, patch
from komand_netmiko.connection.connection import Connection
from komand_netmiko.connection.schema import Input

PASSWORD = "connection-password"
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nconnection-key\n-----END RSA PRIVATE KEY-----\n"


class TestConnection(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = MagicMock()

    @patch("komand_netmiko.connection.connection.ConnectHandler")
    def test_client(self, mock_connect_handler):
        keys = {
            "password": "",
            "key": base64.b64encode(PRIVATE_KEY.encode("utf-8")).decode("utf-8"),
        }
        for auth, private_key in keys.items():
            with self.subTest(auth=auth), TemporaryDirectory() as home:
                self.connection.logger.reset_mock()
                self.connection.parameters = {
                    Input.DEVICE_TYPE: "cisco_ios",
                    Input.HOST: "198.51.100.1",
                    Input.PORT: 22,
                    Input.CREDENTIALS: {"username": "user", "password": PASSWORD},
                    Input.SECRET: {"secretKey": ""},
                    Input.KEY: {"privateKey": private_key},
                }
                with patch("komand_netmiko.connection.connection.path.expanduser", return_value=home):
                    self.connection.client()

                # netmiko 4 ignores global_delay_factor in send_command unless delay_factor_compat is set
                self.assertEqual(mock_connect_handler.call_args.kwargs["global_delay_factor"], 4)
                self.assertTrue(mock_connect_handler.call_args.kwargs["delay_factor_compat"])
                logged = str(self.connection.logger.mock_calls)
                self.assertNotIn(PASSWORD, logged)
                self.assertNotIn("connection-key", logged)
