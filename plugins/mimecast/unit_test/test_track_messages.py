import os
import sys
from unittest import TestCase
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_mimecast.actions import TrackMessages
from komand_mimecast.util.constants import (
    TRACKED_EMAILS_ADVANCED_CAUSE,
    TRACKED_EMAILS_REQUIRED_CAUSE,
    TRACKED_EMAILS_ASSISTANCE,
)
from parameterized import parameterized

from unit_test.util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestTrackMessages(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(TrackMessages())

    def test_track_messages(self, mocked_request: MagicMock):
        actual = self.action.run(Util.load_json("inputs/search_message_tracking.json.exp"))
        expect = Util.load_json("expected/search_message_tracking.json.exp")
        self.assertEqual(expect, actual)

    @parameterized.expand(
        [
            (
                "inputs/search_message_tracking_bad_1.json.exp",
                TRACKED_EMAILS_REQUIRED_CAUSE,
                TRACKED_EMAILS_ASSISTANCE,
            ),
            (
                "inputs/search_message_tracking_bad_2.json.exp",
                TRACKED_EMAILS_ADVANCED_CAUSE,
                TRACKED_EMAILS_ASSISTANCE,
            ),
        ]
    )
    def test_track_messages_exception(
        self, mocked_request: MagicMock, action_payload: str, exception_cause: str, exception_assistance: str
    ):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json(action_payload))
        self.assertEqual(exception.exception.cause, exception_cause)
        self.assertEqual(exception.exception.assistance, exception_assistance)
