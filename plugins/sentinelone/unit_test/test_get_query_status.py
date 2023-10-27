import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.get_query_status import GetQueryStatus
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestGetQueryStatus(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetQueryStatus())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/get_query_status.json.inp"),
                Util.read_file_to_dict("expected/get_query_status.json.exp"),
            ]
        ]
    )
    def test_get_query_status(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_query_id",
                Util.read_file_to_dict("inputs/get_query_status_invalid_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ]
        ]
    )
    def test_get_query_status_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
