import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

import feedparser
import timeout_decorator
from jsonschema import validate
from komand_rss.triggers.poll import Poll
from komand_rss.triggers.poll.schema import Input

from mock import MockSender
from util import Util

DEFAULT_TIMEOUT = 2
STUB_INPUT_PARAMETERS = {Input.FREQUENCY: 1}
TriggerOutput = MockSender()


class TestPoll(TestCase):
    def setUp(self) -> None:
        self.trigger = Util.default_connector(Poll())
        self.expected = Util.load_file("poll", is_feed=False)
        self.feedparser_mock_side_effect = 2 * [Util.load_file("poll")] + [Util.load_file("poll_2")]

    @timeout_decorator.timeout(DEFAULT_TIMEOUT)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=TriggerOutput.send)
    def test_poll(self, mock_send: MagicMock) -> None:
        feedparser.http.get = MagicMock(side_effect=self.feedparser_mock_side_effect)
        self.trigger.run(STUB_INPUT_PARAMETERS)
        validate(TriggerOutput.response, self.trigger.output.schema)
        self.assertEqual(TriggerOutput.response, self.expected)
        mock_send.assert_called()
