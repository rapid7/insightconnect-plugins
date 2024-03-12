import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_broadcom_symantec_endpoint_protection.actions.quarantine import Quarantine
from util import Util
from unittest.mock import patch
from parameterized import parameterized


class TestQuarantine(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mock_request)
    def setUpClass(
        cls,
        mock_request,
    ) -> None:
        cls.action = Util.default_connector(Quarantine())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/quarantine_success.json.inp"),
                Util.read_file_to_dict("expected/quarantine_success.json.exp"),
            ],
        ]
    )
    @patch("requests.sessions.Session.post", side_effect=Util.mock_request)
    @patch("requests.sessions.Session.get", side_effect=Util.mock_request)
    def test_quarantine(self, test_name, input_params, expected, mock_get, mock_post):
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(expected, actual)
