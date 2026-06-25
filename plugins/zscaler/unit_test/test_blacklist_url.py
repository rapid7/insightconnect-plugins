import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

from util import Util
from icon_zscaler.actions.blacklist_url import BlacklistUrl


@patch("requests.request", side_effect=Util.mock_request)
class TestBlacklistUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(BlacklistUrl())

    def test_blacklist_url(self, _mock_request):
        input_params = {"urls": ["http://malicious.com"], "blacklist_state": True, "activate_configuration": False}
        self.action.connection.zia_client.blacklist_url = MagicMock(return_value=True)
        mock_status_response = Mock()
        mock_status_response.json.return_value = {"status": "ACTIVE"}
        self.action.connection.zia_client.get_status = MagicMock(return_value=mock_status_response)
        result = self.action.run(input_params)
        self.assertEqual(result, {"success": True, "status": "ACTIVE"})
        self.action.connection.zia_client.blacklist_url.assert_called_once_with("ADD_TO_LIST", ["malicious.com"])
