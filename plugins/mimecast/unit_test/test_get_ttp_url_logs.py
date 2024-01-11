import os
import sys
from jsonschema import validate
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from komand_mimecast.actions import GetTtpUrlLogs
from komand_mimecast.actions.get_ttp_url_logs.schema import GetTtpUrlLogsOutput, GetTtpUrlLogsInput

from util import Util


@patch("requests.request", side_effect=Util.mocked_request)
class TestGetManagedUrl(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetTtpUrlLogs())

    def test_get_ttp_url_logs(self, _mocked_request):
        input_data = Util.load_json("inputs/get_ttp_url_logs.json.exp")
        validate(input_data, GetTtpUrlLogsInput.schema)
        actual = self.action.run(input_data)
        expect = Util.load_json("expected/get_ttp_url_logs.json.exp")
        self.assertEqual(expect, actual)
        validate(actual, GetTtpUrlLogsOutput.schema)
