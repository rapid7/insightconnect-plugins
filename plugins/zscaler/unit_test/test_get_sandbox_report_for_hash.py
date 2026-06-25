import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from icon_zscaler.actions.get_sandbox_report_for_hash import GetSandboxReportForHash


@patch("requests.request", side_effect=Util.mock_request)
class TestGetSandboxReportForHash(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetSandboxReportForHash())

    def test_get_sandbox_report_for_hash(self, _mock_request):
        mock_report = {"Summary": {"Status": "COMPLETED"}, "Classification": {"Category": "MALICIOUS"}}
        self.action.connection.zia_client.get_hash_report = MagicMock(return_value=mock_report)
        # Valid MD5 hash
        result = self.action.run({"hash": "d41d8cd98f00b204e9800998ecf8427e"})
        self.assertEqual(result, {"full_report": mock_report})

    def test_get_sandbox_report_for_hash_invalid(self, _mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run({"hash": "not-a-valid-hash"})
        self.assertEqual(error.exception.cause, "Provided hash is not supported.")
