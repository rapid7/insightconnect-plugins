from datetime import datetime, timezone
from parameterized import parameterized
from requests import ConnectTimeout
from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock
from typing import Dict, Tuple, Any

from icon_carbon_black_cloud.tasks import MonitorAlerts
from icon_carbon_black_cloud.tasks.monitor_alerts.task import (
    RATE_LIMITED,
    LAST_OBSERVATION_JOB,
    LAST_OBSERVATION_TIME,
    LAST_ALERT_TIME,
    OBSERVATION_QUERY_END_TIME,
)
from icon_carbon_black_cloud.util.constants import OBSERVATION_TIME_FIELD
from icon_carbon_black_cloud.util.exceptions import RateLimitException

from util import (
    Util,
    mock_request_200,
    mock_conditions,
    mock_request_429,
    mock_request_400,
    mock_request_404,
)
from responses.task_test_data import (
    task_first_run,
    task_first_run_output,
    task_first_run_output_within_window,
    task_first_run_output_with_offset,
    task_subsequent_output,
    task_rate_limit_getting_observations,
    task_subsequent_output_no_observation_job,
    observations_more_pages,
    observation_job_not_finished,
    task_401_on_second_request,
    task_404_on_third_request,
    observation_job_exceeded,
    observation_job_not_finished_but_parsed,
    task_404_on_second_request,
    no_logs_in_window_back,
    no_logs_in_window,
    observation_job_not_finished_no_observations,
)

import os
import sys

sys.path.append(os.path.abspath("../"))


@patch("icon_carbon_black_cloud.tasks.monitor_alerts.task.ALERT_PAGE_SIZE_DEFAULT", new=2)  # force page size to be 2
@patch(
    "icon_carbon_black_cloud.tasks.monitor_alerts.task.OBSERVATION_PAGE_SIZE_DEFAULT", new=2
)  # force page size to be 2
@patch(
    "icon_carbon_black_cloud.tasks.monitor_alerts.task.MonitorAlerts._get_current_time",
    return_value=datetime(year=2024, month=4, day=25, hour=16, minute=00, tzinfo=timezone.utc),
)
@patch("requests.request", return_value=mock_request_200(file_name="empty_response"))
class TestMonitorAlerts(TestCase):
    def setUp(self) -> None:
        self.task = Util.default_connector(MonitorAlerts())

    @parameterized.expand(
        [
            [
                "first run",
                task_first_run.copy(),
                ("observation_id", "first_alerts", "first_observations_within_window"),
                task_first_run_output_within_window,
                4,  # all data in mocked responses are returned as no hashes to dedupe
            ],
            [
                "first run - has more pages",
                task_first_run.copy(),
                ("observation_id", "alerts_more_pages", "first_observations"),
                task_first_run_output_with_offset,
                4,  # all data in mocked responses are returned as no hashes to dedupe
            ],
            [
                "subsequent run - testing dedupe logic and no alerts",
                task_first_run_output.copy(),
                ("observation_id", "empty_response", "subsequent_observations"),
                task_subsequent_output,
                1,  # no alerts and 1 observation after dedupe
            ],
            [
                "subsequent run - no alerts and no observation job triggered",
                task_first_run_output.copy(),
                ("empty_response", "empty_response", "empty_response"),
                task_subsequent_output_no_observation_job,
                0,  # no alerts and no observation job successfully triggered
            ],
            [
                "subsequent run - observations has more pages",
                task_first_run_output.copy(),
                ("observation_id", "subsequent_alerts", "observations_has_more_pages"),
                observations_more_pages,
                3,  # 1 alert after dedupe and 2 observations after dedupe
            ],
            [
                "subsequent run - observations has more pages as job has not finished",
                task_first_run_output.copy(),
                ("observation_id", "subsequent_alerts", "observation_not_finished"),
                observation_job_not_finished,
                1,  # 1 alert after dedupe and 0 observations as job not finished
            ],
            [
                "subsequent run - observations not finished but job time has exceeded - has more pages",
                observation_job_exceeded.copy(),
                ("first_alerts", "observation_not_finished", "not_used_response"),
                observation_job_not_finished_but_parsed,
                4,  # all 2 alerts and the 2 observations
            ],
            [
                "subsequent run - no logs - has more pages",
                no_logs_in_window.copy(),
                ("empty_response", "empty_response", "empty_response"),
                no_logs_in_window_back.copy(),
                0,
            ],
            [
                "subsequent run - no observations and job time has exceeded - has more pages",
                observation_job_exceeded.copy(),
                ("first_alerts", "empty_response", "empty_response"),
                observation_job_not_finished_no_observations,
                2,  # 2 alerts and the 0 observations
            ],
        ]
    )
    @patch("logging.Logger.info")
    def test_monitor_alert_happy_paths(
        self,
        test: str,
        test_state: Dict[str, str],
        mocked_responses: Tuple[str, str, str],
        state_output: Dict[str, str],
        logs: int,
        mock_logger: MagicMock,
        mock_req: MagicMock,
        _mock_date: MagicMock,
    ):
        mock_req.side_effect = [
            mock_conditions(200, file_name=mocked_responses[0]),
            mock_conditions(200, file_name=mocked_responses[1]),
            mock_conditions(200, file_name=mocked_responses[2]),
        ]
        response, new_state, has_more_pages, _status_code, _exception = self.task.run(state=test_state)

        expected_has_more_pages = "has more pages" in test
        self.maxDiff = None
        self.assertEqual(expected_has_more_pages, has_more_pages)
        self.assertEqual(logs, len(response))
        self.assertDictEqual(state_output, new_state)

        if "job time has exceeded" in test:
            log_msg = mock_logger.call_args_list[8][0][0]  # 8th logger.info is when we log if job time exceeded
            self.assertIn("has exceeded max run time", log_msg)

    def test_too_many_requests_adds_rate_limiting(self, mock_req: MagicMock, _mock_date: MagicMock):
        """
        Test that when CB return a 429 status code we add a value into the state to prevent further requests
        """
        mock_req.return_value = mock_request_429(file_name="empty_response")
        response, new_state, has_more_pages, status_code, exception = self.task.run(state={})

        self.assertEqual(status_code, 200)  # this is a still successful task execution even if we got rate limited
        self.assertEqual(response, [])

        self.assertTrue(RATE_LIMITED in new_state.keys())
        self.assertEqual("2024-04-25T16:05:00.000000Z", new_state[RATE_LIMITED])  # mocked now + 5 minutes
        self.assertFalse(has_more_pages)  # we don't want to trigger instantly again

        self.assertEqual(type(exception), RateLimitException)

    @parameterized.expand(
        [
            ["Still within rate limiting period", {RATE_LIMITED: "2024-04-25T17:05:00.00Z"}, True],
            ["no longer in rate limiting period", {RATE_LIMITED: "2024-04-25T15:55:00.00Z"}, False],
        ]
    )
    @patch("logging.Logger.info")
    def test_rate_limiting_in_state(
        self,
        logger: str,
        cur_state: Dict[str, str],
        still_rate_limited: bool,
        mock_logger: MagicMock,
        _mock_req: MagicMock,
        _mock_date: MagicMock,
    ):
        """
        When the state passed to the task is within a rate limiting period we should not query CB.
        """
        response, new_state, has_more_pages, status_code, _ = self.task.run(params={}, state=cur_state)

        self.assertEqual(status_code, 200)  # this is a still successful task execution even if we don't query.
        self.assertEqual(response, [])

        # if we're no longer rate limited it should be popped from the state dictionary
        rate_limited = RATE_LIMITED in new_state.keys()

        self.assertEqual(still_rate_limited, rate_limited)
        self.assertIn(logger, mock_logger.call_args_list[0][0][0])  # access first logger param
        self.assertFalse(has_more_pages)  # we don't want to trigger until next task execution

    def test_rate_limiting_on_second_request(self, mock_req: MagicMock, _mock_date: MagicMock):
        """
        Test that when CB returns a 429 status on retrieving alerts that we keep the observation job and alert timings
        """
        mock_req.side_effect = [mock_conditions(200, "observation_id"), mock_request_429(file_name="empty_response")]
        existing_state = task_subsequent_output.copy()
        response, new_state, has_more_pages, status_code, _exception = self.task.run(state=existing_state)

        self.assertEqual(status_code, 200)  # this is a still successful task execution even if we got rate limited
        self.assertEqual(response, [])  # didn't get to successfully retrieve any data

        self.assertTrue(RATE_LIMITED in new_state.keys())
        self.assertEqual("2024-04-25T16:05:00.000000Z", new_state[RATE_LIMITED])  # mocked now + 5 minutes
        self.assertEqual("1234-abcd-5678-sqs", new_state[LAST_OBSERVATION_JOB])  # saved job ID
        self.assertFalse(has_more_pages)  # we don't want to trigger instantly again

        # previous state should not have changed as we got rate limited before getting alerts or observations
        for key, value in existing_state.items():
            self.assertEqual(value, new_state[key])

    def test_rate_limiting_on_getting_observation(self, mock_req: MagicMock, _mock_date: MagicMock):
        """
        When receiving 429, and we have partial results we should return the alerts and store job ID for next run.
        """
        mock_req.side_effect = [
            mock_conditions(200, "observation_id"),
            mock_conditions(200, "first_alerts"),
            mock_request_429(file_name="empty_response"),
        ]
        response, new_state, has_more_pages, status_code, _exception = self.task.run()

        self.assertEqual(status_code, 200)  # this is a still successful task execution even if we got rate limited
        self.assertEqual(2, len(response))  # retrieved the two alerts available

        self.assertFalse(has_more_pages)  # we don't want to trigger instantly again
        self.assertDictEqual(task_rate_limit_getting_observations, new_state)

    @parameterized.expand(
        [
            [
                [mock_request_400(file_name="empty_response"), "empty_response", "empty_response"],
                task_first_run_output,  # we fail right away so the state never changes,
                0,  # no observations or alerts returned
                400,
            ],
            [
                [mock_conditions(200, "observation_id"), mock_conditions(401, "empty"), "empty_response"],
                task_401_on_second_request,
                0,  # observation job created but not retrieved as got 401 on alerts
                401,
            ],
            [
                [
                    mock_conditions(200, "observation_id"),
                    mock_conditions(200, "subsequent_alerts"),
                    mock_request_404(file_name="empty_response"),
                ],
                task_404_on_third_request,
                1,  # able to retrieve the alerts then dedupe and save the observation ID,
                200,
            ],
            [
                [ConnectTimeout(), "empty_response", "empty_response"],
                task_first_run_output,  # we fail right away so the state never changes,
                0,  # no observations or alerts returned
                500,
            ],
            [
                [
                    mock_conditions(200, "observation_id"),
                    mock_request_404(file_name="empty_response"),
                    mock_conditions(200, "empty_response"),
                ],
                task_404_on_second_request,
                0,  # no observations or alerts returned
                404,
            ],
        ],
    )
    def test_http_exceptions(
        self,
        mock_req: MagicMock,
        _mock_date: MagicMock,
        req_side_effects: Tuple[Any, Any, Any],
        expected_state: Dict[str, str],
        num_logs: int,
        expected_status_code: int,
    ):
        mock_req.side_effect = req_side_effects
        input_state = task_first_run_output.copy()
        response, new_state, has_more_pages, status_code, _exception = self.task.run(
            state=input_state, custom_config={}
        )

        self.assertEqual(expected_status_code, status_code)
        self.assertEqual(num_logs, len(response))
        self.assertEqual(has_more_pages, status_code == 200)

        self.assertDictEqual(expected_state, new_state)

    @parameterized.expand(
        [
            [
                {},  # first run but using forced minutes lookback of 10 minutes and 20 minutes
                {LAST_OBSERVATION_TIME: {"minutes": 10}, LAST_ALERT_TIME: {"minutes": 20}},
                {LAST_OBSERVATION_TIME: "2024-04-25T15:35:00.000000Z", LAST_ALERT_TIME: "2024-04-25T15:25:00.000000Z"},
            ],
            [
                {},  # first run but using forced to a direct time
                {
                    LAST_OBSERVATION_TIME: {
                        "date": {"year": 2024, "month": 4, "day": 1, "hour": 14, "minute": 9, "second": 30}
                    },
                    LAST_ALERT_TIME: {
                        "date": {"year": 2024, "month": 4, "day": 3, "hour": 12, "minute": 15, "second": 35}
                    },
                },
                {LAST_OBSERVATION_TIME: "2024-04-01T14:09:30.000000Z", LAST_ALERT_TIME: "2024-04-03T12:15:35.000000Z"},
            ],
            [
                # now = 2024-04-25T16:00:00.000000Z but task - 15 minutes -> 2024-04-25T15:45:00.000000Z
                # subsequent run with the observation time out of the lookback period - default 7 days
                {LAST_OBSERVATION_TIME: "2024-04-15T20:45:30.123Z", LAST_ALERT_TIME: "2024-04-25T15:15:35.123Z"},
                {},  # no special custom config being passed
                {LAST_OBSERVATION_TIME: "2024-04-18T16:45:00.000000Z", LAST_ALERT_TIME: "2024-04-25T15:15:35.123Z"},
            ],
            [
                # now = 2024-04-25T16:00:00.000000Z but task - 15 minutes -> 2024-04-25T15:45:00.000000Z
                # subsequent run with the both times out of limit of overridden 3 days and 6 days
                {LAST_OBSERVATION_TIME: "2024-04-15T20:45:30.123Z", LAST_ALERT_TIME: "2024-04-16T16:15:35.123Z"},
                {f"{LAST_OBSERVATION_TIME}_days": 3, f"{LAST_ALERT_TIME}_days": 6},
                {LAST_OBSERVATION_TIME: "2024-04-22T16:45:00.000000Z", LAST_ALERT_TIME: "2024-04-19T16:45:00.000000Z"},
            ],
            [
                # now = 2024-04-25T16:00:00.000000Z but task - 15 minutes -> 2024-04-25T15:45:00.000000Z
                # subsequent run with the both times out of limit of overridden to specific dates
                {LAST_OBSERVATION_TIME: "2024-04-15T20:45:30.123Z", LAST_ALERT_TIME: "2024-04-19T15:15:35.123Z"},
                {
                    f"max_{LAST_OBSERVATION_TIME}": {
                        "year": 2024,
                        "month": 4,
                        "day": 25,
                        "hour": 12,
                        "minute": 00,
                        "second": 35,
                    },
                    f"max_{LAST_ALERT_TIME}": {
                        "year": 2024,
                        "month": 4,
                        "day": 20,
                        "hour": 10,
                        "minute": 45,
                        "second": 55,
                    },
                },
                {LAST_OBSERVATION_TIME: "2024-04-25T13:00:35.000000Z", LAST_ALERT_TIME: "2024-04-20T11:45:55.000000Z"},
            ],
            [
                {LAST_OBSERVATION_TIME: "2024-04-25T10:35:00.000000Z", LAST_ALERT_TIME: "2024-04-25T15:25:00.000000Z"},
                {OBSERVATION_QUERY_END_TIME: 1},
                {
                    LAST_OBSERVATION_TIME: "2024-04-25T10:35:00.000000Z",
                    LAST_ALERT_TIME: "2024-04-25T15:25:00.000000Z",
                    OBSERVATION_QUERY_END_TIME: "2024-04-25T11:35:00.000000Z",
                },
            ],
        ],
    )
    def test_custom_config_timings(
        self,
        mock_req: MagicMock,
        _mock_date: MagicMock,
        saved_state: Dict[str, str],
        cps_config: Dict[str, Any],
        exp_dates: Dict[str, str],
    ):
        mock_req.side_effect = [
            mock_conditions(200, "observation_id"),
            mock_conditions(200, "empty_response"),
            mock_conditions(200, "empty_response"),
        ]

        _, _, _, _, _ = self.task.run(state=saved_state, custom_config=cps_config)  # not concerned about output

        # check we called the request with the correct parameters passed from CPS
        requested_observation_time = mock_req.call_args_list[0].kwargs.get("json").get("time_range").get("start")
        requested_alert_time = mock_req.call_args_list[1].kwargs.get("json").get("time_range").get("start")
        requested_end_time = mock_req.call_args_list[1].kwargs.get("json").get("time_range").get("end")

        self.assertEqual(exp_dates[LAST_OBSERVATION_TIME], requested_observation_time)
        self.assertEqual(exp_dates[LAST_ALERT_TIME], requested_alert_time)

        if exp_dates.get(OBSERVATION_TIME_FIELD):
            self.assertEqual(exp_dates[OBSERVATION_QUERY_END_TIME], requested_end_time)

    @parameterized.expand(
        [
            [
                {},  # first run but using forced minutes lookback of 10 minutes and 20 minutes
                {LAST_OBSERVATION_TIME: {"minutes": 10}, LAST_ALERT_TIME: {"minutes": 20}},
                {
                    LAST_OBSERVATION_TIME: "2024-04-25T15:35:00.000000Z",
                    LAST_ALERT_TIME: "2024-04-25T15:25:00.000000Z",
                    "alert_page_size": 2,
                    "observation_page_size": 2,
                },
            ],
            [
                # now = 2024-04-25T16:00:00.000000Z but task - 15 minutes -> 2024-04-25T15:45:00.000000Z
                # subsequent run with the both times out of limit of overridden to specific dates
                {LAST_OBSERVATION_TIME: "2024-04-15T20:45:30.123Z", LAST_ALERT_TIME: "2024-04-19T15:15:35.123Z"},
                {
                    f"max_{LAST_OBSERVATION_TIME}": {
                        "year": 2024,
                        "month": 4,
                        "day": 25,
                        "hour": 12,
                        "minute": 00,
                        "second": 35,
                    },
                    f"max_{LAST_ALERT_TIME}": {
                        "year": 2024,
                        "month": 4,
                        "day": 20,
                        "hour": 10,
                        "minute": 45,
                        "second": 55,
                    },
                    "alert_page_size": 7000,
                    "observation_page_size": 7000,
                    "debug": True,
                },
                {
                    LAST_OBSERVATION_TIME: "2024-04-25T13:00:35.000000Z",
                    LAST_ALERT_TIME: "2024-04-20T11:45:55.000000Z",
                    "alert_page_size": 7000,
                    "observation_page_size": 7000,
                    "debug": True,
                },
            ],
        ],
    )
    @patch("logging.Logger.info")
    def test_custom_config_flags(
        self,
        saved_state: Dict[str, str],
        cps_config: Dict[str, Any],
        exp_values: Dict[str, str],
        mock_logger: Mock,
        mock_req: MagicMock,
        _mock_date: MagicMock,
    ):
        mock_req.side_effect = [
            mock_conditions(200, file_name) for file_name in ["observation_id"] + (["empty_response"] * 2)
        ]

        _, _, _, _, _ = self.task.run(state=saved_state, custom_config=cps_config)  # not concerned about output

        # check we called the request with the correct parameters passed from CPS
        requested_observation_time = mock_req.call_args_list[0].kwargs.get("json").get("time_range").get("start")
        requested_observation_rows = mock_req.call_args_list[0].kwargs.get("json").get("rows")

        requested_alert_time = mock_req.call_args_list[1].kwargs.get("json").get("time_range").get("start")
        requested_alert_rows = mock_req.call_args_list[1].kwargs.get("json").get("rows")

        trigger_observation_search_rows = mock_req.call_args_list[2].kwargs.get("url").split("=")[1]

        self.assertEqual(exp_values[LAST_OBSERVATION_TIME], requested_observation_time)
        self.assertEqual(exp_values[LAST_ALERT_TIME], requested_alert_time)

        self.assertEqual(exp_values["observation_page_size"], requested_observation_rows)
        self.assertEqual(str(exp_values["alert_page_size"]), requested_alert_rows)  # converted to string in the payload
        self.assertEqual(
            str(exp_values["observation_page_size"]), trigger_observation_search_rows
        )  # formatted to string in the url

        if cps_config.get("debug", None):
            # check that we have logged request times for each call if debug is enabled
            self.assertIn("Time elapsed for request", mock_logger.call_args_list[5][0][0])
            self.assertIn("Time elapsed for request", mock_logger.call_args_list[8][0][0])
            self.assertIn("Time elapsed for request", mock_logger.call_args_list[12][0][0])
