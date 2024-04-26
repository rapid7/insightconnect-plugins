import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Callable, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_rss.connection.connection import Connection
from komand_rss.connection.schema import Input
from parameterized import parameterized

from mock import (
    mock_request_200,
    mock_request_400,
    mock_request_404,
    mock_request_500,
    mock_request_501,
    mock_request_503,
    mocked_request,
)
from util import STUB_CONNECTION


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()

    def run_connection_test(self, connection_parameters: Dict[str, Any]) -> Dict[str, Any]:
        self.connection.connect(connection_parameters)
        return self.connection.test()

    @parameterized.expand([(STUB_CONNECTION, {"success": True})])
    @patch("requests.request", side_effect=mock_request_200)
    def test_connection(
        self, connection_parameters: Dict[str, Any], expected: Dict[str, Any], mock_requests: MagicMock
    ) -> None:
        response = self.run_connection_test(connection_parameters)
        self.assertEqual(response, expected)
        mock_requests.assert_called_once()

    @parameterized.expand(
        [
            (
                mock_request_400,
                {**STUB_CONNECTION, Input.URL: "WrongURL"},
                "The provided URL is not valid.",
                "Please make sure that you entered the correct URL and try again.",
            ),
            (
                mock_request_400,
                STUB_CONNECTION,
                ConnectionTestException.causes[ConnectionTestException.Preset.BAD_REQUEST],
                ConnectionTestException.assistances[ConnectionTestException.Preset.BAD_REQUEST],
            ),
            (
                mock_request_404,
                STUB_CONNECTION,
                ConnectionTestException.causes[ConnectionTestException.Preset.NOT_FOUND],
                ConnectionTestException.assistances[ConnectionTestException.Preset.NOT_FOUND],
            ),
            (
                mock_request_500,
                STUB_CONNECTION,
                ConnectionTestException.causes[ConnectionTestException.Preset.SERVER_ERROR],
                ConnectionTestException.assistances[ConnectionTestException.Preset.SERVER_ERROR],
            ),
            (
                mock_request_501,
                STUB_CONNECTION,
                ConnectionTestException.causes[ConnectionTestException.Preset.UNKNOWN],
                ConnectionTestException.assistances[ConnectionTestException.Preset.UNKNOWN],
            ),
            (
                mock_request_503,
                STUB_CONNECTION,
                ConnectionTestException.causes[ConnectionTestException.Preset.SERVICE_UNAVAILABLE],
                ConnectionTestException.assistances[ConnectionTestException.Preset.SERVICE_UNAVAILABLE],
            ),
        ]
    )
    def test_connection_exception(
        self, mock_condition: Callable, connection_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        mocked_request(mock_condition)
        with self.assertRaises(ConnectionTestException) as context:
            self.run_connection_test(connection_parameters)
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
