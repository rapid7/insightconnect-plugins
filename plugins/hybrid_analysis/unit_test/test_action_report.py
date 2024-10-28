import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from icon_hybrid_analysis.actions.report import Report
from icon_hybrid_analysis.actions.report.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util


class TestReport(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(Report())

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_report(self, mocked_request):
        actual = self.action.run({Input.HASH: "30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050"})
        expected = {"related_reports": [], "state": "SUCCESS"}
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_bad_report(self, mocked_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.HASH: "1"})

        self.assertEqual("Provided hash is not supported.", context.exception.cause)
        self.assertEqual(
            "The API only supports SHA256 hashes. Please check the provided hash and try again.",
            context.exception.assistance,
        )
