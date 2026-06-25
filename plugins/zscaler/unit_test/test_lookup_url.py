import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock

from util import Util
from icon_zscaler.actions.lookup_url import LookupUrl


@patch("requests.request", side_effect=Util.mock_request)
class TestLookupUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupUrl())

    def test_lookup_url(self, _mock_request):
        input_params = {"urls": ["http://example.com"]}
        self.action.connection.zia_client.url_lookup = MagicMock(
            return_value=[{"url": "example.com", "urlClassifications": ["REFERENCE_SITES"]}]
        )
        result = self.action.run(input_params)
        self.assertEqual(
            result,
            {"url_categorization": [{"url": "example.com", "urlClassifications": ["REFERENCE_SITES"]}]},
        )
        self.action.connection.zia_client.url_lookup.assert_called_once_with(["example.com"])
