import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict, List
from unittest import TestCase

from icon_cisco_umbrella_reporting.util.utils import convert_get_domain_output, return_non_empty
from parameterized import parameterized

from mock import MockResponse


class TestUtils(TestCase):
    @parameterized.expand([(MockResponse("get_domain_visits", 200).json().get("data"),)])
    def test_extract_keys_from_dict(self, input_list_of_dict: List[Dict[str, Any]]) -> None:
        result = convert_get_domain_output(input_list_of_dict)
        expected = [
            {
                "externalIp": "255.255.255.255",
                "internalIp": "255.255.255.255",
                "categories": ["Malware"],
                "verdict": "allowed",
                "domain": "example.com",
                "datetime": "2019-01-24T06:31:46",
                "timestamp": 1548311506,
                "identities": [
                    {
                        "id": 1,
                        "label": "ExampleName",
                        "deleted": True,
                    }
                ],
                "threats": [{"label": "Wannacry", "type": "Ransomware"}],
                "allApplications": ["ExampleApp"],
                "allowedApplications": ["ExampleApp"],
                "queryType": "MX",
            }
        ]
        self.assertEqual(result, expected)

    @parameterized.expand(
        [({"test": 1, "test2": None}, {"test": 1}), ({"test": ["test"], "test2": []}, {"test": ["test"]})]
    )
    def test_return_non_empty(self, input_dict: Dict[str, Any], expected: Dict[str, Any]) -> None:
        result = return_non_empty(input_dict)
        self.assertEqual(result, expected)
