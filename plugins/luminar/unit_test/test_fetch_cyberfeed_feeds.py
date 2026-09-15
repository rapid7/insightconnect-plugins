import logging
import os
import sys
import unittest
from unittest import mock

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_luminar.triggers.fetch_cyberfeed_feeds.trigger import FetchCyberfeedFeeds


class TestFetchCyberfeedFeeds(unittest.TestCase):
    def setUp(self) -> None:
        self.trigger = FetchCyberfeedFeeds()
        self.trigger.logger = logging.getLogger("trigger logger")
        self.trigger.connection = mock.Mock()
        self.trigger.connection.client = mock.Mock()

    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.is_valid_date",
        return_value=False,
    )
    def test_invalid_initial_date(self, mock_valid_date):
        # Run with invalid date → should log error and return None
        with self.assertLogs("trigger logger", level="ERROR") as log:
            result = self.trigger.run(
                {"frequency": 1, "initial_fetch_date": "bad-date"}
            )
            self.assertIsNone(result)
            self.assertIn("Invalid initial fetch date", log.output[0])

    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.is_valid_date",
        return_value=True,
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.get_last_run",
        return_value=None,
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.next_checkpoint",
        return_value="2025-09-23T00:00:00Z",
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.pull_feeds",
        return_value=[{"id": "test_feed"}],
    )
    @mock.patch("icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.save_last_run")
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.time.sleep",
        side_effect=Exception("Stop Loop"),
    )
    def test_trigger_happy_path(
        self, mock_sleep, mock_save, mock_pull, mock_next, mock_last, mock_valid
    ):
        # Mock send to capture outputs
        self.trigger.send = mock.Mock()

        with self.assertRaises(PluginException) as context:
            self.trigger.run({"frequency": 1, "initial_fetch_date": "2025-09-20"})

        # Assert our mock data made it through
        self.trigger.send.assert_called_once_with({"results": [{"id": "test_feed"}]})

        # Ensure save_last_run was called
        mock_save.assert_called_once()

        # Check that Stop Loop text is inside the exception cause
        self.assertIn("Stop Loop", context.exception.cause)

    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.is_valid_date",
        return_value=True,
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.get_last_run",
        return_value=None,
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.next_checkpoint",
        return_value="checkpoint",
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.pull_feeds",
        side_effect=RuntimeError("Boom"),
    )
    @mock.patch(
        "icon_luminar.triggers.fetch_cyberfeed_feeds.trigger.time.sleep",
        side_effect=Exception("Stop Loop"),
    )
    def test_trigger_exception(
        self, mock_sleep, mock_pull, mock_next, mock_last, mock_valid
    ):
        with self.assertRaises(PluginException) as context:
            self.trigger.run({"frequency": 1, "initial_fetch_date": "2025-09-20"})

        self.assertIn("Plugin exception occurred", str(context.exception))
