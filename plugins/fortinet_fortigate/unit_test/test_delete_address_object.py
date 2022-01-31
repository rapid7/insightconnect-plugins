import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.delete_address_object import DeleteAddressObject
from icon_fortinet_fortigate.actions.delete_address_object.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestDeleteAddressObject(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteAddressObject())

    @parameterized.expand(
        [
            [
                "delete_object_ipv4",
                "1.1.1.1",
                {
                    "success": True,
                    "response_object": {
                        "http_method": "DELETE",
                        "revision": "7740a1424b9e690e459c37fa209ab309",
                        "revision_changed": True,
                        "old_revision": "99faf4ed01eaa2e9ea2a0939b468c1df",
                        "mkey": "1.1.1.1",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "delete_object_ipv6",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                {
                    "success": True,
                    "response_object": {
                        "http_method": "DELETE",
                        "revision": "135705de48dac5b8417e4b95176c59c4",
                        "revision_changed": True,
                        "old_revision": "f922dec65c043c7e1e196e2e99d67bf8",
                        "mkey": "1111:2222:3333:4444:5555:6666:7777:8888",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address6",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "delete_object_domain",
                "test.com",
                {
                    "success": True,
                    "response_object": {
                        "http_method": "DELETE",
                        "revision": "47de64fb6bbc46f7e42e9d7c0046fe61",
                        "revision_changed": True,
                        "old_revision": "b9b80c92ba7aa603a6539274a4e03820",
                        "mkey": "test.com",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
        ]
    )
    def test_delete_address_object(self, mock_request, name, address_object, expected):
        actual = self.action.run(
            {
                Input.ADDRESS_OBJECT: address_object,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "address_object_not_found",
                "invalid_object",
                "Resource Not Found: Unable to find the specified resource.",
                "Data was requested but not found. Check that inputs are correct.",
                'Response was: {"message": "Not Found"}',
            ],
        ]
    )
    def test_delete_address_object_bad(self, mock_request, name, address_object, cause, assistance, data):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.ADDRESS_OBJECT: address_object,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
