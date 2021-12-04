import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.threats_fetch_file import ThreatsFetchFile
from komand_sentinelone.actions.threats_fetch_file.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unittest import TestCase


class TestThreatsFetchFile(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ThreatsFetchFile())

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_fail_when_password_too_short(self, mock_post, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.ID: "id",
                    Input.PASSWORD: "password",
                }
            )

        self.assertEqual("Wrong password.", error.exception.cause)
        self.assertEqual(
            "Password must have more than 10 characters and cannot contain whitespace.", error.exception.assistance
        )

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_fail_when_password_with_space(self, mock_post, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.ID: "id",
                    Input.PASSWORD: "pass word",
                }
            )

        self.assertEqual("Wrong password.", error.exception.cause)
        self.assertEqual(
            "Password must have more than 10 characters and cannot contain whitespace.", error.exception.assistance
        )
