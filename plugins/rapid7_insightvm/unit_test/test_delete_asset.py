import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.delete_asset import DeleteAsset
from komand_rapid7_insightvm.actions.delete_asset.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.delete", side_effect=Util.mocked_requests)
class TestDeleteAsset(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteAsset())

    @parameterized.expand([["found", 3, {"success": True}]])
    def test_delete_asset(self, mock_delete, name, asset_id, expected) -> None:
        actual = self.action.run({Input.ID: asset_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                4,
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
                "The resource does not exist or access is prohibited.",
            ]
        ]
    )
    def test_delete_asset_bad(self, mock_delete, name, asset_id, cause, assistance, data) -> None:
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ID: asset_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
