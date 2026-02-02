import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.actions.get_asset_vulnerabilities import GetAssetVulnerabilities
from komand_rapid7_insightvm.actions.get_asset_vulnerabilities.schema import Input
from parameterized import parameterized

from util import Util


@patch("aiohttp.client.ClientSession.request", side_effect=Util.mocked_async_requests)
@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetAssetVulnerabilities(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAssetVulnerabilities())

    @parameterized.expand(
        [
            [
                "found_without_risk_score",
                7,
                False,
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
            ],
            [
                "found_with_risk_score",
                7,
                True,
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
                            "riskScore": 849.0,
                        },
                    ]
                },
            ],
        ]
    )
    def test_get_asset_vulnerabilities(
        self, mock_get, mock_async_get, name, asset_id, get_risk_score, expected
    ) -> None:
        actual = self.action.run({Input.ASSET_ID: asset_id, Input.GET_RISK_SCORE: get_risk_score})
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
    def test_get_asset_vulnerabilities_bad(
        self, mock_get, mock_async_get, name, asset_id, cause, assistance, data
    ) -> None:
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.ASSET_ID: asset_id})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
