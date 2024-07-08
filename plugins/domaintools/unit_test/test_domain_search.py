import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_domaintools.actions.domain_search import DomainSearch
from komand_domaintools.actions.domain_search.schema import Input
from unit_test.util import mock_responder, Util


class TestDomainSearch(TestCase):
    @mock.patch("domaintools.API.account_information", side_effect=mock_responder)
    def setUp(self, mock_post) -> None:
        self.action = Util.default_connector(DomainSearch())
        self.params = {
            Input.QUERY: "example.com",
            Input.EXCLUDE_QUERY: "test.com",
            Input.MAX_LENGTH: 25,
            Input.MIN_LENGTH: 1,
            Input.HAS_HYPHEN: False,
            Input.HAS_NUMBER: False,
            Input.ACTIVE_ONLY: False,
            Input.DELETED_ONLY: False,
            Input.ANCHOR_LEFT: False,
            Input.ANCHOR_RIGHT: False,
            Input.PAGE: 1,
        }

    @mock.patch("domaintools.API.domain_search", side_effect=mock_responder)
    def test_domain_search(self, mock_request):
        response = self.action.run(self.params)
        expected = Util.load_expected("test_domain_search")
        self.assertEqual(response, expected)
