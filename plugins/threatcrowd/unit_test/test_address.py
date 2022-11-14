import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase, mock
from unittest.mock import Mock

from icon_threatcrowd.actions.address import Address
from icon_threatcrowd.actions.address.schema import Input
from icon_threatcrowd.connection.connection import Connection
from parameterized import parameterized

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_401,
    mock_request_404,
    mock_request_500,
    mock_request_503,
    mocked_request,
)


class TestAddress(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = Address()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {Input.DOMAIN: "198.51.100.1"}

    @mock.patch("icon_threatcrowd.actions.address.Address.ip_check")
    def test_address_ok(self, mocked_ip_check: Mock) -> None:
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {
            "domains": [
                {"domain": "example.com", "last_resolved": "2018-09-03"},
                {"domain": "example2.com", "last_resolved": "2018-07-14"},
                {"domain": "example3.com", "last_resolved": "2020-06-17"},
            ],
            "found": True,
            "hashes": [],
            "malicious": "50/50 chance malicious",
            "permalink": "https://www.threatcrowd.org/ip.php?ip=13.33.17.182",
            "references": [],
        }
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE]),
        ],
    )
    @mock.patch("icon_threatcrowd.actions.address.Address.ip_check")
    def test_address_exception(self, mock_request: Callable, exception: str, mocked_ip_check: Mock) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
