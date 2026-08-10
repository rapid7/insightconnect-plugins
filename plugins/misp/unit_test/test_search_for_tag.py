import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.triggers.search_for_tag.trigger import SearchForTag
from komand_misp.triggers.search_for_tag.schema import SearchForTagInput, SearchForTagOutput
from jsonschema import validate


class StopLoop(Exception):
    """Raised from a mocked time.sleep to break the trigger's `while True` loop after one iteration."""


class TestSearchForTag(unittest.TestCase):
    def setUp(self):
        self.trigger = SearchForTag()
        self.trigger.connection = MagicMock()
        self.trigger.logger = MagicMock()
        self.trigger.send = MagicMock()
        self.mock_client = MagicMock()
        self.trigger.connection.client = self.mock_client

        self.params = {
            "interval": 5,
            "tag": "test-tag",
            "remove": False,
        }

    @patch("time.sleep", side_effect=StopLoop)
    def test_search_for_tag_calls_search_index_with_tags(self, _mock_sleep: MagicMock) -> None:
        # search_index returns a bare list of event dicts (no "response" wrapper),
        # matching PyMISP 2.4.194 and the working search_events action.
        self.mock_client.search_index.return_value = [{"id": "1"}, {"id": "2"}]

        validate(self.params, SearchForTagInput.schema)
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Regression guard for SI-35006: the trigger must use `tags=` (plural),
        # not `tag=`, otherwise PyMISP raises TypeError.
        self.mock_client.search_index.assert_called_once_with(tags="test-tag")

        output = {"events": ["1", "2"]}
        self.trigger.send.assert_called_once_with(output)
        validate(output, SearchForTagOutput.schema)

    @patch("time.sleep", side_effect=StopLoop)
    def test_search_for_tag_no_events_does_not_send(self, _mock_sleep: MagicMock) -> None:
        self.mock_client.search_index.return_value = []

        validate(self.params, SearchForTagInput.schema)
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        self.mock_client.search_index.assert_called_once_with(tags="test-tag")
        self.trigger.send.assert_not_called()

    @patch("time.sleep", side_effect=StopLoop)
    def test_search_for_tag_event_missing_id_raises(self, _mock_sleep: MagicMock) -> None:
        # An event without an "id" key must surface as a KeyError, not be silently
        # dropped, so the failure is visible in the trigger logs.
        self.mock_client.search_index.return_value = [{"uuid": "no-id-here"}]

        validate(self.params, SearchForTagInput.schema)
        with self.assertRaises(KeyError):
            self.trigger.run(self.params)

        self.mock_client.search_index.assert_called_once_with(tags="test-tag")
        self.trigger.logger.error.assert_called_once()
        self.trigger.send.assert_not_called()


if __name__ == "__main__":
    unittest.main()
