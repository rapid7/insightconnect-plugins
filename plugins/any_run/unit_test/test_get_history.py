import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_any_run.actions.get_history import GetHistory
from icon_any_run.actions.get_history.schema import Input
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetHistory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetHistory())

    @parameterized.expand(Util.load_parameters("get_history").get("parameters"))
    def test_get_history(
        self, mock_request: MagicMock, name: str, team: str, skip: int, limit: int, expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run({Input.TEAM: team, Input.SKIP: skip, Input.LIMIT: limit})
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)
