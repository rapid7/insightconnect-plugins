import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_sentinelone.actions.mitigate_threat import MitigateThreat
from komand_sentinelone.actions.mitigate_threat.schema import Input

from util import Util


class TestMitigateThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MitigateThreat())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_target_scope(self, mock_request):
        expected = {"affected": 1}
        for test in [
            "rollback-remediation",
            "quarantine",
            "kill",
            "remediate",
            "un-quarantine",
        ]:
            with self.subTest(f"Running agent with action: {test}"):
                actual = self.action.run({Input.THREAT_ID: "1000000000000000000", Input.ACTION: test})
                self.assertEqual(expected, actual)
