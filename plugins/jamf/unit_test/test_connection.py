import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_400,
    mock_request_403,
    mock_request_404,
    mock_request_500,
    mock_request_505,
    mocked_request,
)
from util import Util


class TestConnection(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = Util.default_connection_connector(STUB_CONNECTION)

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mocked_get):
        response = self.connection.test()
        expected_response = {"connection": "successful"}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, ConnectionTestException.causes[ConnectionTestException.Preset.BAD_REQUEST]),
            (mock_request_403, ConnectionTestException.causes[ConnectionTestException.Preset.UNAUTHORIZED]),
            (mock_request_404, ConnectionTestException.causes[ConnectionTestException.Preset.NOT_FOUND]),
            (mock_request_500, ConnectionTestException.causes[ConnectionTestException.Preset.SERVER_ERROR]),
            (mock_request_505, ConnectionTestException.causes[ConnectionTestException.Preset.UNKNOWN]),
        ],
    )
    def test_connection_exception(self, mock_request, exception):
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(context.exception.cause, exception)
