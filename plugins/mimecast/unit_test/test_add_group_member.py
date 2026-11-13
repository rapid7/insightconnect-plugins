import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_mimecast.actions import AddGroupMember
from komand_mimecast.actions.add_group_member.schema import AddGroupMemberOutput, AddGroupMemberInput
from komand_mimecast.util.constants import API, BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, GROUP_MEMBER_ALREADY_EXISTS_ERROR

from util import EXPIRED_ACCESS_TOKEN, Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestAddGroupMember(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddGroupMember())

    def test_add_group_member(self, _mock_request):
        input_data = Util.load_json("inputs/add_group_member.json.exp")
        actual = self.action.run(input_data)
        validate(input_data, AddGroupMemberInput.schema)
        expect = Util.load_json("expected/add_group_member_exp.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, AddGroupMemberOutput.schema)

    def test_bad_add_group_member(self, _mock_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/add_group_member_bad.json.exp"))
        self.assertEqual(exception.exception.cause, ERROR_CASES.get(GROUP_MEMBER_ALREADY_EXISTS_ERROR))
        self.assertEqual(exception.exception.assistance, BASIC_ASSISTANCE_MESSAGE)

    def test_add_group_member_token_expired(self, mock_request):
        self.action.connection.client.access_token = EXPIRED_ACCESS_TOKEN
        actual = self.action.run(Util.load_json("inputs/add_group_member.json.exp"))

        # The retry must use the new token and send the same payload, not wrap it a second time
        first_call, auth_call, retried_call = mock_request.call_args_list
        self.assertEqual(auth_call.kwargs["url"], f"{API}/oauth/token")
        self.assertEqual(first_call.kwargs["headers"]["Authorization"], f"Bearer {EXPIRED_ACCESS_TOKEN}")
        self.assertEqual(retried_call.kwargs["headers"]["Authorization"], "Bearer RPjLow4SKlsPLycjML3dqvIxzi7B")
        self.assertEqual(retried_call.kwargs["json"], first_call.kwargs["json"])
        self.assertEqual(actual, Util.load_json("expected/add_group_member_exp.json.exp"))
        validate(actual, AddGroupMemberOutput.schema)
