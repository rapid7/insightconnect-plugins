from unittest import TestCase
from komand_zendesk.actions.suspend_user import SuspendUser
from komand_zendesk.actions.suspend_user.schema import Input, Output
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


class TestSuspendUser(TestCase):
    @classmethod
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(SuspendUser())

    @patch("zenpy.UserApi.update", side_effect=Util.mocked_requests)
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_suspend_user(self, mock_request, mock_second):
        # happy path test- Note as of now- API just returns 204 and no actual response on success
        actual = self.action.run({Input.USER_ID: 5})
        self.assertEqual(actual.get(Output.STATUS), True)

    @patch("zenpy.UserApi.update", side_effect=Util.mocked_requests)
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_suspend_user_fails(self, mock_request, mock_second):
        # Here id 6 exists but the update operation failed
        actual = self.action.run({Input.USER_ID: 6})
        self.assertEqual(actual.get(Output.STATUS), False)

    @patch("zenpy.UserApi.update", side_effect=Util.mocked_requests)
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_user_not_found(self, mock_request, mock_second):
        # Here -1 is showing a ticket id that doesn't exist. We don't expect an exception just a fail
        actual = self.action.run({Input.USER_ID: -1})
        self.assertEqual(actual.get(Output.STATUS), False)
