import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from icon_rapid7_insightvm_cloud.connection.connection import Connection
from icon_rapid7_insightvm_cloud.actions.get_scan import GetScan
from icon_rapid7_insightvm_cloud.actions.get_scan.schema import Input
from icon_rapid7_insightvm_cloud.connection.schema import Input as ConnectionInput
from unittest.mock import patch
from unit_test.utils import Utils
from unit_test.mock import (
    mock_request,
)


class TestGetScan(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.params = {
            "scan_id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
            "scan_id_invalid": "5058b0b4-701a-414e-9630-430d2cddbf4e",
        }

    def setUp(self) -> None:
        self.connection, self.action = Utils.default_connector(GetScan())

    # test finding event via all inputs
    @patch("requests.request", side_effect=mock_request)
    def test_get_scan(self):
        actual = self.action.run({
            "scan_id": "5058b0b4-701a-414e-9630-430d2cddbf4d"
        })
        expected = Utils.read_file_to_dict("expected_responses/get_scan.json.resp")
        self.assertEqual(expected, actual)