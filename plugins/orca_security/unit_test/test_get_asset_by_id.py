import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.get_asset_by_id import GetAssetById
from icon_orca_security.actions.get_asset_by_id.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetAssetById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssetById())

    @parameterized.expand(Util.load_parameters("get_asset_by_id").get("parameters"))
    def test_get_asset_by_id(self, mock_request, name, asset_id, expected):
        actual = self.action.run({Input.ASSET_UNIQUE_ID: asset_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_asset_by_id_bad").get("parameters"))
    def test_get_asset_by_id_bad(self, mock_request, name, asset_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ASSET_UNIQUE_ID: asset_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
