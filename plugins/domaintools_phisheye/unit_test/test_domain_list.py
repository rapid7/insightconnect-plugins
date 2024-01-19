import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_domaintools_phisheye.actions.domain_list import DomainList
from icon_domaintools_phisheye.actions.domain_list.schema import Input, DomainListInput, DomainListOutput
from unit_test.mock import Util
from parameterized import parameterized
from jsonschema import validate


class TestDomainList(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(DomainList())

        self.params_only_query = {Input.QUERY: "example"}

    @parameterized.expand(
        [
            [
                "valid_query_with_days_back",
                {Input.QUERY: "example", Input.DAYS_BACK: 1},
                {
                    "date": "2016-11-01",
                    "domains": [
                        {
                            "Created Date": {},
                            "Domain": "appeltypoexample.com",
                            "IP Addresses": [{"Country Code": {}, "IPv4": {}}],
                            "Name Servers": "ns57.domaincontrol.com",
                            "Registrant Email": {},
                            "Registrar Name": {},
                            "Risk Score": 24,
                            "TLD": {},
                        }
                    ],
                    "term": "apple",
                }
            ]
        ]
    )
    def test_domain_list(self, _test_name: str, input_params: dict, expected: dict):
        validate(input_params, DomainListInput.schema)
        response = self.action.run(input_params)
        self.assertEqual(response, expected)
        validate(response, DomainListOutput)
