"""Covers the character-limit truncation guard.

Cyber GRC rejects the whole request when a text field is over its limit, which would
fail the step. The client truncates a known over-length field to a safe length and logs
a warning instead, so a workflow mirroring long text from another system is not blocked.
The guard lives in create_record and update_record, so it covers the typed Create/Update
actions, the generic Create/Update Record actions, and Add Comment, which posts to the
Discussions collection.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from icon_rapid7_cyber_grc.actions import AddComment, CreateIncident, CreateRisk, UpdateRisk
from icon_rapid7_cyber_grc.util.api import CHAR_LIMIT_MARGIN, FIELD_CHAR_LIMITS
from util import BASE_URL, MockResponse, Util

COMMENT_LIMIT = FIELD_CHAR_LIMITS["Discussions"]["comment"]  # 5000
RISK_DESC_LIMIT = FIELD_CHAR_LIMITS["Risks"]["description"]  # 2000


def comment_server(method, url, **kwargs):
    """Serve a record carrying a comment thread, and echo any posted body back."""
    Util.calls.append({"method": method, "url": url, **kwargs})
    if method == "POST":
        return MockResponse(201, {"id": 900, **(kwargs.get("json") or {})})
    return MockResponse(200, {"id": 4, "discussionFieldID": 77})


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestRecordCharLimits(TestCase):
    def setUp(self):
        Util.calls = []
        Util.updated = {}

    @staticmethod
    def sent(method):
        return next(call["json"] for call in Util.calls if call["method"] == method)

    def test_an_over_limit_risk_description_is_truncated_on_create(self, mock_request):
        action = Util.default_connector(CreateRisk())
        action.run({"record": {"name": "Big", "description": "x" * (RISK_DESC_LIMIT + 500)}})

        posted = self.sent("POST")
        self.assertEqual(len(posted["description"]), RISK_DESC_LIMIT - CHAR_LIMIT_MARGIN)

    def test_an_over_limit_risk_description_is_truncated_on_update(self, mock_request):
        action = Util.default_connector(UpdateRisk())
        action.run({"id": 4, "record": {"description": "y" * (RISK_DESC_LIMIT + 1)}})

        put = self.sent("PUT")
        self.assertEqual(len(put["description"]), RISK_DESC_LIMIT - CHAR_LIMIT_MARGIN)

    def test_a_description_within_the_limit_is_left_untouched(self, mock_request):
        text = "z" * RISK_DESC_LIMIT
        action = Util.default_connector(CreateRisk())
        action.run({"record": {"name": "Fine", "description": text}})

        self.assertEqual(self.sent("POST")["description"], text)

    def test_other_fields_are_not_truncated(self, mock_request):
        # Only fields named in FIELD_CHAR_LIMITS are guarded; name has no limit here.
        long_name = "n" * (RISK_DESC_LIMIT + 500)
        action = Util.default_connector(CreateRisk())
        action.run({"record": {"name": long_name}})

        self.assertEqual(self.sent("POST")["name"], long_name)

    def test_truncation_is_logged_as_a_warning(self, mock_request):
        action = Util.default_connector(CreateRisk())
        with self.assertLogs(action.connection.logger, level="WARNING") as logged:
            action.run({"record": {"description": "x" * (RISK_DESC_LIMIT + 10)}})

        self.assertTrue(any("truncated" in line.lower() for line in logged.output))

    def test_the_full_original_value_is_logged_so_it_is_not_lost(self, mock_request):
        original = "x" * (RISK_DESC_LIMIT + 250)
        action = Util.default_connector(CreateRisk())
        with self.assertLogs(action.connection.logger, level="INFO") as logged:
            action.run({"record": {"description": original}})

        # The full untruncated value must appear in the log even though the record
        # stored only the truncated form.
        self.assertTrue(any(original in line for line in logged.output))

    def test_secondary_risk_body_fields_are_also_truncated(self, mock_request):
        # businessImpact and possibleOutcome are guarded alongside description.
        action = Util.default_connector(CreateRisk())
        action.run(
            {
                "record": {
                    "businessImpact": "b" * (RISK_DESC_LIMIT + 300),
                    "possibleOutcome": "p" * (RISK_DESC_LIMIT + 300),
                }
            }
        )

        posted = self.sent("POST")
        self.assertEqual(len(posted["businessImpact"]), RISK_DESC_LIMIT - CHAR_LIMIT_MARGIN)
        self.assertEqual(len(posted["possibleOutcome"]), RISK_DESC_LIMIT - CHAR_LIMIT_MARGIN)

    def test_body_fields_on_another_record_type_are_truncated(self, mock_request):
        # An incident carries several narrative fields; each is guarded.
        limit = FIELD_CHAR_LIMITS["Incidents"]["rootCause"]
        action = Util.default_connector(CreateIncident())
        action.run({"record": {"rootCause": "r" * (limit + 500), "lessonsLearned": "l" * (limit + 500)}})

        posted = self.sent("POST")
        self.assertEqual(len(posted["rootCause"]), limit - CHAR_LIMIT_MARGIN)
        self.assertEqual(len(posted["lessonsLearned"]), limit - CHAR_LIMIT_MARGIN)


class TestCommentCharLimit(TestCase):
    def setUp(self):
        Util.calls = []

    def run_comment(self, comment):
        action = Util.default_connector(AddComment())
        with patch("requests.Session.request", side_effect=comment_server):
            return action.run({"record_type": "Tasks", "id": 4, "comment": comment, "user_id": 5})

    @staticmethod
    def posted():
        return next(call["json"] for call in Util.calls if call["method"] == "POST")

    def test_an_over_limit_comment_is_truncated(self):
        self.run_comment("c" * (COMMENT_LIMIT + 1000))

        self.assertEqual(len(self.posted()["comment"]), COMMENT_LIMIT - CHAR_LIMIT_MARGIN)

    def test_a_comment_within_the_limit_is_left_untouched(self):
        text = "c" * (COMMENT_LIMIT - 1)
        self.run_comment(text)

        self.assertEqual(self.posted()["comment"], text)
