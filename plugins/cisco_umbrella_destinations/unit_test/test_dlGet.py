import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.actions.dlGet.schema import Output
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.connection.schema import Input
from icon_cisco_umbrella_destinations.actions.dlGet import DlGet
import json
import logging

from ..unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mocked_request
)


class TestDlGet(TestCase):
    def test_dlGet(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlGet()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    # @mock.patch("requests.request", side_effect=mock_request_200)
    def test_destination_list_get_success(self):
        mocked_request(mock_request_200)
        response = self.action.run()
        expected_response = {
            "id": 15755711,
            "organizationId": 2372338,
            "access": "allow",
            "isGlobal": False,
            "name": "CreateListTest",
            "thirdpartyCategoryId": None,
            "createdAt": "2022-01-28T16:03:36+0000",
            "modifiedAt": "2022-02-02T14:04:29+0000",
            "isMspDefault": False,
            "markedForDeletion": False,
            "bundleTypeId": 1,
            "meta": {
                "destinationCount": 5
            }
        }
        self.assertEqual(response, expected_response)
