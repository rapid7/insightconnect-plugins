import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.submit_threat_feed import SubmitThreatFeed


@patch("requests.request", side_effect=Util.mock_request)
class TestSubmitThreatFeed(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitThreatFeed())

    def test_submit_threat_feed(self, _mock_request):
        mock_response = {"success": True, "submitted_count": 3}
        self.action.connection.zia_client.submit_threat_feed = MagicMock(return_value=mock_response)
        result = self.action.run(
            {
                "feed_type": "IP",
                "indicators": ["1.2.3.4", "5.6.7.8", "9.10.11.12"],
                "description": "Test feed",
            }
        )
        self.assertEqual(result, {"success": True, "submitted_count": 3})
