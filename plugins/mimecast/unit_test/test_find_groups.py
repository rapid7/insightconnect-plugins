import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import FindGroups
from komand_mimecast.actions.find_groups.schema import FindGroupsOutput, FindGroupsInput

from util import EXPIRED_ACCESS_TOKEN, Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestFindGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(FindGroups())

    def test_find_group(self, _mocked_request):
        input_data = Util.load_json("inputs/find_groups.json.exp")
        validate(input_data, FindGroupsInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/find_groups.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, FindGroupsOutput.schema)

    def test_empty_response(self, _mocked_request):
        actual = self.action.run(Util.load_json("inputs/find_groups_with_filter.json.exp"))
        expect = Util.load_json("expected/find_groups_empty_groups.json.exp")
        self.assertEqual(expect, actual)

    def test_find_groups_token_expired(self, mocked_request):
        # The stored token is expired so the action re-authenticates and retries the call
        self.action.connection.client.access_token = EXPIRED_ACCESS_TOKEN
        actual = self.action.run(Util.load_json("inputs/find_groups.json.exp"))
        self.assertEqual(Util.load_json("expected/find_groups.json.exp"), actual)
        self.assertEqual(mocked_request.call_count, 3)
        validate(actual, FindGroupsOutput.schema)
