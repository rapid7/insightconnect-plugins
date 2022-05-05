import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from komand_rapid7_insightvm.actions.get_asset_vulnerabilities import GetAssetVulnerabilities
from komand_rapid7_insightvm.actions.get_asset_vulnerabilities.schema import Input
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetAssetVulnerabilities(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssetVulnerabilities())

    @parameterized.expand(
        [
            [
                "found",
                7,
                {
                    "vulnerabilities": [
                        {
                            "id": "certificate-common-name-mismatch",
                            "instances": 1,
                            "links": [],
                            "results": [
                                {
                                    "port": 443,
                                    "proof": "<p><p>The subject common name found in the X.509 certificate does not seem to match the scan target:<ul><li>Subject CN observium does not match target name specified in the site.</li><li>Subject CN observium does not match DNS name specified in the site.</li><li>Subject CN observium could not be resolved to an IP address via DNS lookup</li><li>Subject Alternative Name observium does not match target name specified in the site.</li><li>Subject Alternative Name observium does not match DNS name specified in the site.</li></ul></p></p>",
                                    "protocol": "tcp",
                                    "since": "2020-08-18T20:39:17.369Z",
                                    "status": "vulnerable",
                                }
                            ],
                            "since": "2020-08-18T20:39:17.369Z",
                            "status": "vulnerable",
                        },
                    ]
                },
            ]
        ]
    )
    def test_get_asset(self, mock_get, name, asset_id, expected):
        actual = self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                8,
                "InsightVM returned an error message. Not Found",
                "Ensure that the requested resource exists.",
                "The resource does not exist or access is prohibited.",
            ]
        ]
    )
    def test_get_asset_bad(self, mock_get, name, asset_id, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
