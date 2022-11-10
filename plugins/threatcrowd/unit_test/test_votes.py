import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase

from icon_threatcrowd.actions.votes import Votes
from icon_threatcrowd.actions.votes.schema import Input
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


class TestVotes(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = Votes()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {Input.ENTITY: "user@example.com", Input.VOTE: False}

    def test_votes_ok(self) -> None:
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {"status": "200"}
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, "Vote submission failed for unknown reason."),
            (mock_request_401, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE]),
        ],
    )
    def test_votes_exception(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
