import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_web_logs import GetWebLogs


@patch("requests.request", side_effect=Util.mock_request)
class TestGetWebLogs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetWebLogs())

    def test_get_web_logs(self, _mock_request):
        mock_response = {
            "logs": [{"timestamp": "2024-01-01T00:00:00Z", "url": "example.com"}],
            "next_link": "",
        }
        self.action.connection.zia_client.get_web_logs = MagicMock(return_value=mock_response)
        result = self.action.run({"start_time": "2024-01-01T00:00:00Z", "end_time": "2024-01-02T00:00:00Z"})
        self.assertEqual(result["logs"], [{"timestamp": "2024-01-01T00:00:00Z", "url": "example.com"}])
