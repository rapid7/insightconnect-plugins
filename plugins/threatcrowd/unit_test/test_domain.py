import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase

from icon_threatcrowd.actions.domain import Domain
from icon_threatcrowd.actions.domain.schema import Input
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


class TestDomain(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = Domain()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {Input.DOMAIN: "https://example.com"}

    def test_domain_ok(self) -> None:
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {
            "domains": [
                {"ip_address": "-", "last_resolved": "2016-02-17"},
                {"ip_address": "198.51.100.1", "last_resolved": "2017-03-03"},
                {"ip_address": "198.51.100.1", "last_resolved": "2018-04-30"},
                {"ip_address": "198.51.100.1", "last_resolved": "2020-07-24"},
                {"ip_address": "198.51.100.1", "last_resolved": "2019-12-28"},
                {"ip_address": "198.51.100.1", "last_resolved": "2017-07-13"},
            ],
            "emails": ["user@example.com"],
            "found": True,
            "hashes": [],
            "malicious": "Malicious",
            "permalink": "https://www.threatcrowd.org/domain.php?domain=1119.leke.cn",
            "references": [],
            "subdomains": [],
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
    def test_domain_exception(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
