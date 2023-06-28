import sys
import os
from unittest.mock import patch
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_proofpoint_tap.util.exceptions import ApiException
from komand_proofpoint_tap.actions.fetch_forensics import FetchForensics
from unit_test.test_util import Util
from unittest import TestCase
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestFetchForensics(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(FetchForensics())

    @parameterized.expand(
        [
            [
                "fetch_forensics_with_threat_and_forensic",
                Util.read_file_to_dict("inputs/fetch_forensics_with_threat_and_forensic.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_with_threat_and_forensic.json.exp"),
            ],
            [
                "fetch_forensics_with_threat_without_forensic",
                Util.read_file_to_dict("inputs/fetch_forensics_with_threat_without_forensic.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_with_threat_without_forensic.json.exp"),
            ],
            [
                "fetch_forensics_with_campaign",
                Util.read_file_to_dict("inputs/fetch_forensics_with_campaign.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_with_campaign.json.exp"),
            ],
            [
                "fetch_forensics_blacklisted_as_boolean",
                Util.read_file_to_dict("inputs/fetch_forensics_blacklisted_as_boolean.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_blacklisted_as_boolean.json.exp"),
            ],
            [
                "fetch_forensics_blacklisted_as_integer",
                Util.read_file_to_dict("inputs/fetch_forensics_blacklisted_as_integer.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_blacklisted_as_integer.json.exp"),
            ],
            [
                "fetch_forensics_blacklisted_as_boolean_and_integer",
                Util.read_file_to_dict("inputs/fetch_forensics_blacklisted_as_boolean_and_integer.json.inp"),
                Util.read_file_to_dict("expected/fetch_forensics_blacklisted_as_boolean_and_integer.json.exp"),
            ],
        ]
    )
    def test_fetch_forensics(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "fetch_forensics_with_threat_and_campaign",
                Util.read_file_to_dict("inputs/fetch_forensics_two_parameters_bad.json.inp"),
                "Both Campaign ID and Threat ID were provided.",
                "Only one of the following two parameters can be used: Campaign ID or Threat ID.",
            ],
            [
                "fetch_forensics_no_parameters",
                Util.read_file_to_dict("inputs/fetch_forensics_no_parameters_bad.json.inp"),
                "One of the following inputs must be provided.",
                "Please enter either Threat ID or Campaign ID.",
            ],
        ]
    )
    def test_fetch_forensics_raise_plugin_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "fetch_forensics_threat_id_not_found",
                Util.read_file_to_dict("inputs/fetch_forensics_threat_id_not_found.json.inp"),
                "No results found.",
                "Please provide valid inputs and try again.",
            ],
            [
                "fetch_forensics_campaign_id_not_found",
                Util.read_file_to_dict("inputs/fetch_forensics_campaign_id_not_found.json.inp"),
                "No results found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_fetch_forensics_raise_api_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
