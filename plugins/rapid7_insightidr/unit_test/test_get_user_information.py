import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_user_information import GetUserInformation
from komand_rapid7_insightidr.actions.get_user_information.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetUserInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserInformation())

    @parameterized.expand(Util.load_parameters("get_user_information").get("parameters"))
    def test_get_user_information(self, mock_request, user_rrn, expected):
        actual = self.action.run({Input.USER_RRN: user_rrn})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_user_information_bad").get("parameters"))
    def test_get_user_information_bad(self, mock_request, user_rrn, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.USER_RRN: user_rrn})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
