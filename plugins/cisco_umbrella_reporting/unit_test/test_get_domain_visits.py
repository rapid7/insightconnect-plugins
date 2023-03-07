import sys
import os

sys.path.append(os.path.abspath("../"))

from parameterized import parameterized
from unittest import TestCase, mock
from icon_cisco_umbrella_reporting.connection.connection import Connection
from icon_cisco_umbrella_reporting.actions.get_domain_visits import GetDomainVisits
from insightconnect_plugin_runtime.exceptions import PluginException
import logging
from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_400,
    mock_request_401,
    mock_request_403,
    mock_request_404,
    mocked_request,
)


class TestGetDomainVisits(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("Connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = GetDomainVisits()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("Action logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_get_domain_visits(self, other_arg):
        response = self.action.run()
        expected_response = {'domain_visits': []}

        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [
            (mock_request_400, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_401, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_request_403, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
        ],
    )
    def test_not_ok(self, mock_request, exception):
        mocked_request(mock_request)

        with self.assertRaises(PluginException) as context:
            self.action.run()
        self.assertEqual(context.exception.cause, exception)
