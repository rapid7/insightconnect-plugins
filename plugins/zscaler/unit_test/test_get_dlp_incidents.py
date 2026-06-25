import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_dlp_incidents import GetDlpIncidents


@patch("requests.request", side_effect=Util.mock_request)
class TestGetDlpIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetDlpIncidents())

    def test_get_dlp_incidents(self, _mock_request):
        mock_response = {
            "incidents": [{"id": 1, "severity": "HIGH"}],
            "next_link": "https://api.zsapi.net/zia/api/v1/dlp/incidents?page=2",
        }
        self.action.connection.zia_client.get_dlp_incidents = MagicMock(return_value=mock_response)
        result = self.action.run({"start_time": "2024-01-01T00:00:00Z", "end_time": "2024-01-02T00:00:00Z"})
        self.assertEqual(result["incidents"], [{"id": 1, "severity": "HIGH"}])
        self.assertEqual(result["next_link"], "https://api.zsapi.net/zia/api/v1/dlp/incidents?page=2")
