import sys
import os

from unittest.mock import patch

from komand_proofpoint_tap.tasks import MonitorEvents
from test_util import Util
from unittest import TestCase
from parameterized import parameterized
from datetime import datetime, timezone

sys.path.append(os.path.abspath("../"))

ENV_VALUE = '{"year": 2024, "month": 1, "day": 27, "hour": 0, "minute": 0, "second": 0}'
TEST_PAGE_SIZE = 2


@patch(
    "komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.get_current_time",
    return_value=datetime.strptime("2023-04-04T08:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc),
)
@patch("komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.SPLIT_SIZE", new=TEST_PAGE_SIZE)
@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMonitorEvents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorEvents())

    @parameterized.expand(
        [
            [
                "first_run",
                Util.read_file_to_dict("inputs/monitor_events_first_run.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_first_run.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_events_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_next_page.json.exp"),
            ],
            [
                "last_page",
                Util.read_file_to_dict("inputs/monitor_events_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_next_page.json.exp"),
            ],
            [
                "subsequent_run",
                Util.read_file_to_dict("inputs/monitor_events_subsequent_run.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_subsequent_run.json.exp"),
            ],
            [
                "duplicated_event",
                Util.read_file_to_dict("inputs/monitor_events_duplicated_event.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_duplicated_event.json.exp"),
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_events_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_bad_request.json.exp"),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_events_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_server_error.json.exp"),
            ],
        ]
    )
    def test_monitor_events(self, _mock_request, _mock_get_time, _test_name, current_state, expected):
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("events"))
        self.assertEqual(actual_state, expected.get("state"))

    @patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=ENV_VALUE)
    @patch("logging.Logger.info")
    def test_monitor_events_with_env_variable_empty_state(self, mock_logger, _mock_request, _mock_time):
        # When we inject the env variable into the pod we should change the time we retrieve events from.
        response, state, has_more_pages, status_code, _error = self.action.run(state={})

        # we should have logged using env var
        self.assertIn("Using env var value", mock_logger.call_args_list[1][0][0])

        # state last time should be injected env var + 1 hour
        self.assertEqual("2024-01-27T01:00:00+00:00", state["last_collection_date"])

        # Split the logs being returned by the SPLIT_SIZE variable
        self.assertEqual(TEST_PAGE_SIZE, len(response))

        # We should expect next_page = True because we cut the results and NEXT_PAGE to be set
        self.assertTrue(has_more_pages)
        self.assertEqual(1, state["next_page_index"])

    @patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=ENV_VALUE)
    @patch("logging.Logger.info")
    def test_monitor_events_with_env_variable_existing_state(self, mock_logger, _mock_request, _mock_time):
        # Although we inject the env var because we have a state saved we can ignore and continue our usual logic
        # use this date to avoid cut off logic from mocked current time.
        existing_state = {"last_collection_date": "2023-04-04T01:00:00+00:00"}
        response, state, has_more_pages, status_code, _error = self.action.run(state=existing_state)

        # state last time should be last_collected_date + 1 hour
        self.assertEqual("2023-04-04T02:00:00+00:00", state["last_collection_date"])

        # Split the logs being returned by the SPLIT_SIZE variable
        self.assertEqual(TEST_PAGE_SIZE, len(response))
