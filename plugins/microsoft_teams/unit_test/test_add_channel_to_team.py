import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_microsoft_teams.actions.add_channel_to_team.action import AddChannelToTeam
from icon_microsoft_teams.actions.add_channel_to_team.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util
from unittest import TestCase, mock
from unittest.mock import Mock
from parameterized import parameterized

STUB_TEAM_NAME = "Example Team"
STUB_CHANNEL_NAME = "ExampleName"
STUB_CHANNEL_DESCRIPTION = "Example Channel Description"

STUB_EXAMPLE_ACTION_RESPONSE = {"success": True}


class TestAddChannelToTeam(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(AddChannelToTeam())
        self.payload = {
            Input.TEAM_NAME: STUB_TEAM_NAME,
            Input.CHANNEL_NAME: STUB_CHANNEL_NAME,
            Input.CHANNEL_DESCRIPTION: STUB_CHANNEL_DESCRIPTION,
        }

    @parameterized.expand([("Standard",), ("Private",)])
    @mock.patch("requests.get", side_effect=Util.mocked_requests)
    @mock.patch("requests.post", side_effect=Util.mocked_requests)
    def test_add_group_owner(self, mock_requests_get: Mock, mock_requests_post: Mock, channel_type: str) -> None:
        response = self.action.run({**self.payload, "channel_type": channel_type})
        expected_response = STUB_EXAMPLE_ACTION_RESPONSE
        self.assertEqual(response, expected_response)
