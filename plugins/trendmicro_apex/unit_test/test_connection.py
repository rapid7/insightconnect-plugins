import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.connection.connection import Connection
import logging
from mock import STUB_CONNECTION, mock_request_200_connection, mocked_request


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestConnectionTest(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection Logger")
        self.connection.connect(STUB_CONNECTION)

    # @patch("requests.request", side_effect=mock_request_200_connection)
    # def test_connection_test(self, mock_get, mock_token) -> None:
    #     # breakpoint()
    #     mocked_request(mock_get)
    #     response = Connection().test()
    #     self.assertEqual(response, {"success": True})
