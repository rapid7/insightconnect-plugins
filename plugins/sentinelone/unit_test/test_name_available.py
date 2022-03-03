import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.name_available import NameAvailable
from komand_sentinelone.actions.name_available.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestNameAvailable(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(NameAvailable())

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success(self, mock_request):
        expected = {"available": True}
        actual = self.action.run({Input.NAME: "account_name"})
        self.assertEqual(expected, actual)
