import json
import logging
import os
import sys
from unittest import TestCase
from unittest.mock import patch

import requests

sys.path.append(os.path.abspath("../"))

from icon_rapid7_surface_command.util.api_connection import ApiConnection
from insightconnect_plugin_runtime.exceptions import PluginException

CSV = "Name,Hostnames\nhost-a,a.example.com\nhost-b,\n"
ROWS = [{"Name": "host-a", "Hostnames": "a.example.com"}, {"Name": "host-b", "Hostnames": None}]
JOB_ID = "0b1c2d3e-4f50-6172-8394-a5b6c7d8e9f0"


def make_response(status, text="", headers=None):
    response = requests.Response()
    response.status_code = status
    response._content = text.encode()
    response.headers.update(headers or {})
    response.url = "https://us.api.insight.rapid7.com/surface/graph-api/objects/table"
    return response


def accepted(job_id=JOB_ID, retry_after="5", location=True):
    headers = {"Retry-After": retry_after, "Preference-Applied": "respond-async"}
    if location:
        headers["Location"] = f"table/jobs/{job_id}"
    return make_response(202, json.dumps({"id": job_id, "status": "RUNNING", "retryAfterSeconds": 5}), headers)


class FakeClock:
    """Replaces time.monotonic/time.sleep so polling loops run instantly and their waits can be checked."""

    def __init__(self):
        self.now = 1000.0
        self.sleeps = []

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.now += seconds


class AsyncQueryTestCase(TestCase):
    def setUp(self):
        self.api = ApiConnection("not_an_api_key", "us", logging.getLogger("test"), timeout=170)
        self.clock = FakeClock()
        patcher_mono = patch("icon_rapid7_surface_command.util.api_connection.time.monotonic", self.clock.monotonic)
        patcher_sleep = patch("icon_rapid7_surface_command.util.api_connection.time.sleep", self.clock.sleep)
        patcher_mono.start()
        patcher_sleep.start()
        self.addCleanup(patcher_mono.stop)
        self.addCleanup(patcher_sleep.stop)

    def send_returns(self, *responses):
        """Stub only the network: real make_request/response_handler run on these responses, in order."""
        patcher = patch.object(requests.Session, "send", side_effect=list(responses))
        mock_send = patcher.start()
        self.addCleanup(patcher.stop)
        return mock_send


class TestStartQueryApi(AsyncQueryTestCase):
    def test_saved_query_returns_job_id(self):
        send = self.send_returns(accepted())

        result = self.api.start_query(query_id="q-1")

        self.assertEqual(result, {"status": "running", "job_id": JOB_ID, "items": []})
        request = send.call_args.args[0]
        self.assertEqual(request.method, "POST")
        self.assertIn("format=csv", request.url)
        self.assertEqual(request.headers["Prefer"], "respond-async, wait=0")
        self.assertEqual(request.headers["X-Api-Key"], "not_an_api_key")
        self.assertEqual(json.loads(request.body), {"query_id": "q-1"})
        self.assertEqual(send.call_args.kwargs["timeout"], 170)

    def test_adhoc_query_sends_cypher(self):
        send = self.send_returns(accepted())

        self.api.start_query(cypher="MATCH (m:Machine) RETURN m")

        self.assertEqual(json.loads(send.call_args.args[0].body), {"cypher": "MATCH (m:Machine) RETURN m"})

    def test_finished_job_returns_rows(self):
        self.send_returns(make_response(200, CSV))

        result = self.api.start_query(query_id="q-1")

        self.assertEqual(result, {"status": "complete", "job_id": "", "items": ROWS})

    def test_job_id_falls_back_to_body(self):
        self.send_returns(accepted(location=False))

        self.assertEqual(self.api.start_query(query_id="q-1")["job_id"], JOB_ID)

    def test_missing_job_id_fails(self):
        self.send_returns(make_response(202, "{}", {"Retry-After": "5"}))

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("did not return a job ID", ctx.exception.cause)

    def test_busy_server_is_retried_after_retry_after(self):
        send = self.send_returns(make_response(503, "busy", {"Retry-After": "7"}), accepted())

        result = self.api.start_query(query_id="q-1")

        self.assertEqual(result["status"], "running")
        self.assertEqual(send.call_count, 2)
        self.assertEqual(self.clock.sleeps, [7])

    def test_busy_server_gives_up_within_timeout(self):
        send = self.send_returns(*[make_response(503, "busy", {"Retry-After": "60"}) for _ in range(5)])

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("busy", ctx.exception.cause)
        self.assertEqual(send.call_count, 4)  # 0, 60, 120, 180 s; another 60 s wait would pass the 230 s action budget
        self.assertEqual(self.clock.sleeps, [60, 60, 60])

    def test_bad_request_is_not_retried(self):
        send = self.send_returns(make_response(400, '{"title":"Bad Request"}'))

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(cypher="NOT CYPHER")
        self.assertIn("Bad Request", ctx.exception.data)
        self.assertEqual(send.call_count, 1)

    def test_read_timeout_points_at_feature_flag(self):
        patcher = patch.object(
            requests.Session, "send", side_effect=requests.exceptions.ReadTimeout("read timeout=170")
        )
        send = patcher.start()
        self.addCleanup(patcher.stop)

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("ASYNC_TABLE_QUERIES", ctx.exception.assistance)
        self.assertEqual(send.call_count, 1)

    def test_connection_error_is_not_reworded(self):
        patcher = patch.object(requests.Session, "send", side_effect=requests.exceptions.ConnectionError("refused"))
        patcher.start()
        self.addCleanup(patcher.stop)

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertNotIn("ASYNC_TABLE_QUERIES", ctx.exception.assistance)


class TestGetQueryResultApi(AsyncQueryTestCase):
    def test_finished_job_returns_rows(self):
        send = self.send_returns(make_response(200, CSV))

        result = self.api.get_query_result(JOB_ID)

        self.assertEqual(result, {"status": "complete", "job_id": JOB_ID, "items": ROWS})
        request = send.call_args.args[0]
        self.assertEqual(request.method, "GET")
        self.assertTrue(request.url.endswith(f"/surface/graph-api/objects/table/jobs/{JOB_ID}"))
        self.assertNotIn("Prefer", request.headers)

    def test_polls_until_complete_honouring_retry_after(self):
        send = self.send_returns(accepted(retry_after="10"), accepted(retry_after="10"), make_response(200, CSV))

        result = self.api.get_query_result(JOB_ID, max_wait=180)

        self.assertEqual(result["status"], "complete")
        self.assertEqual(send.call_count, 3)
        self.assertEqual(self.clock.sleeps, [10, 10])

    def test_still_running_after_max_wait_returns_running(self):
        send = self.send_returns(*[accepted(retry_after="30") for _ in range(20)])

        result = self.api.get_query_result(JOB_ID, max_wait=100)

        self.assertEqual(result, {"status": "running", "job_id": JOB_ID, "items": []})
        self.assertLessEqual(sum(self.clock.sleeps), 100)
        self.assertEqual(self.clock.sleeps, [30, 30, 30, 10])
        self.assertEqual(send.call_count, 5)

    def test_zero_max_wait_checks_once(self):
        send = self.send_returns(accepted())

        result = self.api.get_query_result(JOB_ID, max_wait=0)

        self.assertEqual(result["status"], "running")
        self.assertEqual(send.call_count, 1)
        self.assertEqual(self.clock.sleeps, [])

    def test_expired_job_fails(self):
        send = self.send_returns(make_response(404, '{"detail":"The query job does not exist or has expired."}'))

        with self.assertRaises(PluginException) as ctx:
            self.api.get_query_result(JOB_ID)
        self.assertIn("not found or has expired", ctx.exception.cause)
        self.assertIn("1 hour", ctx.exception.assistance)
        self.assertEqual(send.call_count, 1)

    def test_cancelled_job_fails(self):
        self.send_returns(make_response(410, '{"detail":"cancelled"}'))

        with self.assertRaises(PluginException) as ctx:
            self.api.get_query_result(JOB_ID)
        self.assertIn("cancelled", ctx.exception.cause)

    def test_lost_job_fails_after_retries(self):
        send = self.send_returns(*[make_response(503, '{"detail":"lost"}', {"Retry-After": "5"}) for _ in range(5)])

        with self.assertRaises(PluginException) as ctx:
            self.api.get_query_result(JOB_ID)
        self.assertIn("Start the query again", ctx.exception.assistance)
        self.assertEqual(send.call_count, 3)  # first answer plus 2 retries

    def test_gateway_unavailable_blip_is_retried(self):
        send = self.send_returns(
            make_response(503, "no healthy upstream", {"Retry-After": "2"}), make_response(200, CSV)
        )

        self.assertEqual(self.api.get_query_result(JOB_ID)["status"], "complete")
        self.assertEqual(send.call_count, 2)

    def test_failed_job_surfaces_server_error(self):
        send = self.send_returns(make_response(400, '{"title":"Bad Request","detail":"Your query includes a type"}'))

        with self.assertRaises(PluginException) as ctx:
            self.api.get_query_result(JOB_ID)
        self.assertIn("Your query includes a type", ctx.exception.data)
        self.assertEqual(send.call_count, 1)

    def test_job_id_is_url_encoded(self):
        send = self.send_returns(make_response(200, CSV))

        self.api.get_query_result("a/b c")

        self.assertTrue(send.call_args.args[0].url.endswith("/jobs/a%2Fb%20c"))

    def test_bad_retry_after_uses_default(self):
        self.send_returns(accepted(retry_after="soon"), make_response(200, CSV))

        self.api.get_query_result(JOB_ID)

        self.assertEqual(self.clock.sleeps, [5])


class TestTimeBudget(AsyncQueryTestCase):
    def send_taking(self, seconds, *responses):
        responses = list(responses)
        timeouts = []

        def send(request, **kwargs):
            timeouts.append(kwargs["timeout"])
            self.clock.now += seconds
            return responses.pop(0)

        patcher = patch.object(requests.Session, "send", side_effect=send)
        patcher.start()
        self.addCleanup(patcher.stop)
        return timeouts

    def test_get_stays_within_action_budget_with_slow_requests(self):
        start = self.clock.now
        timeouts = self.send_taking(25, *[accepted(retry_after="30") for _ in range(20)])

        result = self.api.get_query_result(JOB_ID, max_wait=180)

        self.assertEqual(result["status"], "running")
        self.assertLessEqual(self.clock.now - start, 230)
        self.assertTrue(all(t <= 170 for t in timeouts))

    def test_request_timeout_is_capped_by_time_left(self):
        timeouts = self.send_taking(100, accepted(retry_after="1"), accepted(retry_after="1"), make_response(200, CSV))

        self.api.get_query_result(JOB_ID, max_wait=200)

        self.assertEqual(timeouts[0], 170)
        self.assertLessEqual(timeouts[1], 230 - 101)

    def test_max_wait_above_limit_is_capped(self):
        start = self.clock.now
        self.send_returns(*[accepted(retry_after="30") for _ in range(20)])

        self.assertEqual(self.api.get_query_result(JOB_ID, max_wait=1000)["status"], "running")
        self.assertLessEqual(self.clock.now - start, 200)

    def test_start_stays_within_action_budget(self):
        start = self.clock.now
        self.send_taking(60, *[make_response(503, "busy", {"Retry-After": "30"}) for _ in range(10)])

        with self.assertRaises(PluginException):
            self.api.start_query(query_id="q-1")
        self.assertLessEqual(self.clock.now - start, 230 + 60)  # the last request may start just before the budget ends
        self.assertLessEqual(len(self.clock.sleeps), 3)


class TestRetryAndErrorHandling(AsyncQueryTestCase):
    def test_none_timeout_uses_default(self):
        api = ApiConnection("not_an_api_key", "us", logging.getLogger("test"), timeout=None)
        send = self.send_returns(accepted())

        self.assertEqual(api.start_query(query_id="q-1")["status"], "running")
        self.assertEqual(send.call_args.kwargs["timeout"], 170)

    def test_get_retries_temporary_gateway_errors(self):
        for status in (429, 502, 504):
            with self.subTest(status=status):
                send = self.send_returns(
                    make_response(status, f"gateway {status}", {"Retry-After": "3"}), make_response(200, CSV)
                )
                self.assertEqual(self.api.get_query_result(JOB_ID)["status"], "complete")
                self.assertEqual(send.call_count, 2)

    def test_persistent_gateway_error_keeps_status_and_body(self):
        self.send_returns(*[make_response(502, "bad gateway from proxy", {"Retry-After": "60"}) for _ in range(10)])

        with self.assertRaises(PluginException) as ctx:
            self.api.get_query_result(JOB_ID, max_wait=100)
        self.assertIn("HTTP 502", ctx.exception.cause)
        self.assertIn("bad gateway from proxy", ctx.exception.data)

    def test_start_gateway_timeout_points_at_feature_flag(self):
        self.send_returns(*[make_response(504, "upstream timeout", {"Retry-After": "120"}) for _ in range(5)])

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("ASYNC_TABLE_QUERIES", ctx.exception.assistance)

    def test_start_retries_rate_limit(self):
        send = self.send_returns(make_response(429, "slow down", {"Retry-After": "2"}), accepted())

        self.assertEqual(self.api.start_query(query_id="q-1")["status"], "running")
        self.assertEqual(send.call_count, 2)

    def test_get_read_timeout_reports_running(self):
        patcher = patch.object(requests.Session, "send", side_effect=requests.exceptions.ReadTimeout("read timeout"))
        patcher.start()
        self.addCleanup(patcher.stop)

        self.assertEqual(self.api.get_query_result(JOB_ID)["status"], "running")

    def test_job_id_body_that_is_not_an_object(self):
        self.send_returns(make_response(202, "[]", {"Retry-After": "5"}))

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("did not return a job ID", ctx.exception.cause)


class TestRetrySafety(AsyncQueryTestCase):
    def test_lost_job_fails_even_with_short_max_wait(self):
        for max_wait in (0, 20):
            with self.subTest(max_wait=max_wait):
                send = self.send_returns(
                    *[make_response(503, '{"detail":"lost"}', {"Retry-After": "30"}) for _ in range(5)]
                )
                with self.assertRaises(PluginException) as ctx:
                    self.api.get_query_result(JOB_ID, max_wait=max_wait)
                self.assertIn("unavailable", ctx.exception.cause)
                self.assertEqual(send.call_count, 3)

    def test_start_does_not_resend_after_bad_gateway(self):
        send = self.send_returns(make_response(502, "bad gateway", {"Retry-After": "1"}), accepted())

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("HTTP 502", ctx.exception.cause)
        self.assertIn("bad gateway", ctx.exception.data)
        self.assertEqual(send.call_count, 1)

    def test_start_does_not_resend_after_gateway_timeout(self):
        send = self.send_returns(make_response(504, "upstream timeout"), accepted())

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("ASYNC_TABLE_QUERIES", ctx.exception.assistance)
        self.assertEqual(send.call_count, 1)

    def test_timeout_after_busy_retry_is_not_blamed_on_flag(self):
        responses = [make_response(503, "busy", {"Retry-After": "5"}), requests.exceptions.ReadTimeout("read timeout")]
        patcher = patch.object(requests.Session, "send", side_effect=responses)
        patcher.start()
        self.addCleanup(patcher.stop)

        with self.assertRaises(PluginException) as ctx:
            self.api.start_query(query_id="q-1")
        self.assertIn("busy", ctx.exception.cause)
        self.assertNotIn("ASYNC_TABLE_QUERIES", ctx.exception.assistance)


class TestUnavailableRetries(AsyncQueryTestCase):
    def test_separate_blips_between_running_answers_do_not_fail_the_job(self):
        blip = lambda: make_response(503, "no healthy upstream", {"Retry-After": "2"})
        responses = [
            blip(),
            accepted(retry_after="2"),
            blip(),
            accepted(retry_after="2"),
            blip(),
            accepted(retry_after="2"),
            make_response(200, CSV),
        ]
        send = self.send_returns(*responses)

        self.assertEqual(self.api.get_query_result(JOB_ID)["status"], "complete")
        self.assertEqual(send.call_count, 7)
