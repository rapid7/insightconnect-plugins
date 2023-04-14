import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from unit_test.util import Util

from parameterized import parameterized

from icon_servicenow.actions.create_change_request.action import CreateChangeRequest
from icon_servicenow.actions.create_change_request.schema import Input
from typing import Dict, Any


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
