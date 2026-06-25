import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.get_blacklist_url import GetBlacklistUrl


@patch("requests.request", side_effect=Util.mock_request)
class TestGetBlacklistUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetBlacklistUrl())

    def test_get_blacklist_url(self, _mock_request):
        self.action.connection.zia_client.get_blacklist_url = MagicMock(
            return_value={"blacklistUrls": ["malicious.com", "bad-site.org"]}
        )
        result = self.action.run({})
        self.assertEqual(result, {"blacklisted_urls": ["malicious.com", "bad-site.org"]})
