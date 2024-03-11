import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_ise.actions.quarantine import Quarantine
from icon_cisco_ise.actions.quarantine.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import mock_request_200
from utils import Util

STUB_PAYLOAD = {Input.MAC_ADDRESS: "00:11:22:33:44:55", Input.POLICY: "ExamplePolicy"}


class TestQuarantine(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(Quarantine())

    @parameterized.expand(
        [
            (STUB_PAYLOAD, {"macAddress": "00:11:22:33:44:55", "policyName": "policy1"}),
        ]
    )
    @patch("requests.Session.put", side_effect=mock_request_200)
    @patch("requests.Session.get", side_effect=mock_request_200)
    def test_quarantine(
        self,
        input_data: Dict[str, Any],
        expected: Dict[str, Any],
        mock_request_put: MagicMock,
        mock_request_get: MagicMock,
    ) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        expected = {Output.ERS_ANC_ENDPOINT: expected}
        self.assertEqual(response, expected)
        mock_request_put.assert_called()
        mock_request_get.assert_called()
