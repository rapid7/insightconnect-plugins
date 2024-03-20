import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.list_memory import ListMemory
from komand_cuckoo.actions.list_memory.schema import ListMemoryOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestListMemory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListMemory())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/list_memory_success.json.inp"),
                Util.read_file_to_dict("expected/list_memory_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_list_memory(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, ListMemoryOutput.schema)
