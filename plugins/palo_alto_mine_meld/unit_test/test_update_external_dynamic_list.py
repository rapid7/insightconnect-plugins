import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_palo_alto_mine_meld.actions.update_external_dynamic_list import UpdateExternalDynamicList
from icon_palo_alto_mine_meld.actions.update_external_dynamic_list.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestUpdateExternalDynamicList(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateExternalDynamicList())

    @parameterized.expand(
        [
            ["add_domain", "example.com", "domain_list_add", "Add", {"success": True}],
            ["remove_domain", "example.com", "domain_list_remove", "Remove", {"success": True}],
            ["add_ipv4", "1.1.1.1", "ipv4_list_add", "Add", {"success": True}],
            ["remove_ipv4", "1.1.1.1", "ipv4_list_remove", "Remove", {"success": True}],
            ["add_ipv6", "2001:db8:8:4::2", "ipv6_list_add", "Add", {"success": True}],
            ["remove_iv6", "2001:db8:8:4::2", "ipv6_list_remove", "Remove", {"success": True}],
            ["add_url", "https://example.com", "url_list_add", "Add", {"success": True}],
            ["remove_url", "https://example.com", "url_list_remove", "Remove", {"success": True}],
        ]
    )
    def test_update_external_dynamic_list(
        self, mock: MagicMock, name: str, indicator: str, list_name: str, operation: str, expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run({Input.INDICATOR: indicator, Input.LIST_NAME: list_name, Input.OPERATION: operation})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "already_added",
                "example.com",
                "domain_list_remove",
                "Add",
                "Duplicate indicator.",
                "Indicator already exists in domain_list_remove.",
            ],
            [
                "indicator_not_found",
                "example.com",
                "domain_list_add",
                "Remove",
                "Not exist.",
                "Indicator does not exist in domain_list_add.",
            ],
            [
                "invalid_indicator",
                "example",
                "domain_list_add",
                "Add",
                "The provided indicator example is invalid.",
                "The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
            ],
            [
                "invalid_indicator_domain",
                "example..com",
                "domain_list_add",
                "Add",
                "The provided indicator example..com is invalid.",
                "The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
            ],
            [
                "invalid_indicator_ipv4",
                "999.999.999.999",
                "ipv4_list_add",
                "Add",
                "The provided indicator 999.999.999.999 is invalid.",
                "The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
            ],
            [
                "invalid_indicator_ipv6",
                "2001:db8:8:40000::2",
                "ipv6_list_add",
                "Add",
                "The provided indicator 2001:db8:8:40000::2 is invalid.",
                "The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
            ],
            [
                "invalid_indicator_url",
                "httx://example.com",
                "url_list_add",
                "Add",
                "The provided indicator httx://example.com is invalid.",
                "The provided indicator must be a domain, IPv4 address, IPv6 address, or URL.",
            ],
        ]
    )
    def test_update_external_dynamic_list_bad(self, mock, name, indicator, list_name, operation, cause, assistance):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.INDICATOR: indicator, Input.LIST_NAME: list_name, Input.OPERATION: operation})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "invalid_external_dynamic_list",
                "example.com",
                "invalid_list",
                "Add",
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
                {"error": {"message": "Unknown config data file"}},
            ]
        ]
    )
    def test_update_external_dynamic_list_bad(
        self,
        mock: MagicMock,
        name: str,
        indicator: str,
        list_name: str,
        operation: str,
        cause: str,
        assistance: str,
        data: Dict[str, Any],
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run({Input.INDICATOR: indicator, Input.LIST_NAME: list_name, Input.OPERATION: operation})
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
        self.assertEqual(error.exception.data, str(data))
