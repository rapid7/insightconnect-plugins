import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_servicenow.actions.create_change_request.action import CreateChangeRequest
from icon_servicenow.actions.create_change_request.schema import Input
from parameterized import parameterized

from util import Util


class TestCreateChangeRequest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateChangeRequest())

    @parameterized.expand([({},), ({"short_description": "ExampleTest"})])
    @patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
    def test_create_change_request(self, additional_fields: Dict[str, Any], mock_post: MagicMock) -> None:
        actual = self.action.run({Input.ADDITIONAL_FIELDS: additional_fields})
        expected = {"success": True}
        self.assertEqual(actual, expected)
