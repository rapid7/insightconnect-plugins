import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_ise.actions.get_anc_endpoint import GetAncEndpoint
from icon_cisco_ise.actions.get_anc_endpoint.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import mock_request_200
from utils import Util

STUB_PAYLOAD = {Input.MAC: "00:11:22:33:44:55"}


class TestGetAncEndpoint(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetAncEndpoint())

    @parameterized.expand(
        [
            (STUB_PAYLOAD, {"macAddress": "00:11:22:33:44:55", "policyName": "policy1"}),
            ({Input.MAC: "11:22:33:44:55:66"}, {}),
        ]
    )
    @patch("requests.Session.get", side_effect=mock_request_200)
    def test_get_anc_endpoint(
        self, input_data: Dict[str, Any], expected: Dict[str, Any], mock_request_get: MagicMock
    ) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        expected = {Output.RESULTS: expected}
        self.assertEqual(response, expected)
        mock_request_get.assert_called()
