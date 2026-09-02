"""Covers the ten typed entity action families.

Each family is generated from the same shape, so the interesting behaviour is that
every action targets the right /api/v2 collection and returns it under the right
output key. These cases assert exactly that, across all fifty typed actions.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from parameterized import parameterized

from icon_rapid7_cyber_grc import actions
from util import BASE_URL, Util

# (entity path segment, singular output key, plural output key, class name stem)
FAMILIES = [
    ("Risks", "risk", "risks", "Risk"),
    ("Incidents", "incident", "incidents", "Incident"),
    ("Tasks", "task", "tasks", "Task"),
    ("Audits", "audit", "audits", "Audit"),
    ("ControlSets", "control_set", "control_sets", "ControlSet"),
    ("Assessments", "assessment", "assessments", "Assessment"),
    ("Vendors", "vendor", "vendors", "Vendor"),
    ("Certifications", "certification", "certifications", "Certification"),
    ("ITAssets", "it_asset", "it_assets", "ItAsset"),
    ("Users", "user", "users", "User"),
]

LIST_CASES = [[entity, plural, f"Get{stem}s"] for entity, _, plural, stem in FAMILIES]
GET_CASES = [[entity, singular, f"Get{stem}"] for entity, singular, _, stem in FAMILIES]
CREATE_CASES = [[entity, singular, f"Create{stem}"] for entity, singular, _, stem in FAMILIES]
UPDATE_CASES = [[entity, singular, f"Update{stem}"] for entity, singular, _, stem in FAMILIES]
DELETE_CASES = [[entity, f"Delete{stem}"] for entity, _, _, stem in FAMILIES]


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestCoreActions(TestCase):
    def setUp(self):
        Util.calls = []
        Util.updated = {}

    @staticmethod
    def run_action(class_name, params):
        action = Util.default_connector(getattr(actions, class_name)())
        return action.run(params)

    @parameterized.expand(LIST_CASES)
    def test_list_action_returns_records_and_a_count(self, mock_request, entity, plural, class_name):
        actual = self.run_action(class_name, {"filter": "statusID eq 3", "top": 0})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/{entity}")
        self.assertEqual(Util.calls[0]["params"], {"$filter": "statusID eq 3"})
        self.assertEqual([item["id"] for item in actual[plural]], [1, 2])
        self.assertEqual(actual["count"], 2)

    @parameterized.expand(GET_CASES)
    def test_get_action_returns_one_record(self, mock_request, entity, singular, class_name):
        actual = self.run_action(class_name, {"id": 4, "select": "id,name"})

        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/{entity}/4")
        self.assertEqual(Util.calls[0]["params"], {"$select": "id,name"})
        self.assertEqual(actual[singular]["id"], 4)

    @parameterized.expand(CREATE_CASES)
    def test_create_action_posts_the_record(self, mock_request, entity, singular, class_name):
        actual = self.run_action(class_name, {"record": {"name": "Fresh"}})

        self.assertEqual(Util.calls[0]["method"], "POST")
        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/{entity}")
        self.assertEqual(actual[singular]["name"], "Fresh")

    @parameterized.expand(UPDATE_CASES)
    def test_update_action_puts_the_record(self, mock_request, entity, singular, class_name):
        actual = self.run_action(class_name, {"id": 4, "record": {"name": "Changed"}})

        self.assertEqual(Util.calls[0]["method"], "PUT")
        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/{entity}/4")
        self.assertEqual(actual[singular]["name"], "Changed")

    @parameterized.expand(DELETE_CASES)
    def test_delete_action_reports_the_outcome(self, mock_request, entity, class_name):
        actual = self.run_action(class_name, {"id": 4})

        self.assertEqual(Util.calls[0]["method"], "DELETE")
        self.assertEqual(Util.calls[0]["url"], f"{BASE_URL}/api/v2/{entity}/4")
        self.assertTrue(actual["result"]["success"])

    def test_every_typed_action_is_covered(self, mock_request):
        covered = {case[-1] for case in LIST_CASES + GET_CASES + CREATE_CASES + UPDATE_CASES + DELETE_CASES}
        generic = {
            "ListRecords",
            "GetRecord",
            "CreateRecord",
            "UpdateRecord",
            "DeleteRecord",
            "CountRecords",
            "GetRecordHistory",
            "UploadFlatFile",
        }
        typed = {name for name in dir(actions) if isinstance(getattr(actions, name), type) and name not in generic}

        self.assertEqual(typed, covered)
