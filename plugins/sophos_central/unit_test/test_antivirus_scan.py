import os
import sys
from unittest import TestCase, mock
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from unit_test.util import Util

from icon_sophos_central.actions.antivirus_scan import AntivirusScan

sys.path.append(os.path.abspath("../"))


class TestAntivirusScan(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.action = Util.default_connector(AntivirusScan())

    @patch("requests.request", side_effect=Util.mock_request)
    @patch("requests.request", side_effect=Util.mock_request)
    def test_antivirus_scan(self, mock_request_1, mock_request_2):
        input_params = Util.read_file_to_dict("inputs/get_endpoint_id.json.inp")
        expected = Util.read_file_to_dict("expected/antivirus_scan.json.exp")

        actual = self.action.run(input_params)

        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "Unauthorized.",
                "The client needs to authenticate before making the API call. "
                "Either your credentials are invalid or blacklisted,"
                " or your JWT authorization token has expired.",
                Util.mock_request_errors_401,
            ],
            [
                "Bad request.",
                "The API client sent a malformed request.",
                Util.mock_request_errors_400,
            ],
            [
                "Forbidden.",
                "The client has authenticated but doesn't have permission " "to perform the operation via the API.",
                Util.mock_request_errors_403,
            ],
            [
                "Not found.",
                "The requested resource wasn't found. The resource ID provided may be invalid, "
                "or the resource may have been deleted, or is no longer addressable.",
                Util.mock_request_errors_404,
            ],
            [
                "Conflict.",
                "Request made conflicts with an existing resource. Please check the API documentation "
                "or contact Support.",
                Util.mock_request_errors_409,
            ],
            [
                "Unavailable for Legal Reasons",
                "An example of a legal reason we can't serve an API is that the caller is located "
                "in a country where United States export control restrictions apply, "
                "and we are required by law not to handle such API calls.",
                Util.mock_request_errors_451,
            ],
        ]
    )
    def test_antivirus_scan_raise_exception(self, cause, assistance, mock_request_1):
        mock_function = requests
        mock_function.request = mock.Mock(side_effect=mock_request_1)

        input_parameters = Util.read_file_to_dict("inputs/get_endpoint_id.json.inp")
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
