import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_ise.actions.remove_from_quarantine import RemoveFromQuarantine
from icon_cisco_ise.actions.remove_from_quarantine.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import mock_request_200
from utils import Util

STUB_PAYLOAD = {Input.MAC_ADDRESS: "22:33:44:55:66:77"}


class TestRemoveFromQuarantine(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(RemoveFromQuarantine())

    @parameterized.expand([(STUB_PAYLOAD, True)])
    @patch("requests.Session.put", side_effect=mock_request_200)
    @patch("requests.Session.get", side_effect=mock_request_200)
    def test_remove_from_quarantine(
        self,
        input_data: Dict[str, Any],
        expected: Dict[str, Any],
        mock_request_put: MagicMock,
        mock_request_get: MagicMock,
    ) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        expected = {Output.SUCCESS: expected}
        self.assertEqual(response, expected)
        mock_request_put.assert_called()
        mock_request_get.assert_called()
