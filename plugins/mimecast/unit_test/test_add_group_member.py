import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_mimecast.actions import AddGroupMember
from komand_mimecast.actions.add_group_member.schema import AddGroupMemberOutput, AddGroupMemberInput
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, GROUP_MEMBER_ALREADY_EXISTS_ERROR

from util import Util


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
