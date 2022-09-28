import os
import sys
from typing import Callable
from unittest import mock

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase

from icon_darktrace.actions.update_watched_domains import UpdateWatchedDomains
from icon_darktrace.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException

from mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_405,
    mock_request_500,
    mocked_request,
)

STUB_ACTION_INPUT = {
    "description": "Watched Domains managed by InsightConnect",
    "entry": "",
    "expiration_time": "",
    "hostname": False,
    "source": "InsightConnect",
    "watched_domain_status": False,
}


class TestUpdateWatchedDomains(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = UpdateWatchedDomains()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_update_watched_domains_ok(self, mocked_request: mock.Mock) -> None:
        response = self.action.run(STUB_ACTION_INPUT)
        self.assertEqual(response, {"success": True, "added": 0, "updated": 0})

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_400, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_request_403, PluginException.causes[PluginException.Preset.API_KEY]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_405, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ]
    )
    def test_update_watched_domains_error(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
