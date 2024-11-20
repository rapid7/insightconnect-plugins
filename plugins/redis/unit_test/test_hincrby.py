import os
import sys

sys.path.append(os.path.abspath("../"))

from util import Util
from unittest import TestCase
from unittest.mock import MagicMock, patch
from jsonschema import validate
from komand_redis.actions.hincrby import Hincrby


class TestHincrby(TestCase):
    def setUp(self) -> None:
        self.action = None

        @patch("redis.StrictRedis", return_value=Util.mock_redis())
        def mocked_connector(mocked_redis: MagicMock) -> None:
            self.action = Util.default_connector(Hincrby())

        mocked_connector()

    def test_hincrby(self):
        input_param = Util.load_json("inputs/hincrby.json.exp")
        expect = Util.load_json("expected/hincrby_exp.json.exp")
        actual = self.action.run(input_param)
        validate(input_param, self.action.input.schema)
        self.assertEqual(expect, actual)
        validate(actual, self.action.output.schema)
