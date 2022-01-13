from unittest import TestCase
from komand_zendesk.actions.show_user import ShowUser
from komand_zendesk.actions.show_user.schema import Input, Output
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


class TestCreate(TestCase):
    @classmethod
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ShowUser())

    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_show_user(self, mock_request):
        # happy path test
        actual = self.action.run({Input.USER_ID: 1902872923584})
        expected_role = "admin"
        self.assertEqual(actual.get(Output.USER).get("role"), expected_role)

    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_show_user_fails(self, mock_request):
        with self.assertRaises(PluginException) as exc:
            actual = self.action.run({Input.USER_ID: -1})
        self.assertEqual(exc.exception.assistance, "Make sure the input user ID is correct.")
