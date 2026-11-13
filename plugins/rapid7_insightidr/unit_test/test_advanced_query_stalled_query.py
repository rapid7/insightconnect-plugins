import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Optional
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.actions.advanced_query_on_log import AdvancedQueryOnLog
from komand_rapid7_insightidr.actions.advanced_query_on_log.schema import Input as LogInput
from komand_rapid7_insightidr.actions.advanced_query_on_log.schema import Output
from komand_rapid7_insightidr.actions.advanced_query_on_log_set import AdvancedQueryOnLogSet
from komand_rapid7_insightidr.actions.advanced_query_on_log_set.schema import Input as LogSetInput
from parameterized import parameterized

from util import Util

FINISHED = None
STALLED = [10] * 500
EVENT = {"message": '{"user": "example"}', "timestamp": 1700000000000, "labels": []}

LOG = (
    AdvancedQueryOnLog,
    "komand_rapid7_insightidr.actions.advanced_query_on_log.action.send_session_request",
    {LogInput.LOG_ID: "log-id"},
)
LOG_SET = (
    AdvancedQueryOnLogSet,
    "komand_rapid7_insightidr.actions.advanced_query_on_log_set.action.send_session_request",
    {LogSetInput.LOG_SET: "Unparsed Data"},
)


class FakeResponse:
    def __init__(self, body: dict[str, Any]) -> None:
        self.body = body
        self.status_code = 200
        self.text = str(body)

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return self.body


class FakeLogSearch:
    """
    Stands in for send_session_request. The n-th submitted query reports the progress values in attempts[n] on
    successive polls (the last value repeats), and FINISHED returns one event.
    """

    def __init__(self, attempts: list[list[Optional[int]]]) -> None:
        self.attempts = attempts
        self.submits = 0
        self.polls = {}

    def __call__(
        self,
        request_url: str,
        request_headers: dict[str, Any],
        request_id: str,
        request_params: Optional[dict[str, Any]] = None,
    ) -> FakeResponse:
        if request_url.endswith("log_search/management/logsets"):
            return FakeResponse({"logsets": [{"name": "Unparsed Data", "id": "logset-id"}]})
        if "log_search/query/logs/" in request_url or "log_search/query/logsets/" in request_url:
            self.submits += 1
            return FakeResponse({"links": [{"rel": "Self", "href": f"https://callback/{self.submits}"}]})

        query = int(request_url.rsplit("/", 1)[-1])
        progress_values = self.attempts[min(query, len(self.attempts)) - 1]
        poll = self.polls.get(query, 0)
        self.polls[query] = poll + 1
        progress = progress_values[min(poll, len(progress_values) - 1)]
        if progress is FINISHED:
            return FakeResponse({"events": [EVENT], "links": []})
        return FakeResponse({"progress": progress, "links": [{"rel": "Self", "href": request_url}]})


def run_action(action_class: type, target: str, extra_input: dict[str, Any], timeout: int, fake: FakeLogSearch) -> dict:
    action = Util.default_connector(action_class())
    params = {
        LogInput.QUERY: "where(user=example)",
        LogInput.TIMEOUT: timeout,
        LogInput.RELATIVE_TIME: "Last 5 Minutes",
        **extra_input,
    }
    with patch(target, side_effect=fake):
        return action.run(params)


@patch("time.sleep")
class TestAdvancedQueryStalledQuery(TestCase):
    @parameterized.expand(
        [
            ("log_stalled_query_is_resubmitted", *LOG, 120, [STALLED, [FINISHED]], 2, 30),
            ("log_set_stalled_query_is_resubmitted", *LOG_SET, 120, [STALLED, [FINISHED]], 2, 30),
            ("log_progressing_query_is_not_resubmitted", *LOG, 120, [[10] * 20 + [20] * 20 + [FINISHED]], 1, 40),
            (
                "log_set_progressing_query_is_not_resubmitted",
                *LOG_SET,
                120,
                [[10] * 20 + [20] * 20 + [FINISHED]],
                1,
                40,
            ),
        ]
    )
    def test_returns_results(
        self,
        mock_sleep: MagicMock,
        _name: str,
        action_class: type,
        target: str,
        extra_input: dict[str, Any],
        timeout: int,
        attempts: list[list[Optional[int]]],
        expected_submits: int,
        expected_seconds_polled: int,
    ) -> None:
        fake = FakeLogSearch(attempts)
        actual = run_action(action_class, target, extra_input, timeout, fake)
        self.assertEqual(actual.get(Output.COUNT), 1)
        self.assertEqual(fake.submits, expected_submits)
        self.assertEqual(mock_sleep.call_count, expected_seconds_polled)

    @parameterized.expand(
        [
            ("log_every_attempt_stalls", *LOG, 120, [STALLED], 3),
            ("log_set_every_attempt_stalls", *LOG_SET, 120, [STALLED], 3),
            ("log_no_time_left_to_resubmit", *LOG, 30, [STALLED, [FINISHED]], 1),
            ("log_set_no_time_left_to_resubmit", *LOG_SET, 30, [STALLED, [FINISHED]], 1),
        ]
    )
    def test_times_out_within_the_timeout(
        self,
        mock_sleep: MagicMock,
        _name: str,
        action_class: type,
        target: str,
        extra_input: dict[str, Any],
        timeout: int,
        attempts: list[list[Optional[int]]],
        expected_submits: int,
    ) -> None:
        fake = FakeLogSearch(attempts)
        with self.assertRaises(PluginException) as error:
            run_action(action_class, target, extra_input, timeout, fake)
        self.assertEqual(error.exception.cause, "Time out exceeded")
        self.assertEqual(fake.submits, expected_submits)
        self.assertEqual(mock_sleep.call_count, timeout)
