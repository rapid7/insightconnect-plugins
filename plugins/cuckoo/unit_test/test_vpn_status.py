import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.vpn_status import VpnStatus
from komand_cuckoo.actions.vpn_status.schema import VpnStatusOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestVpnStatus(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(VpnStatus())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("expected/vpn_status_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_vpn_status(self, test_name, expected, mock_request):
        actual = self.action.run()
        self.assertEqual(expected, actual)
        validate(actual, VpnStatusOutput.schema)
