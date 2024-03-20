import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.get_pcap import GetPcap
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestGetPcap(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetPcap())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/get_pcap_success.json.inp"),
                Util.read_file_to_dict("expected/get_pcap_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_pcap(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
