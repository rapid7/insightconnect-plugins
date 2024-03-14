import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_ise.actions.query_endpoint import QueryEndpoint
from icon_cisco_ise.actions.query_endpoint.schema import Input, Output
from jsonschema import validate
from parameterized import parameterized

from mock import mock_request_200
from utils import Util

STUB_PAYLOAD = {Input.HOSTNAME: "ExampleHostname"}


class TestQueryEndpoint(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(QueryEndpoint())

    @parameterized.expand(
        [
            (
                STUB_PAYLOAD,
                {
                    "id": "id",
                    "name": "ExampleHostname",
                    "description": "description",
                    "mac": "00:01:02:03:04:05",
                    "profileId": "profileId",
                    "staticProfileAssignment": False,
                    "groupId": "groupId",
                    "staticGroupAssignment": True,
                    "portalUser": "portalUser",
                    "identityStore": "identityStore",
                    "identityStoreId": "identityStoreId",
                    "customAttributes": {"customAttributes": {"key1": "value1", "key2": "value2"}},
                    "mdmAttributes": {
                        "mdmServerName": "MdmServerName",
                        "mdmReachable": True,
                        "mdmEnrolled": False,
                        "mdmComplianceStatus": False,
                        "mdmOS": "",
                        "mdmManufacturer": "",
                        "mdmModel": "",
                        "mdmSerial": "",
                        "mdmEncrypted": False,
                        "mdmPinlock": False,
                        "mdmJailBroken": False,
                        "mdmIMEI": "",
                        "mdmPhoneNumber": "",
                    },
                },
            ),
        ]
    )
    @patch("requests.Session.get", side_effect=mock_request_200)
    def test_query_endpoint(
        self,
        input_data: Dict[str, Any],
        expected: Dict[str, Any],
        mock_request_get: MagicMock,
    ) -> None:
        response = self.action.run(input_data)
        validate(response, self.action.output.schema)
        expected = {Output.ERS_ENDPOINT: expected}
        self.assertEqual(response, expected)
        mock_request_get.assert_called()
