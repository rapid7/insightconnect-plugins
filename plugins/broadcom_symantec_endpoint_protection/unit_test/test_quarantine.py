import os
import sys
from typing import Any

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_broadcom_symantec_endpoint_protection.actions.quarantine import Quarantine
from parameterized import parameterized

from util import Util


class TestQuarantine(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mock_request)
    def setUpClass(
        cls,
        mock_request: MagicMock,
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
    def test_quarantine(
        self,
        test_name: str,
        input_params: dict[str, Any],
        expected: dict[str, Any],
        mock_get: MagicMock,
        mock_post: MagicMock,
    ) -> None:
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(expected, actual)
