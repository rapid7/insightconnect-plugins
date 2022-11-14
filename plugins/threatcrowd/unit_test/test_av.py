import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase

from icon_threatcrowd.actions.av import Av
from icon_threatcrowd.actions.av.schema import Input
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


class TestAv(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = Av()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {Input.ANTIVIRUS: "plugx"}

    def test_av_ok(self) -> None:
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {
            "found": True,
            "hashes": [
                "31d0e421894004393c48de1769744687",
                "5cd3f073caac28f915cf501d00030b31",
                "bbd9acdd758ec2316855306e83dba469",
                "ef9d8cd06de03bd5f07b01c1cce9761f",
                "06bd026c77ce6ab8d85b6ae92bb34034",
                "2af64ba808c79dccd2c1d84f010b22d7",
            ],
            "permalink": "https://www.threatcrowd.org/listMalware.php?antivirus=plugx",
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
    def test_address_exception(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
