import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightvm.actions.list_inactive_assets import ListInactiveAssets
from komand_rapid7_insightvm.actions.list_inactive_assets.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestListInactiveAssets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListInactiveAssets())

    @parameterized.expand(
        [
            [
                "found",
                30,
                {
                    "assets": [
                        {
                            "addresses": [{"ip": "198.51.100.100", "mac": "00:00:00:00:00:00"}],
                            "assessedForPolicies": False,
                            "assessedForVulnerabilities": True,
                            "history": [
                                {"date": "2020-08-19T11:14:25.007Z", "scanId": 3, "type": "SCAN", "version": 1}
                            ],
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
                    ]
                },
            ],
            ["not_found", 10, {"assets": []}],
        ]
    )
    def test_get_asset(self, mock_get, name, days_ago, expected) -> None:
        actual = self.action.run({Input.DAYS_AGO: days_ago})
        self.assertEqual(actual, expected)
