import sys
import os

from unittest import TestCase
from komand_rapid7_insightappsec.actions.get_vulnerabilities import GetVulnerabilities
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.sessions.Session.get", side_effect=Util.mock_request)
class TestGetVulnerabilities(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetVulnerabilities())

    @parameterized.expand(
        [
            [
                "all_params",
                Util.read_file_to_dict("inputs/get_vulnerabilities_all_params.json.inp"),
                Util.read_file_to_dict("expected/get_vulnerabilities_all_params.json.exp"),
            ],
            [
                "no_params",
                Util.read_file_to_dict("inputs/get_vulnerabilities_no_params.json.inp"),
                Util.read_file_to_dict("expected/get_vulnerabilities_no_params.json.exp"),
            ],
        ]
    )
    def test_get_vulnerabilities(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
