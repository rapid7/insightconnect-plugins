import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightidr.actions.get_user_information import GetUserInformation
from komand_rapid7_insightidr.actions.get_user_information.schema import (
    Input,
    GetUserInformationInput,
    GetUserInformationOutput,
)
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetUserInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserInformation())

    @parameterized.expand(Util.load_parameters("get_user_information").get("parameters"))
    def test_get_user_information(self, mock_request, user_rrn, expected):
        test_input = {Input.USER_RRN: user_rrn}
        validate(test_input, GetUserInformationInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetUserInformationOutput.schema)

    @parameterized.expand(Util.load_parameters("get_user_information_bad").get("parameters"))
    def test_get_user_information_bad(self, mock_request, user_rrn, cause, assistance):
        test_input = {Input.USER_RRN: user_rrn}
        validate(test_input, GetUserInformationInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
