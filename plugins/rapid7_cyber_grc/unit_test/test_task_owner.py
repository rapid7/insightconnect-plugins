"""Covers the Owner and Status ID inputs on Get Tasks.

A task's status is a plain integer field, so it narrows the query at the API. Its
assignee is a nested object with no filterable scalar ID, so the owner is matched by the
plugin after the records are read.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_rapid7_cyber_grc.actions import GetTasks
from util import BASE_URL, Util


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGetTasksOwner(TestCase):
    def setUp(self):
        Util.calls = []

    @staticmethod
    def run_action(params):
        return Util.default_connector(GetTasks()).run(params)

    def test_status_narrows_the_query_at_the_api(self, mock_request):
        self.run_action({"status_id": 3, "top": 0})

        self.assertEqual(Util.calls[0]["params"]["$filter"], "statusID eq 3")

    def test_status_is_combined_with_the_callers_filter(self, mock_request):
        self.run_action({"filter": "name eq 'a' or name eq 'b'", "status_id": 3, "top": 0})

        # Each half is parenthesised so the caller's or cannot widen the result.
        self.assertEqual(Util.calls[0]["params"]["$filter"], "(name eq 'a' or name eq 'b') and (statusID eq 3)")

    def test_no_status_leaves_the_filter_alone(self, mock_request):
        self.run_action({"filter": "statusID eq 3", "status_id": 0, "top": 0})

        self.assertEqual(Util.calls[0]["params"]["$filter"], "statusID eq 3")

    def test_owner_matches_the_assignee_email_regardless_of_case(self, mock_request):
        actual = self.run_action({"owner": "alice@example.com", "top": 0})

        self.assertEqual([item["id"] for item in actual["tasks"]], [1])
        self.assertEqual(actual["count"], 1)

    def test_owner_matches_a_numeric_user_id(self, mock_request):
        actual = self.run_action({"owner": "22", "top": 0})

        self.assertEqual([item["id"] for item in actual["tasks"]], [2])

    def test_an_owner_with_no_tasks_returns_nothing(self, mock_request):
        actual = self.run_action({"owner": "nobody@example.com", "top": 0})

        self.assertEqual(actual["tasks"], [])
        self.assertEqual(actual["count"], 0)

    def test_the_owner_is_not_sent_to_the_api(self, mock_request):
        self.run_action({"owner": "alice@example.com", "top": 0})

        self.assertNotIn("$filter", Util.calls[0]["params"])

    def test_top_and_skip_count_the_owners_tasks(self, mock_request):
        # Both paged tasks belong to the two owners, so skipping one leaves none of
        # Alice's. Applying Top at the API instead would have hidden task 2 from Bob.
        self.assertEqual(self.run_action({"owner": "bob@example.com", "top": 1})["count"], 1)
        self.assertEqual(self.run_action({"owner": "bob@example.com", "top": 0, "skip": 1})["count"], 0)
        # Top and Skip must not reach the API when the owner match needs every record.
        self.assertNotIn("$top", Util.calls[0]["params"])
        self.assertNotIn("$skip", Util.calls[0]["params"])

    def test_select_keeps_the_assignee_so_the_match_can_be_made(self, mock_request):
        self.run_action({"owner": "alice@example.com", "select": "id,name", "top": 0})

        self.assertEqual(Util.calls[0]["params"]["$select"], "id,name,assignedTo")

    def test_select_that_already_asks_for_the_assignee_is_left_alone(self, mock_request):
        self.run_action({"owner": "alice@example.com", "select": "id,assignedTo", "top": 0})

        self.assertEqual(Util.calls[0]["params"]["$select"], "id,assignedTo")

    def test_whitespace_is_not_treated_as_an_owner(self, mock_request):
        actual = self.run_action({"owner": "  ", "top": 0})

        self.assertEqual([item["id"] for item in actual["tasks"]], [1, 2])
