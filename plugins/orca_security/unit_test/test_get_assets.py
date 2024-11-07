import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_orca_security.actions.get_assets import GetAssets
from icon_orca_security.actions.get_assets.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetAssets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssets())

    @parameterized.expand(Util.load_parameters("get_assets").get("parameters"))
    def test_get_assets(
        self,
        mock_request,
        name,
        asset_id,
        cloud_provider_id,
        asset_type,
        asset_state,
        asset_label,
        internet_facing,
        region,
        vpc,
        score,
        severity,
        expected,
    ):
        actual = self.action.run(
            {
                Input.ASSET_UNIQUE_ID: asset_id,
                Input.CLOUD_PROVIDER_ID: cloud_provider_id,
                Input.ASSET_TYPE: asset_type,
                Input.ASSET_STATE: asset_state,
                Input.ASSET_LABELS: asset_label,
                Input.STATE_SCORE: score,
                Input.STATE_SEVERITY: severity,
                Input.INTERNET_FACING: internet_facing,
                Input.COMPUTE_REGIONS: region,
                Input.COMPUTE_VPCS: vpc,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("get_assets_bad").get("parameters"))
    def test_get_assets_bad(
        self,
        mock_request,
        name,
        asset_id,
        cloud_provider_id,
        asset_type,
        asset_state,
        asset_label,
        internet_facing,
        region,
        vpc,
        score,
        severity,
        cause,
        assistance,
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(
                {
                    Input.ASSET_UNIQUE_ID: asset_id,
                    Input.CLOUD_PROVIDER_ID: cloud_provider_id,
                    Input.ASSET_TYPE: asset_type,
                    Input.ASSET_STATE: asset_state,
                    Input.ASSET_LABELS: asset_label,
                    Input.STATE_SCORE: score,
                    Input.STATE_SEVERITY: severity,
                    Input.INTERNET_FACING: internet_facing,
                    Input.COMPUTE_REGIONS: region,
                    Input.COMPUTE_VPCS: vpc,
                }
            )
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
