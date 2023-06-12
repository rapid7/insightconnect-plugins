import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import GetTtpUrlLogs

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetManagedUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTtpUrlLogs())

    def test_get_ttp_url_logs(self, mocked_request):
        actual = self.action.run(Util.load_json("inputs/get_ttp_url_logs.json.exp"))
        expect = Util.load_json("expected/get_ttp_url_logs.json.exp")
        self.assertEqual(expect, actual)
