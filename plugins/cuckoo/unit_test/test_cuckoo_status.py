import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.cuckoo_status import CuckooStatus
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestCuckooStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CuckooStatus())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("expected/cuckoo_status_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_cuckoo_status(self, test_name, expected, mock_request):
        actual = self.action.run()
        self.assertEqual(expected, actual)
