import sys

sys.path.append("../")

from unittest import TestCase
from unittest.mock import Mock, patch

from icon_zendesk.actions.search import Search
from icon_zendesk.actions.search.schema import Input
from icon_zendesk.util.messages import Messages

from util import Util
from typing import Dict, Any, Tuple
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException


class TestSearch(TestCase):
    @classmethod
    @patch("zenpy.SearchApi.__call__", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(Search())
        cls.maxDiff = None

    @parameterized.expand(
        [
            (
                "Organization",
                {
                    "organizations": [
                        {
                            "created_at": "2009-07-20T22:55:29Z",
                            "details": "Example Organization",
                            "external_id": "1234",
                            "group_id": 1,
                            "id": 1234,
                            "name": "Example Organization",
                            "shared_comments": True,
                            "shared_tickets": True,
                            "tags": ["enterprise"],
                            "updated_at": "2011-05-05T10:38:52Z",
                            "url": "https://company.zendesk.com/api/v2/organizations/1234.json",
                        }
                    ]
                },
            ),
            (
                "Ticket",
                {
                    "tickets": [
                        {
                            "assignee_id": 1902872923580,
                            "brand_id": 4414536111640,
                            "collaborator_ids": [],
                            "created_at": "2022-01-12T18:08:44Z",
                            "description": "A ticket description",
                            "group_id": 4414536112530,
                            "has_incidents": False,
                            "id": 5,
                            "organization_id": 1260928947860,
                            "priority": "urgent",
                            "raw_subject": "Breach",
                            "requester_id": 1902872923580,
                            "sharing_agreement_ids": [],
                            "status": "open",
                            "subject": "Breach",
                            "submitter_id": 1902872923580,
                            "tags": [],
                            "type": "problem",
                            "updated_at": "2022-01-12T18:08:44Z",
                            "url": "https://organization.zendesk.com/api/v2/tickets/5.json",
                        }
                    ]
                },
            ),
            (
                "User",
                {
                    "users": [
                        {
                            "active": True,
                            "created_at": "2022-01-04T17:38:19Z",
                            "email": "user@example.com",
                            "id": 6,
                            "last_login_at": "2022-01-13T15:12:00Z",
                            "locale": "en-US",
                            "locale_id": 1,
                            "moderator": True,
                            "name": "First Last",
                            "only_private_comments": False,
                            "organization_id": 1260928947860,
                            "restricted_agent": False,
                            "role": "admin",
                            "shared": False,
                            "shared_agent": False,
                            "suspended": False,
                            "tags": [],
                            "time_zone": "America/New_York",
                            "updated_at": "2022-01-13T15:12:00Z",
                            "url": "https://organization.zendesk.com/api/v2/users/1902872923580.json",
                            "verified": True,
                        }
                    ]
                },
            ),
        ]
    )
    @patch("zenpy.SearchApi.__call__", side_effect=Util.mocked_requests)
    def test_search(self, input_type: str, expected: Dict[str, Any], mock_request: Mock) -> None:
        # happy path test
        response = self.action.run({Input.TYPE: input_type, Input.ITEM: "Example Item"})
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                "Empty",
                (
                    PluginException.causes[PluginException.Preset.NOT_FOUND],
                    PluginException.assistances[PluginException.Preset.NOT_FOUND],
                ),
            ),
            ("Error", (Messages.EXCEPTION_TOO_MANY_VALUES_CAUSE, Messages.EXCEPTION_TOO_MANY_VALUES_ASSISTANCE)),
            (
                "Error 2",
                (
                    Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_CAUSE,
                    Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_ASSISTANCE,
                ),
            ),
        ]
    )
    @patch("zenpy.SearchApi.__call__", side_effect=Util.mocked_requests)
    def test_exceptions(self, input_type: str, expected_error: Tuple[str], mock_request: Mock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.TYPE: input_type, Input.ITEM: "Example Item"})
        self.assertEqual(context.exception.cause, expected_error[0])
        self.assertEqual(context.exception.assistance, expected_error[1])
