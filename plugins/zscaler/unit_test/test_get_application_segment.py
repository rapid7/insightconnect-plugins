import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_application_segment import GetApplicationSegment


@patch("requests.request", side_effect=Util.mock_request)
class TestGetApplicationSegment(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetApplicationSegment())

    def test_get_application_segment(self, _mock_request):
        mock_segment = {"id": "seg-1", "name": "Internal App", "enabled": True}
        self.action.connection.zpa_client.get_application_segment = MagicMock(return_value=mock_segment)
        result = self.action.run({"segment_id": "seg-1"})
        self.assertEqual(result, {"segment": mock_segment})
