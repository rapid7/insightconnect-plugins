import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.get_asset import GetAsset
from komand_rapid7_insightvm.actions.get_asset.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetAsset(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAsset())

    @parameterized.expand(
        [
            [
                "found",
                1,
                {
                    "asset": {
                        "addresses": [{"ip": "198.51.100.100", "mac": "00:00:00:00:00:00"}],
                        "assessedForPolicies": False,
                        "assessedForVulnerabilities": True,
                        "history": [{"date": "2020-08-19T11:14:25.007Z", "scanId": 3, "type": "SCAN", "version": 1}],
                        "hostName": "example.com",
                        "hostNames": [{"name": "example.com", "source": "dns"}],
                        "id": 1,
                        "ip": "198.51.100.100",
                        "links": [],
                        "mac": "00:00:00:00:00:00",
                        "os": "Linux 3.2",
                        "osFingerprint": {},
                        "rawRiskScore": 0.0,
                        "riskScore": 0.0,
                        "services": [],
                        "vulnerabilities": {
                            "critical": 0,
                            "exploits": 0,
                            "malwareKits": 0,
                            "moderate": 2,
                            "severe": 0,
                            "total": 2,
                        },
                    }
                },
            ]
        ]
    )
    def test_get_asset(self, mock_get, name, asset_id, expected) -> None:
        actual = self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                2,
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
                "The resource does not exist or access is prohibited.",
            ]
        ]
    )
    def test_get_asset_bad(self, mock_get, name, asset_id, cause, assistance, data) -> None:
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
