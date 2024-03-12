import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_broadcom_symantec_endpoint_protection.actions.get_agent_details import GetAgentDetails
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestGetAgentDetails(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mock_request)
    def setUpClass(
        cls,
        mock_request,
    ) -> None:
        cls.action = Util.default_connector(GetAgentDetails())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/get_agent_details_success.json.inp"),
                Util.read_file_to_dict("expected/get_agent_details_success.json.exp"),
            ],
        ]
    )
    @patch("requests.sessions.Session.get", side_effect=Util.mock_request)
    def test_get_agent_details(self, test_name, input_params, expected, mock_request):
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(expected, actual)
