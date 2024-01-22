import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase, mock
from unittest.mock import Mock
from komand_domaintools.actions.domain_search import DomainSearch
from komand_domaintools.actions.domain_search.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import logging

from parameterized import parameterized
from mock import (
    Util,
    mocked_action,
    mock_responder,
)

class TestDomainSearch(TestCase):
    @mock.patch("domaintools.API.domain_search", side_effect=mock_responder)
    def setUp(self, mock_post: Mock) -> None:
        self.action = Util.default_connector(DomainSearch())
        self.params = {Input.QUERY: "ETC"}

    @mock.patch("domaintools.API.domain_search", side_effect=mock_responder)
    def test_domain_search(self, mock_request):
        mocked_action(mock_request)
        response = self.action.run(self.params)
        expected = {}
        self.assertEqual(response, expected)

    @parameterized.expand(
        [
            (mock_responder, PluginException.causes[PluginException.Preset.BAD_REQUEST]),
            (mock_responder, PluginException.causes[PluginException.Preset.USERNAME_PASSWORD]),
            (mock_responder, PluginException.causes[PluginException.Preset.UNAUTHORIZED]),
            (mock_responder, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_responder, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
        ],
    )
    def test_domain_search_fail(self, mock_request, exception):
        mocked_action(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, exception)
