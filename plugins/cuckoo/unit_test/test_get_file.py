import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.get_file import GetFile
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestGetFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFile())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/get_file_success.json.inp"),
                Util.read_file_to_dict("expected/get_file_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_file(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
