import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_sentinelone.actions.get_threat_summary import GetThreatSummary

from util import Util


class TestGetThreatSummary(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetThreatSummary())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success(self, mock_request):
        expected = {
            "data": [
                {"id": "1111-1111-11111111-1111"},
                {"id": "1111-1111-11111111-1112"},
                {"id": "1111-1111-11111111-1113"},
                {"id": "1111-1111-11111111-1114"},
            ],
            "errors": [],
        }
        actual = self.action.run()
        self.assertEqual(expected, actual)
