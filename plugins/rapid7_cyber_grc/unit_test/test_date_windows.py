"""Covers the due date and renewal window inputs on Get Tasks and Get Contracts.

Both fields are plain scalar dates, so the window is pushed into $filter rather than
applied after the records are read. What matters is that the right bounds end up in the
expression and that they compose with a filter the caller wrote.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

import re
from datetime import datetime, timedelta, timezone
from unittest import TestCase
from unittest.mock import patch

from icon_rapid7_cyber_grc.actions import GetContracts, GetTasks
from util import Util

# The literal the plugin writes, e.g. 2026-09-10T15:12:03.833Z.
LITERAL = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"


def days_from_now(literal: str) -> float:
    parsed = datetime.fromisoformat(literal.replace("Z", "+00:00"))
    return (parsed - datetime.now(timezone.utc)) / timedelta(days=1)


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestDateWindows(TestCase):
    def setUp(self):
        Util.calls = []

    @staticmethod
    def filter_sent():
        return Util.calls[0]["params"].get("$filter")

    def run_tasks(self, **params):
        Util.default_connector(GetTasks()).run({"top": 0, **params})
        return self.filter_sent()

    def run_contracts(self, **params):
        Util.default_connector(GetContracts()).run({"top": 0, **params})
        return self.filter_sent()

    def test_no_window_sends_no_filter(self, mock_request):
        self.assertIsNone(self.run_tasks(due_within_days=0, overdue_only=False))

    def test_due_within_days_bounds_the_due_date(self, mock_request):
        sent = self.run_tasks(due_within_days=7)

        match = re.fullmatch(rf"dueDate ne null and dueDate le ({LITERAL})", sent)
        self.assertIsNotNone(sent and match, sent)
        self.assertAlmostEqual(days_from_now(match.group(1)), 7, places=2)

    def test_a_negative_window_is_read_as_a_length(self, mock_request):
        match = re.search(rf"le ({LITERAL})", self.run_tasks(due_within_days=-7))

        self.assertAlmostEqual(days_from_now(match.group(1)), 7, places=2)

    def test_overdue_only_bounds_the_due_date_at_now(self, mock_request):
        sent = self.run_tasks(overdue_only=True)

        match = re.fullmatch(rf"dueDate ne null and dueDate lt ({LITERAL})", sent)
        self.assertIsNotNone(sent and match, sent)
        self.assertAlmostEqual(days_from_now(match.group(1)), 0, places=2)

    def test_both_options_leave_the_tighter_bound_in_force(self, mock_request):
        sent = self.run_tasks(due_within_days=7, overdue_only=True)

        # Two clauses, so each is parenthesised, and the lt now clause is the tighter.
        self.assertIn("dueDate lt", sent)
        self.assertIn("dueDate le", sent)
        self.assertTrue(sent.startswith("("), sent)

    def test_the_window_is_combined_with_the_callers_filter(self, mock_request):
        sent = self.run_tasks(filter="name eq 'a' or name eq 'b'", due_within_days=7)

        # The caller's or is parenthesised so it cannot bind looser than the and and
        # widen the result.
        self.assertTrue(sent.startswith("(name eq 'a' or name eq 'b') and ("), sent)

    def test_the_window_is_combined_with_the_status(self, mock_request):
        sent = self.run_tasks(status_id=3, due_within_days=7)

        self.assertTrue(sent.startswith("(statusID eq 3) and (dueDate ne null and dueDate le "), sent)

    def test_a_renewal_window_bounds_the_end_date_at_both_ends(self, mock_request):
        sent = self.run_contracts(renewing_within_days=90, include_expired=False)

        upper = re.search(rf"endDate le ({LITERAL})", sent)
        lower = re.search(rf"endDate ge ({LITERAL})", sent)
        self.assertAlmostEqual(days_from_now(upper.group(1)), 90, places=2)
        self.assertAlmostEqual(days_from_now(lower.group(1)), 0, places=2)

    def test_including_expired_contracts_drops_the_lower_bound(self, mock_request):
        sent = self.run_contracts(renewing_within_days=90, include_expired=True)

        self.assertEqual(sent, sent.replace("endDate ge", ""))
        self.assertIn("endDate le", sent)

    def test_no_renewal_window_leaves_the_filter_alone(self, mock_request):
        sent = self.run_contracts(filter="statusID eq 3", renewing_within_days=0, include_expired=False)

        self.assertEqual(sent, "statusID eq 3")

    def test_including_expired_does_nothing_without_a_window(self, mock_request):
        self.assertIsNone(self.run_contracts(renewing_within_days=0, include_expired=True))
