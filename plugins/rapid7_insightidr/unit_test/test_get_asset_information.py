import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.actions.get_asset_information import GetAssetInformation
from komand_rapid7_insightidr.actions.get_asset_information.schema import (
    GetAssetInformationInput,
    GetAssetInformationOutput,
    Input,
)
from parameterized import parameterized

from util import Util


@patch("requests.Session.send", side_effect=Util.mocked_requests)
class TestGetAssetInformation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssetInformation())

    @parameterized.expand(Util.load_parameters("get_asset_information").get("parameters"))
    def test_get_asset_information(self, mock_request, asset_rrn, expected) -> None:
        test_input = {Input.ASSET_RRN: asset_rrn}
        validate(test_input, GetAssetInformationInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, GetAssetInformationOutput.schema)

    @parameterized.expand(Util.load_parameters("get_asset_information_bad").get("parameters"))
    def test_get_asset_information_bad(self, mock_request, asset_rrn, cause, assistance) -> None:
        test_input = {Input.ASSET_RRN: asset_rrn}
        validate(test_input, GetAssetInformationInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(test_input)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
