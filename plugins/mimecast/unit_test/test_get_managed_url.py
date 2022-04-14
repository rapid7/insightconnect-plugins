import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from komand_mimecast.actions import GetManagedUrl


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetManagedUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetManagedUrl())

    def test_get_managed_url(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/get_managed_url.json.exp"))
        expect = Util.load_json("expected/get_managed_url.json.exp")
        self.assertEqual(expect, actual)

    def test_empty_response(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/get_managed_url_with_filter.json.exp"))
        expect = Util.load_json("expected/get_managed_url_empty_response.json.exp")
        self.assertEqual(expect, actual)

