import os
import sys

sys.path.append(os.path.abspath("../"))

from util import Util
from unittest import TestCase
from unittest.mock import MagicMock, patch
from jsonschema import validate
from komand_redis.actions.list_push import ListPush


class TestListPush(TestCase):
    def setUp(self) -> None:
        self.action = None

        @patch("redis.StrictRedis", return_value=Util.mock_redis())
        def mocked_connector(mocked_redis: MagicMock) -> None:
            self.action = Util.default_connector(ListPush())

        mocked_connector()

    def test_list_push(self):
        input_param = Util.load_json("inputs/list_push.json.exp")
        expect = Util.load_json("expected/list_push_exp.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
