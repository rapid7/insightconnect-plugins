import logging
from unittest import TestCase, mock

from icon_greynoise.actions.context_lookup import ContextLookup
from icon_greynoise.actions.ip_lookup import IpLookup

from test_ip_lookup import ip_response
from util import MockConnection


class TestContextLookup(TestCase):
    @mock.patch("greynoise.GreyNoise.ip", side_effect=ip_response)
    def test_context_lookup_calls_ip_lookup(self, _mock_get):
        log = logging.getLogger("Test")
        connection = MockConnection()
        params = {"ip_address": "1.2.3.4"}

        alias = ContextLookup()
        alias.connection = connection
        alias.logger = log

        lookup = IpLookup()
        lookup.connection = connection
        lookup.logger = log

        self.assertEqual(lookup.run(params), alias.run(params))
