import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, Mock

from parameterized import parameterized

from icon_domaintools_phisheye.actions.domain_list import DomainList
from icon_domaintools_phisheye.actions.domain_list.schema import Input
from mock import (
    Util,
    mock_request_200,
    mocked_request,
)


class TestDomainList(TestCase):
    @patch("icon_domaintools_phisheye.connection.connection.Connection.connect", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DomainList())
        self.params_only_query = {Input.QUERY: "example"}

    @patch("icon_domaintools_phisheye.actions.domain_list.DomainList.run", side_effect=mock_request_200)
    def test_domain_list(self, mock_get):
        mocked_request(mock_get)
        response = self.action.run(self.params_only_query)
        expected = {
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

        self.assertEqual(response.json().get("data"), expected)
