import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_server_group import GetServerGroup


@patch("requests.request", side_effect=Util.mock_request)
class TestGetServerGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetServerGroup())

    def test_get_server_group(self, _mock_request):
        mock_group = {"id": "grp-1", "name": "DC Servers", "enabled": True}
        self.action.connection.zpa_client.get_server_group = MagicMock(return_value=mock_group)
        result = self.action.run({"group_id": "grp-1"})
        self.assertEqual(result, {"group": mock_group})
