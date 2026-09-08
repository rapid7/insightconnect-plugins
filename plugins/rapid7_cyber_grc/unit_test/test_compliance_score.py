"""Covers Get Compliance Score.

Cyber GRC has no tenant wide score endpoint and keeps every past calculation in
ControlSetMetrics, so the action picks the newest row per framework, names it from the
control sets, and averages what is left. These cases pin that behaviour down.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

from icon_rapid7_cyber_grc.actions import GetComplianceScore
from icon_rapid7_cyber_grc.util.compliance import number
from util import BASE_URL, Util


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGetComplianceScore(TestCase):
    def setUp(self):
        Util.calls = []

    @staticmethod
    def run_action(params):
        return Util.default_connector(GetComplianceScore()).run(params)

    def test_scores_every_live_framework_newest_calculation_first(self, mock_request):
        actual = self.run_action({"control_set_id": 0})

        # Control set 1 has a newer and an older calculation and only the newer counts,
        # control set 3 is archived, and control set 4 has never been scored.
        self.assertEqual(
            actual["frameworks"],
            [
                {
                    "control_set_id": 1,
                    "name": "SOC 2",
                    "compliance": 80.0,
                    "linked_controls_percentage": 50.0,
                    "automated_controls_percentage": 40.0,
                    "date_calculated": "2026-09-01T00:00:00.000Z",
                },
                {
                    "control_set_id": 2,
                    "name": "ISO 27001",
                    "compliance": 60.0,
                    "linked_controls_percentage": 70.0,
                    "automated_controls_percentage": 20.0,
                    "date_calculated": "2026-08-01T00:00:00.000Z",
                },
            ],
        )

    def test_overall_is_the_mean_of_the_frameworks_returned(self, mock_request):
        actual = self.run_action({"control_set_id": 0})

        self.assertEqual(
            actual["overall"],
            {"compliance": 70.0, "automated_controls_percentage": 30.0, "framework_count": 2},
        )

    def test_the_control_sets_are_read_before_the_scores(self, mock_request):
        # The control sets name each framework and say which are in use, and their number
        # is what bounds the scoring reads that follow.
        self.run_action({"control_set_id": 0})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/ControlSets")
        self.assertEqual(Util.calls[0]["params"], {"$select": "id,name,enabled,isArchived"})

    def test_only_the_newest_scoring_of_each_framework_is_read(self, mock_request):
        # ControlSetMetrics holds every calculation ever made for every framework, so it
        # is asked for one row per framework rather than read whole. Reading it whole
        # meant paging tens of thousands of rows to use a handful of them, which exhausts
        # the API rate limit on a tenant with real scoring history.
        self.run_action({"control_set_id": 0})

        scoring = [call for call in Util.calls if call["url"].endswith("/ControlSetMetrics")]
        self.assertEqual(
            [call["params"] for call in scoring],
            [
                {"$filter": f"controlSetID eq {set_id}", "$orderby": "dateCalculated desc", "$top": 1}
                for set_id in (1, 2, 4)
            ],
        )

    def test_a_framework_scored_more_than_once_reports_its_latest_score(self, mock_request):
        # Control set 1 has an older calculation as well as a newer one.
        actual = self.run_action({"control_set_id": 1})

        self.assertEqual(actual["frameworks"][0]["compliance"], 80.0)
        self.assertEqual(actual["frameworks"][0]["date_calculated"], "2026-09-01T00:00:00.000Z")

    def test_a_named_control_set_is_scored_even_when_archived(self, mock_request):
        actual = self.run_action({"control_set_id": 3})

        scoring = [call for call in Util.calls if call["url"].endswith("/ControlSetMetrics")]
        self.assertEqual(scoring[0]["params"]["$filter"], "controlSetID eq 3")
        self.assertEqual([framework["control_set_id"] for framework in actual["frameworks"]], [3])
        self.assertEqual(actual["overall"]["framework_count"], 1)

    def test_an_unscored_tenant_returns_zeroes_rather_than_failing(self, mock_request):
        actual = self.run_action({"control_set_id": 999})

        self.assertEqual(actual["frameworks"], [])
        self.assertEqual(
            actual["overall"],
            {"compliance": 0.0, "automated_controls_percentage": 0.0, "framework_count": 0},
        )


class TestScoreNumbers(TestCase):
    """Turning whatever Cyber GRC stored into a score the output schema can carry.

    Every score field is a required float, so an absent or unreadable value has to become
    a number rather than a null that would fail validation or a gap in a report.
    """

    @parameterized.expand(
        [
            ["a_float", 80.0, 80.0],
            ["an_int", 80, 80.0],
            ["a_string", "72.5", 72.5],
            ["extra_precision", 33.333333, 33.33],
            ["rounds_up", 66.666666, 66.67],
            ["absent", None, 0.0],
            ["unreadable", "not a score", 0.0],
        ]
    )
    def test_a_score_is_a_float_rounded_to_two_places(self, _name, value, expected):
        self.assertEqual(number(value), expected)
