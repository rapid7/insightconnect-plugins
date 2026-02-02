import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.get_asset_software import GetAssetSoftware
from komand_rapid7_insightvm.actions.get_asset_software.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetAssetSoftware(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssetSoftware())

    @parameterized.expand(
        [
            [
                "found",
                5,
                {
                    "software": [
                        {
                            "description": "Adobe Flash 18.0.0.209",
                            "family": "Flash",
                            "id": 31,
                            "product": "Flash",
                            "type": "Internet Client",
                            "vendor": "Adobe",
                            "version": "18.0.0.209",
                        }
                    ]
                },
            ]
        ]
    )
    def test_get_asset_software(self, mock_get, name, asset_id, expected) -> None:
        actual = self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                6,
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
                "The resource does not exist or access is prohibited.",
            ]
        ]
    )
    def test_get_asset_software_bad(self, mock_get, name, asset_id, cause, assistance, data) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, data)
