import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.download_malicious_file import DownloadMaliciousFile
from icon_orca_security.actions.download_malicious_file.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
@patch("requests.get", side_effect=Util.mocked_requests)
class TestDownloadMaliciousFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DownloadMaliciousFile())

    @parameterized.expand(Util.load_parameters("download_malicious_file").get("parameters"))
    def test_download_malicious_file(self, mock_request, mock_get, name, alert_id, expected):
        actual = self.action.run({Input.ALERT_ID: alert_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("download_malicious_file_bad").get("parameters"))
    def test_download_malicious_file_bad(self, mock_request, mock_get, name, alert_id, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ALERT_ID: alert_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
