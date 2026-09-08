"""Covers the Add Comment action.

A comment is not a sub-resource of the record it belongs to: it is a row in one
tenant-wide Discussions collection, tied back by the record's own Discussion Field ID.
The action reads that ID off the record so a workflow does not have to know it.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

import json
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_rapid7_cyber_grc.actions import AddComment
from util import BASE_URL, MockResponse, Util

# The comment thread Cyber GRC has created on the record under test.
FIELD_ID = 77


def serve(field_id=FIELD_ID):
    """A request mock for a record carrying the given Discussion Field ID."""

    def handler(method, url, **kwargs):
        Util.calls.append({"method": method, "url": url, **kwargs})
        if method == "POST":
            return MockResponse(201, {"id": 900, **(kwargs.get("json") or {})})
        record = {"id": 4} if field_id is None else {"id": 4, "discussionFieldID": field_id}
        return MockResponse(200, record)

    return handler


class TestAddComment(TestCase):
    def setUp(self):
        Util.calls = []

    def run_action(self, field_id=FIELD_ID, **params):
        action = Util.default_connector(AddComment())
        with patch("requests.Session.request", side_effect=serve(field_id)):
            return action.run({"record_type": "Tasks", "id": 4, "comment": "Closed upstream", "user_id": 5, **params})

    @staticmethod
    def posted():
        return next(call["json"] for call in Util.calls if call["method"] == "POST")

    def test_the_comment_is_posted_to_the_discussions_collection(self):
        actual = self.run_action()

        self.assertEqual(Util.calls[-1]["url"], f"{BASE_URL}/api/v2/Discussions")
        self.assertEqual(actual["comment"]["id"], 900)

    def test_the_thread_is_read_off_the_record_being_commented_on(self):
        self.run_action()

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Tasks/4")
        self.assertEqual(Util.calls[0]["params"], {"$select": "discussionFieldID"})
        self.assertEqual(self.posted()["discussionFieldID"], FIELD_ID)

    def test_the_form_discussion_id_defaults_to_the_record_id(self):
        self.run_action()

        self.assertEqual(self.posted()["formDiscussionID"], 4)

    def test_the_author_is_always_named(self):
        # Cyber GRC rejects a comment that does not name an author with "UserID must be
        # greater than 0", so the author is a required input rather than an optional one.
        self.run_action()

        self.assertEqual(self.posted()["userID"], 5)

    def test_the_author_is_the_user_the_step_names(self):
        self.run_action(user_id=42)

        self.assertEqual(self.posted()["userID"], 42)

    def test_a_given_thread_id_skips_reading_the_record(self):
        self.run_action(discussion_field_id=12)

        self.assertEqual([call["method"] for call in Util.calls], ["POST"])
        self.assertEqual(self.posted()["discussionFieldID"], 12)

    def test_a_given_form_discussion_id_overrides_the_record_id(self):
        self.run_action(form_discussion_id=31)

        self.assertEqual(self.posted()["formDiscussionID"], 31)

    def test_another_record_type_is_commented_on_the_same_way(self):
        self.run_action(record_type="Risks", id=9)

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/Risks/9")
        self.assertEqual(self.posted()["formDiscussionID"], 9)

    def test_a_record_with_no_thread_is_reported_rather_than_guessed_at(self):
        with self.assertRaises(PluginException) as raised:
            self.run_action(field_id=None)

        self.assertIn("Tasks record 4 has no comment thread", raised.exception.cause)
        self.assertEqual([call["method"] for call in Util.calls], ["GET"])
