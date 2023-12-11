import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.get_threat_summary import GetThreatSummary
from komand_sentinelone.actions.get_threat_summary.schema import GetThreatSummaryOutput
from util import Util
from unittest import TestCase
from parameterized import parameterized
from jsonschema import validate


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetThreatSummary(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetThreatSummary())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("expected/get_threat_summary.json.exp"),
            ],
        ]
    )
    def test_get_threat_summary(self, mock_request, test_name, expected):
        actual = self.action.run()
        self.assertEqual(expected, actual)
        validate(actual, GetThreatSummaryOutput.schema)
