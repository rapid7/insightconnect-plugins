import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_any_run.actions.get_history import GetHistory
from icon_any_run.actions.get_history.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetHistory(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetHistory())

    @parameterized.expand(Util.load_parameters("get_history").get("parameters"))
    def test_get_history(self, mock_request, name, team, skip, limit, expected):
        actual = self.action.run({Input.TEAM: team, Input.SKIP: skip, Input.LIMIT: limit})
        self.assertEqual(actual, expected)
