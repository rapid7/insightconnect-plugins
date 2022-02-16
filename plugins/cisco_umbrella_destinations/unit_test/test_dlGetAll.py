import sys
import os
from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from icon_cisco_umbrella_destinations.connection.connection import Connection
from icon_cisco_umbrella_destinations.actions.dlGetAll import DlGetAll
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cisco_umbrella_destinations.util.api import ERROR_MSG
import logging
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_403,
    mock_request_401,
    mock_request_500,
    mock_request_400,
    mock_request_404,
    mocked_request,
)


class TestDlGetAll(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = DlGetAll()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_success(self, mock_get):
        response = self.action.run()
        expected_response = {
            "success": {
                "status": {"code": 200, "text": "OK"},
                "meta": {"page": 1, "limit": 100, "total": 12},
                "data": [
                    {
                        "id": 5798992,
                        "organizationId": 2303280,
                        "access": "block",
                        "isGlobal": False,
                        "name": "Block For All",
                        "thirdpartyCategoryId": None,
                        "createdAt": "2020-05-19T20:58:55+0000",
                        "modifiedAt": "2020-05-19T21:11:15+0000",
                        "isMspDefault": False,
                        "markedForDeletion": False,
                        "bundleTypeId": 1,
                        "meta": {
                            "destinationCount": 0,
                            "domainCount": 0,
                            "urlCount": 0,
                            "ipv4Count": 0,
                            "applicationCount": 0,
                        },
                    },
                    {
                        "id": 1912718,
                        "organizationId": 2372338,
                        "access": "allow",
                        "isGlobal": True,
                        "name": "Global Allow List",
                        "thirdpartyCategoryId": None,
                        "createdAt": "2017-10-25T19:45:48+0000",
                        "modifiedAt": "2017-10-25T19:45:48+0000",
                        "isMspDefault": False,
                        "markedForDeletion": False,
                        "bundleTypeId": 1,
                        "meta": {
                            "destinationCount": 0,
                            "domainCount": 0,
                            "urlCount": 0,
                            "ipv4Count": 0,
                            "applicationCount": 0,
                        },
                    },
                    {
                        "id": 1912720,
                        "organizationId": 2372338,
                        "access": "block",
                        "isGlobal": True,
                        "name": "Global Block List",
                        "thirdpartyCategoryId": None,
                        "createdAt": "2017-10-25T19:45:48+0000",
                        "modifiedAt": "2017-10-25T19:45:48+0000",
                        "isMspDefault": False,
                        "markedForDeletion": False,
                        "bundleTypeId": 1,
                        "meta": {
                            "destinationCount": 0,
                            "domainCount": 0,
                            "urlCount": 0,
                            "ipv4Count": 0,
                            "applicationCount": 0,
                        },
                    },
                ],
            }
        }

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, ERROR_MSG),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
