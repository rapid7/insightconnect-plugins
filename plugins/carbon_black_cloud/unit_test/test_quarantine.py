import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock

from icon_carbon_black_cloud.actions.quarantine import Quarantine
from icon_carbon_black_cloud.actions.quarantine.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from mock import (
    mock_request_201,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_409,
    mocked_request,
)
from util import Util

STUB_PAYLOAD = {Input.AGENT: "ExampleAgent", Input.QUARANTINE_STATE: True, Input.WHITELIST: []}


class TestQuarantine(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Quarantine())

    @mock.patch("requests.post", side_effect=mock_request_201)
    def test_quarantine(self, mock_post: Mock) -> None:
        response = self.action.run(STUB_PAYLOAD)
        expected = {Output.QUARANTINED: True}
        self.assertEqual(response, expected)
        mock_post.assert_called()

    @parameterized.expand(
        [
            (mock_request_400, "400 Bad Request"),
            (mock_request_401, "Authentication Error"),
            (mock_request_403, "The specified object cannot be accessed or changed."),
            (mock_request_404, "The object referenced in the request cannot be found."),
            (mock_request_409, "Either the name you chose already exists, or there is an unacceptable character used."),
        ],
    )
    def test_quarantine_exception(self, mock_request: Mock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(
            context.exception.cause,
            exception,
        )
