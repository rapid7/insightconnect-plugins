import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.create_ioc_threat import CreateIocThreat
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestCreateIocThreat(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(CreateIocThreat())

    @parameterized.expand(
        [
            [
                "only_required_inputs",
                Util.read_file_to_dict("inputs/create_ioc_threat.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "all_inputs",
                Util.read_file_to_dict("inputs/create_ioc_threat_2.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
        ]
    )
    def test_create_ioc_threat(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_agent_id",
                Util.read_file_to_dict("inputs/create_ioc_threat_invalid_agent_id.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please "
                "contact support.",
            ],
            [
                "invalid_hash",
                Util.read_file_to_dict("inputs/create_ioc_threat_invalid_hash.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please "
                "contact support.",
            ],
        ]
    )
    def test_create_ioc_threat_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
