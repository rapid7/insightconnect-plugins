import os
import sys
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_mimecast.actions import AddGroupMember
from komand_mimecast.util.constants import BASIC_ASSISTANCE_MESSAGE, ERROR_CASES, GROUP_MEMBER_ALREADY_EXISTS_ERROR

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestAddGroupMember(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddGroupMember())

    def test_add_group_member(self, mock_request):
        actual = self.action.run(Util.load_json("inputs/add_group_member.json.exp"))
        expect = Util.load_json("expected/add_group_member_exp.json.exp")
        self.assertEqual(expect, actual)

    def test_bad_add_group_member(self, mock_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(Util.load_json("inputs/add_group_member_bad.json.exp"))
        self.assertEqual(exception.exception.cause, ERROR_CASES.get(GROUP_MEMBER_ALREADY_EXISTS_ERROR))
        self.assertEqual(exception.exception.assistance, BASIC_ASSISTANCE_MESSAGE)
