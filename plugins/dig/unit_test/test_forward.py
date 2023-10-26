import sys
import os
sys.path.append(os.path.abspath('../'))

from komand_dig.connection.connection import Connection
from unittest import TestCase
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from komand_dig.actions.forward import Forward


@patch("insightconnect_plugin_runtime.helper.exec_command", side_effect=Util.mock_dig)
class TestForward(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Forward())

    @parameterized.expand(
        [
            [
                "forward",
                Util.read_file_to_dict("inputs/forward.json.inp"),
                Util.read_file_to_dict("expected/forward.json.exp")

            ]
        ]
    )
    def test_forward(self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict):

        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    # def test_error(self, _mock_request: MagicMock, _test_name: str, input_params: dict, cause: str, assistance: str):
    #
    #     actual = self.action.run(input_params)
    #     self.assertEqual(error.exception.cause, cause)
    #     self.assertEqual(error.exception.assistance, assistance)
