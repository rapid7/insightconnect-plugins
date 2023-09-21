import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_carbon_black_cloud.actions.quarantine import Quarantine
from icon_carbon_black_cloud.actions.quarantine.schema import Input, Output, QuarantineOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import (
    Util,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mock_request_409,
    mock_request_503,
    mocked_request,
)

STUB_AGENT_ID = "192.168.0.1"


class TestQuarantine(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Quarantine())
        self.payload = {Input.AGENT: STUB_AGENT_ID, Input.WHITELIST: [], Input.QUARANTINE_STATE: False}

    @patch("requests.post", side_effect=mock_request_200)
    def test_quarantine(self, mocked_post: MagicMock) -> None:
        response = self.action.run(self.payload)
        expected = {Output.QUARANTINED: False}
        validate(response, QuarantineOutput.schema)
        self.assertEqual(response, expected)
        mocked_post.assert_called()

    @parameterized.expand(
        [
            (mock_request_400, "400 Bad Request"),
            (mock_request_401, "Authentication Error"),
            (mock_request_403, "The specified object cannot be accessed or changed."),
            (mock_request_404, "The object referenced in the request cannot be found."),
            (mock_request_409, "Either the name you chose already exists, or there is an unacceptable character used."),
            (mock_request_503, PluginException.causes[PluginException.Preset.UNKNOWN]),
        ],
    )
    def test_quarantine_exception(self, mock_request: MagicMock, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
