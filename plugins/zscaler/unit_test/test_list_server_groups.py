import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.list_server_groups import ListServerGroups


@patch("requests.request", side_effect=Util.mock_request)
class TestListServerGroups(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListServerGroups())

    def test_list_server_groups(self, _mock_request):
        mock_response = {
            "groups": [{"id": "grp-1", "name": "DC Servers"}],
            "next_link": "",
        }
        self.action.connection.zpa_client.list_server_groups = MagicMock(return_value=mock_response)
        result = self.action.run({})
        self.assertEqual(result["groups"], [{"id": "grp-1", "name": "DC Servers"}])
