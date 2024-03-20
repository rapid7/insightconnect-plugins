import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.get_memory import GetMemory
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestGetMemory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetMemory())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/get_memory_success.json.inp"),
                Util.read_file_to_dict("expected/get_memory_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_memory(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
