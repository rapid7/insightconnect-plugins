import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.exit import Exit
from komand_cuckoo.actions.exit.schema import ExitOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestExit(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Exit())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("expected/exit_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_exit(self, test_name, expected, mock_request):
        actual = self.action.run()
        self.assertEqual(expected, actual)
        validate(actual, ExitOutput.schema)
