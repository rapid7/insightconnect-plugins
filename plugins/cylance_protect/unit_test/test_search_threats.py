import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_cylance_protect.actions.search_threats.action import SearchThreats
from icon_cylance_protect.actions.search_threats.schema import SearchThreatsInput, SearchThreatsOutput
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from jsonschema import validate
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("icon_cylance_protect.util.api.CylanceProtectAPI.generate_token", side_effect=Util.mock_generate_token)
@patch("requests.request", side_effect=Util.mock_request)
class TestSearchThreats(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SearchThreats())

    @parameterized.expand(
        [
            [
                "valid_threat_search_md5",
                {
                    "threat_identifier": ["938c2cc0dcc05f2b68c4287040cfcf71"],
                    "score": -1,
                },
                {
                    "threats": [
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF71",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D80",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        }
                    ]
                },
            ],
            [
                "valid_threat_search_sha",
                {
                    "threat_identifier": ["5fedaebe1c409a201c01053fe95da99cf19f9999f0a5ca39be93de34488b9d80"],
                    "score": -1,
                },
                {
                    "threats": [
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF71",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D80",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        }
                    ]
                },
            ],
            [
                "valid_threat_search_both",
                {
                    "threat_identifier": [
                        "938c2cc0dcc05f2b68c4287040cfcf71",
                        "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D86",
                    ],
                    "score": -1,
                },
                {
                    "threats": [
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF71",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D80",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        },
                        {
                            "classification": "Malware",
                            "cylance_score": -1,
                            "file_size": 109395,
                            "global_quarantined": False,
                            "last_found": "2020-05-29T10:12:45",
                            "md5": "938C2CC0DCC05F2B68C4287040CFCF76",
                            "name": "honeyhashx86.exe",
                            "safelisted": False,
                            "sha256": "5FEDAEBE1C409A201C01053FE95DA99CF19F9999F0A5CA39BE93DE34488B9D86",
                            "sub_classification": "Exploit",
                            "unique_to_cylance": False,
                        },
                    ]
                },
            ],
        ]
    )
    def test_integration_search_threats_valid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        expected: dict,
    ):
        validate(input_params, SearchThreatsInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, SearchThreatsOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_threat_search",
                {
                    "threat_identifier": ["invalid"],
                    "score": -1,
                },
                "Threat not found.",
                "Unable to find any threats using identifier provided: invalid.",
            ],
            [
                "invalid_threat_search_bad_score",
                {
                    "threat_identifier": ["938c2cc0dcc05f2b68c4287040cfcf71"],
                    "score": 1,
                },
                "No threats matching the score found.",
                "Unable to find any threats using identifier and score provided.",
            ],
        ]
    )
    def test_integration_search_threats_invalid(
        self,
        _mock_request: MagicMock,
        _mock_generate_token: MagicMock,
        _test_name: str,
        input_params: dict,
        cause: str,
        assistance: str,
    ):
        validate(input_params, SearchThreatsInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
