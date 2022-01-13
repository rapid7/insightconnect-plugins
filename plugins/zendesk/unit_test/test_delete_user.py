from unittest import TestCase
from komand_zendesk.actions.delete_user import DeleteUser
from komand_zendesk.actions.delete_user.schema import Input, Output
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

from util import Util


class TestCreate(TestCase):
    @classmethod
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteUser())

    @patch("zenpy.UserApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_user(self, mock_request, mock_second):
        # happy path test- Note as of now- API just returns 204 and no actual response on success
        actual = self.action.run({Input.USER_ID: 0})
        self.assertEqual(actual.get(Output.STATUS), True)

    @patch("zenpy.UserApi.delete", side_effect=Util.mocked_requests)
    @patch("zenpy.UserApi.__call__", side_effect=Util.mocked_requests)
    def test_delete_user_fail(self, mock_request, mock_second):
        # Here -1 is showing a ticket id that doesn't exist. We don't expect an exception just a fail
        actual = self.action.run({Input.USER_ID: -1})
        self.assertEqual(actual.get(Output.STATUS), False)
