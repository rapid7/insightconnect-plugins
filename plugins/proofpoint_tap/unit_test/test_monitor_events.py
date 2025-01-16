import sys
import os

sys.path.append(os.path.abspath("../"))


from unittest.mock import patch

from komand_proofpoint_tap.tasks import MonitorEvents
from unit_test.test_util import Util
from unittest import TestCase
from parameterized import parameterized
from datetime import datetime, timezone, timedelta
from json import loads
from jsonschema import validate

ENV_VALUE = '{"year": 2024, "month": 1, "day": 27, "hour": 0, "minute": 0, "second": 0}'
ENV_VALUE_2 = '{"year": 2024, "month": 2, "day": 20, "hour": 12, "minute": 0, "second": 0}'
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

    @patch("logging.Logger.info")
    def test_monitor_events_uses_custom_config_data(self, mock_logger, _mock_request, _mock_time):
        # Even though we have an environment variable specified we use the custom_config passed from CPS
        full_lookback_value = loads(ENV_VALUE)
        cps_config = {"lookback": full_lookback_value}  # pass this as a dict as our API will supply as it like this
        response, state, has_more_pages, status_code, _error = self.action.run({}, {}, cps_config)

        # In this example we have an env var specified but this is ignored to use the value in the custom_config
        date = datetime(**full_lookback_value)
        self.assertTrue(
            any(f"Attempting to use custom value of {date}" in call[0][0] for call in mock_logger.call_args_list[0:])
        )

        # state last time should be custom config value + 1 hour
        self.assertEqual("2024-01-27T01:00:00+00:00", state["last_collection_date"])
        self.assertEqual(1, state["next_page_index"])

        # second time we call we will then pass no lookback from SDK level and now use the cutoff date value
        cps_config = {"cutoff": {"date": full_lookback_value}}
        _resp, state_2, _more_pages, _status_code, _error = self.action.run({}, state.copy(), cps_config)

        # Due to pagination the last collection date will not change in our state
        self.assertEqual(state["last_collection_date"], state_2["last_collection_date"])
        self.assertEqual(2, state_2["next_page_index"])  # however we should be on the second page

        # Third time we call - we increase page size to return more_pages=False from the task
        with patch("komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.SPLIT_SIZE", new=40000):
            _resp, state_3, more_pages, _status_code, _error = self.action.run({}, state_2.copy(), cps_config)
            self.assertEqual(state_2["last_collection_date"], state_3["last_collection_date"])
            self.assertEqual(True, more_pages)  # finished 'pages' between time A-B, we haven't caught up to now

        # Fourth time task is called - custom_config is 'normal' and we do normal time calculations / cut off.
        new_now = datetime.strptime("2024-03-25T08:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        with patch(
            "komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.get_current_time", return_value=new_now
        ):
            mock_logger.reset_mock()
            config = {"cutoff": {"hours": 24}}  # config reverted to normal behaviour
            _resp, _state_4, _more_pages, _status_code, _error = self.action.run({}, state_3.copy(), config)
            # get lookback time as task.py does with using now - (lookback + 1 minute latency delay)
            lookback = new_now - timedelta(hours=config["cutoff"]["hours"], minutes=1)
            lookback_msg = "Supplied a start_time further than allowed. Moving this to 2024-03-24 07:59:00+00:00"

            self.assertTrue(any(lookback_msg in call[0][0] for call in mock_logger.call_args_list[0:]))

    @parameterized.expand(
        [
            [
                "enforced_during_backfill_config",
                [{}, {"lookback": {"year": 2023, "month": 3, "day": 4}}],
                ["Supplied a start_time further than allowed. Moving this to 2023-03-28 08:14:00", ""],
            ],
            [
                "enforced_during_lookback_config_date",
                [{}, {"cutoff": {"date": {"year": 2023, "month": 3, "day": 4}}}],
                ["Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 08:14:00", ""],
            ],
            [
                "enforced_during_lookback_config_hours",
                [{}, {"cutoff": {"hours": 24 * 10}}],  # 10 days lookback
                ["Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 08:14:00", ""],
            ],
            [
                "enforced_during_a_state_passed_value",
                # customer has been paused since 29th March, and have an override cutoff hours to 8
                [{"last_collection_date": "2023-03-28T07:00:00.406053+00:00"}, {"cutoff": {"hours": 24 * 8}}],
                [
                    "Supplied a custom_api_limit further than allowed. Moving this to 2023-03-28 08:14:00",
                    "Supplied a start_time further than allowed. Moving this to 2023-03-28 08:14:00",
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
