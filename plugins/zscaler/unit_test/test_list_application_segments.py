import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.list_application_segments import ListApplicationSegments


@patch("requests.request", side_effect=Util.mock_request)
class TestListApplicationSegments(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListApplicationSegments())

    def test_list_application_segments(self, _mock_request):
        mock_response = {
            "segments": [{"id": "seg-1", "name": "Internal App"}],
            "next_link": "",
        }
        self.action.connection.zpa_client.list_application_segments = MagicMock(return_value=mock_response)
        result = self.action.run({})
        self.assertEqual(result["segments"], [{"id": "seg-1", "name": "Internal App"}])
