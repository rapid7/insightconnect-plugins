import sys

sys.path.append("../")

from unittest import TestCase
from unittest.mock import Mock, patch

from icon_zendesk.actions.show_memberships import ShowMemberships
from icon_zendesk.actions.show_memberships.schema import Input
from icon_zendesk.util.messages import Messages

from util import Util
from typing import Dict, Any, Tuple
from parameterized import parameterized

from insightconnect_plugin_runtime.exceptions import PluginException


class TestShowMemberships(TestCase):
    @classmethod
    @patch("zenpy.UserApi.organization_memberships", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: Mock) -> None:
        cls.action = Util.default_connector(ShowMemberships())

    @patch("zenpy.UserApi.organization_memberships", side_effect=Util.mocked_requests)
    def test_show_memberships(self, mock_request: Mock) -> None:
        # happy path test
        response = self.action.run({Input.USER_ID: 1})
        expected = {
            "memberships": [
                {
                    "id": 1261124434660,
                    "user_id": 1902872923580,
                    "organization_id": 1260928947860,
                    "default": True,
                    "created_at": "2022-01-04T17:38:25Z",
                    "updated_at": "2022-01-04T17:38:25Z",
                }
            ]
        }
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (
                -1,
                (
                    PluginException.causes[PluginException.Preset.UNKNOWN],
                    PluginException.assistances[PluginException.Preset.UNKNOWN],
                ),
            ),
            (-2, (Messages.EXCEPTION_TOO_MANY_VALUES_CAUSE, Messages.EXCEPTION_TOO_MANY_VALUES_ASSISTANCE)),
            (
                -3,
                (
                    Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_CAUSE,
                    Messages.EXCEPTION_SEARCH_RESPONSE_LIMIT_EXCEEDED_ASSISTANCE,
                ),
            ),
        ]
    )
    @patch("zenpy.UserApi.organization_memberships", side_effect=Util.mocked_requests)
    def test_exceptions(self, input_user_id: int, expected_error: Tuple[str], mock_request: Mock) -> None:
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.USER_ID: input_user_id})
        self.assertEqual(context.exception.cause, expected_error[0])
        self.assertEqual(context.exception.assistance, expected_error[1])
