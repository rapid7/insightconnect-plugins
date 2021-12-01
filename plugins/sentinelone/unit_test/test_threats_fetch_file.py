import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.threats_fetch_file import ThreatsFetchFile
from komand_sentinelone.actions.threats_fetch_file.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestThreatsFetchFile(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ThreatsFetchFile())

    @patch("requests.get", side_effect=Util.mocked_requests_get)
    def test_should_success_when_id_and_password(self, mock_request):
        actual = self.action.run(
            {
                Input.ID: "id",
                Input.PASSWORD: "password",
            }
        )
        expected = {}
        self.assertEqual(expected, actual)
