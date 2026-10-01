import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_rapid7_intelhub.connection.connection import Connection
from parameterized import parameterized

from util import BASE_URL, STUB_CONNECTION, STUB_UNAUTHORIZED_CONNECTION, STUB_UNLICENSED_CONNECTION, Util


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection(self, mock_request: MagicMock) -> None:
        self.connection.connect(STUB_CONNECTION)
        self.assertEqual({"success": True}, self.connection.test())
        self.assertEqual(f"{BASE_URL}/cve", mock_request.call_args.kwargs["url"])

    @parameterized.expand(
        [
            [
                "unauthorized",
                STUB_UNAUTHORIZED_CONNECTION,
                "unauthorized",
                "Unauthorized",
                "Please verify your API key is valid and has access to Intelligence Hub.",
            ],
            [
                "license_not_found",
                STUB_UNLICENSED_CONNECTION,
                "license_not_found",
                "Product license not found.",
                "The API key is valid, but its organization has neither an InsightIDR nor an Intelligence Hub "
                "license. Use an API key from an organization that has one of them.",
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_raise_exception(
        self,
        _name: str,
        connection_params: dict,
        payload: str,
        cause: str,
        assistance: str,
        mock_request: MagicMock,
    ) -> None:
        self.connection.connect(connection_params)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(cause, context.exception.cause)
        self.assertEqual(assistance, context.exception.assistance)
        self.assertEqual(Util.read_file_to_string(f"payloads/{payload}.json.resp"), context.exception.data)
