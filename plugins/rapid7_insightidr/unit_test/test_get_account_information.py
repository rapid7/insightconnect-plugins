import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.get_account_information import GetAccountInformation
from komand_rapid7_insightidr.actions.get_account_information.schema import (
    GetAccountInformationInput,
    GetAccountInformationOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetAccountInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAccountInformation())

    @parameterized.expand(Util.load_parameters("get_account_information").get("parameters"))
    def test_get_account_information(self, mock_request: MagicMock, account_rrn: str, expected: dict) -> None:
        test_input = {Input.ACCOUNT_RRN: account_rrn}
        validate(test_input, GetAccountInformationInput.schema)
        actual = self.action.run(test_input)
        self.assertCountEqual(actual, expected)
        validate(actual, GetAccountInformationOutput.schema)

    @parameterized.expand(Util.load_parameters("get_account_information_not_found").get("parameters"))
    def test_get_account_information_bad(
        self, mock_request: MagicMock, account_rrn: str, cause: str, assistance: str
    ) -> None:
        test_input = {Input.ACCOUNT_RRN: account_rrn}
        validate(test_input, GetAccountInformationInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
