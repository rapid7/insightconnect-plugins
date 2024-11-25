import os
import sys

sys.path.append(os.path.abspath("../"))

from util import Util
from unittest import TestCase
from unittest.mock import MagicMock, patch
from jsonschema import validate
from komand_redis.actions.set import Set


class TestSet(TestCase):
    def setUp(self) -> None:
        self.action = None

        @patch("redis.StrictRedis", return_value=Util.mock_redis())
        def mocked_connector(mocked_redis: MagicMock) -> None:
            self.action = Util.default_connector(Set())

        mocked_connector()

    def test_set(self):
        input_param = Util.load_json("inputs/set.json.exp")
        expect = Util.load_json("expected/set_exp.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
