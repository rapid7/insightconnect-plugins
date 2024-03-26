import sys
import os

from unittest.mock import patch

from komand_proofpoint_tap.tasks import MonitorEvents
from test_util import Util
from unittest import TestCase
from parameterized import parameterized
from datetime import datetime, timezone, timedelta
from json import loads

sys.path.append(os.path.abspath("../"))

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
        self.assertEqual(actual, expected.get("events"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, expected.get("has_more_pages"))

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
        self.assertEqual(actual, expected.get("events"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, True)  # this is different to enforce another call to the third party API

        # add in extra failsafe that the `.exp' file has not changed this has_more_pages to True
        self.assertNotEquals(has_more_pages, expected.get("has_more_pages"))

    @patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=ENV_VALUE)
    @patch("logging.Logger.info")
    def test_monitor_events_with_env_variable_empty_state(self, mock_logger, _mock_request, _mock_time):
        # When we inject the env variable into the pod we should change the time we retrieve events from.
        response, state, has_more_pages, status_code, _error = self.action.run(state={}, custom_config={})

        # we should have logged using env var
        self.assertIn("Using custom value of", mock_logger.call_args_list[2][0][0])

        # state last time should be injected env var + 1 hour
        self.assertEqual("2024-01-27T01:00:00+00:00", state["last_collection_date"])

        # Split the logs being returned by the SPLIT_SIZE variable
        self.assertEqual(TEST_PAGE_SIZE, len(response))

        # We should expect next_page = True because we cut the results and NEXT_PAGE to be set
        self.assertTrue(has_more_pages)
        self.assertEqual(1, state["next_page_index"])

    @patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=ENV_VALUE)
    def test_monitor_events_with_env_variable_existing_state(self, _mock_request, _mock_time):
        # Although we inject the env var because we have a state saved we can ignore and continue our usual logic
        # use this date to avoid cut off logic from mocked current time.
        existing_state = {"last_collection_date": "2023-04-04T01:00:00+00:00"}
        response, state, has_more_pages, status_code, _error = self.action.run(state=existing_state, custom_config={})

        # state last time should be last_collected_date + 1 hour
        self.assertEqual("2023-04-04T02:00:00+00:00", state["last_collection_date"])

        # Split the logs being returned by the SPLIT_SIZE variable
        self.assertEqual(TEST_PAGE_SIZE, len(response))

    @patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=ENV_VALUE_2)
    @patch("logging.Logger.info")
    def test_monitor_events_uses_custom_config_data(self, mock_logger, _mock_request, _mock_time):
        # Even though we have an environment variable specified we use the custom_config passed from CPS
        full_lookback_value = loads(ENV_VALUE)
        cps_config = {"lookback": full_lookback_value}  # pass this as a dict as our API will supply as it like this
        response, state, has_more_pages, status_code, _error = self.action.run({}, {}, cps_config)

        # In this example we have an env var specified but this is ignored to use the value in the custom_config
        self.assertIn(f"Using custom value of {full_lookback_value}", mock_logger.call_args_list[2][0][0])

        # state last time should be custom config value + 1 hour
        self.assertEqual("2024-01-27T01:00:00+00:00", state["last_collection_date"])
        self.assertEqual(1, state["next_page_index"])

        # second time we call we will then pass no lookback from SDK level and now use the cutoff date value
        with patch("komand_proofpoint_tap.tasks.monitor_events.task.SPECIFIC_DATE", new=""):  # clear env var
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
                lookback_msg = f"Last collection date reset to max lookback allowed: {lookback.isoformat()}"
                self.assertEquals(lookback_msg, mock_logger.call_args_list[2][0][0])
