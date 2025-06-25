import sys
import os

sys.path.append(os.path.abspath("../"))


from unittest.mock import patch

from komand_proofpoint_tap.tasks import MonitorEvents
from test_util import Util
from unittest import TestCase
from parameterized import parameterized
from datetime import datetime, timezone
from jsonschema import validate

ENV_VALUE = '{"year": 2024, "month": 1, "day": 27, "hour": 0, "minute": 0, "second": 0}'
ENV_VALUE_2 = '{"year": 2024, "month": 2, "day": 20, "hour": 12, "minute": 0, "second": 0}'
TEST_PAGE_SIZE = 2


@patch(
    "komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.get_current_time",
    return_value=datetime.strptime("2023-04-04T08:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc),
)
@patch("komand_proofpoint_tap.tasks.monitor_events.task.DEFAULT_SPLIT_SIZE", new=TEST_PAGE_SIZE)
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
                Util.read_file_to_dict("inputs/monitor_events_last_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_last_page.json.exp"),
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
        actual, actual_state, has_more_pages, status_code, error = self.action.run(
            state=current_state, custom_config={}
        )
        validate(actual, self.action.output.schema)
        self.assertEqual(expected.get("events"), actual)
        self.assertEqual(expected.get("state"), actual_state)
        self.assertEqual(expected.get("has_more_pages"), has_more_pages)

    @parameterized.expand(
        [
            [
                "sub_30_seconds",
                {"last_collection_date": "2023-04-03T05:59:00+00:00"},
                {"state": {"last_collection_date": "2023-04-03T05:59:00+00:00"}, "has_more_pages": False},
            ],
            [
                "beyond_api_limit",
                {"last_collection_date": "2023-04-03T04:59:00+00:00"},
                {"state": {}, "has_more_pages": False},
            ],
        ]
    )
    def test_monitor_events_handle_api_error(self, _mock_request, _mock_get_time, _test_name, state, expected):
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=state, custom_config={})
        self.assertEqual([], actual)
        self.assertEqual(expected.get("state"), actual_state)
        self.assertEqual(expected.get("has_more_pages"), has_more_pages)

    def test_monitor_events_last_page_not_queried_to_now(self, _mock_request, mock_time):
        """
        Reuse the 'last_page' parameters from the test above but mock the time to be + 1 hour and we should
        change that has_more_pages is now True to continue ingesting events until we have pulled everything from
        the third party API.
        """
        current_state = Util.read_file_to_dict("inputs/monitor_events_last_page.json.inp")
        expected = Util.read_file_to_dict("expected/monitor_events_last_page.json.exp")

        # Move current time forward 1 hour from other tests to test has_more_pages logic.
        mock_time.return_value = datetime.strptime("2023-04-04T09:00:00", "%Y-%m-%dT%H:%M:%S").replace(
            tzinfo=timezone.utc
        )

        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(expected.get("events"), actual)
        self.assertEqual(expected.get("state"), actual_state)
        self.assertEqual(True, has_more_pages)  # this is different to enforce another call to the third party API

        # add in extra failsafe that the `.exp' file has not changed this has_more_pages to True
        self.assertNotEqual(expected.get("has_more_pages"), has_more_pages)

    @parameterized.expand(
        [
            [
                "enforced_during_backfill_config",
                [{}, {"lookback": {"year": 2023, "month": 3, "day": 4}}],
                ["Supplied a start_time further than allowed. Moving this to 2023-03-28 10:14:00", ""],
            ],
            [
                "enforced_during_lookback_config_date",
                [{}, {"cutoff": {"date": {"year": 2023, "month": 3, "day": 4}}}],
                ["Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 09:14:00", ""],
            ],
            [
                "enforced_during_lookback_config_hours",
                [{}, {"cutoff": {"hours": 24 * 10}}],  # 10 days lookback
                ["Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 09:14:00", ""],
            ],
            [
                "enforced_both_lookback_date_and_cutoff_hours_config",
                # customer has been paused since 29th March, and have an override cutoff hours to 8
                [{}, {"lookback": {"year": 2023, "month": 3, "day": 4}, "cutoff": {"hours": 24 * 8}}],
                [
                    "Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 09:14:00",
                    "Supplied a start_time further than allowed. Moving this to 2023-03-28 10:14:00",
                ],
            ],
        ]
    )
    @patch("logging.Logger.info")
    def test_api_max_looback_enforced(
        self, _test_name, task_params, logger_msgs, mock_logger, _mock_request, _mock_time
    ):
        # _mock_time is set to be 2023-04-04T08:00:00; we want to pass a date further back that 7 days in different
        # scenarios and ensure that we don't query the API for Proofpoint as it will error out.
        state, config = task_params
        custom_config_logger, saved_state_logger = logger_msgs

        _resp, _state, _has_more_pages, _status_code, _error = self.action.run({}, state, config)
        self.assertTrue(any(custom_config_logger in call[0][0] for call in mock_logger.call_args_list[0:]))

        self.assertTrue(any(saved_state_logger in call[0][0] for call in mock_logger.call_args_list[0:]))
