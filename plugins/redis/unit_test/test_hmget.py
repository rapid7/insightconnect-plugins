import os
import sys

sys.path.append(os.path.abspath("../"))

from util import Util
from unittest import TestCase
from unittest.mock import MagicMock, patch
from jsonschema import validate
from komand_redis.actions.hmget import Hmget


class TestHmget(TestCase):
    def setUp(self) -> None:
        self.action = None

        @patch("redis.StrictRedis", return_value=Util.mock_redis())
        def mocked_connector(mocked_redis: MagicMock) -> None:
            self.action = Util.default_connector(Hmget())

        mocked_connector()

    def test_hmget(self):
        input_param = Util.load_json("inputs/hmget.json.exp")
        expect = Util.load_json("expected/hmget_exp.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
