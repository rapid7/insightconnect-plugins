import os
import sys
from typing import Any

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_broadcom_symantec_endpoint_protection.actions.blacklist import Blacklist
from parameterized import parameterized

from util import Util


class TestBlacklist(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mock_request)
    def setUpClass(
        cls,
        mock_request: MagicMock,
    ) -> None:
        cls.action = Util.default_connector(Blacklist())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/blacklist_success.json.inp"),
                Util.read_file_to_dict("expected/blacklist_success.json.exp"),
            ],
        ]
    )
    @patch("aiohttp.ClientSession.post", side_effect=Util.async_mock_request)
    def test_blacklist(
        self, test_name: str, input_params: dict[str, Any], expected: dict[str, Any], mock_request: MagicMock
    ) -> None:
        actual = self.action.run(input_params)
        print(actual)
        self.assertEqual(expected, actual)
