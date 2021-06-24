from unittest import TestCase
from icon_extractit.actions.mac_extractor import MacExtractor
from icon_extractit.actions.mac_extractor.schema import Input, Output


class TestMacExtractor(TestCase):
    def test_extract_mac_addresses_from_string(self):
        action = MacExtractor()
        actual = action.run(
            {Input.STR: "00:1B:44:11:3A:B7, 00:14:22:01:23:45, 00:a2:cc:01:2d:33 are example MAC addresses"}
        )
        expected = {Output.MAC_ADDRS: ["00:1B:44:11:3A:B7", "00:14:22:01:23:45", "00:a2:cc:01:2d:33"]}
        self.assertEqual(actual, expected)

    def test_extract_mac_addresses_from_file(self):
        action = MacExtractor()
        actual = action.run(
            {
                Input.FILE: "MDA6MUI6NDQ6MTE6M0E6QjcsIDAwOjE0OjIyOjAxOjIzOjQ1LCAwMDphMjpjYzowMToyZDozMyBhcmUgZXhhbXBsZSBNQUMgYWRkcmVzc2Vz",
            }
        )
        expected = {Output.MAC_ADDRS: ["00:1B:44:11:3A:B7", "00:14:22:01:23:45", "00:a2:cc:01:2d:33"]}
        self.assertEqual(actual, expected)

    def test_extract_mac_addresses_from_string_bad(self):
        action = MacExtractor()
        actual = action.run(
            {Input.STR: "100:1B:44:11:3A:B7, 00:14:222:01:23:45, 00:a2:gc:01:2d:33, 00:a2:ac::01:2d:33"}
        )
        expected = {Output.MAC_ADDRS: []}
        self.assertEqual(actual, expected)

    def test_extract_mac_addresses_from_file_bad(self):
        action = MacExtractor()
        actual = action.run(
            {
                Input.FILE: "MTAwOjFCOjQ0OjExOjNBOkI3LCAwMDoxNDoyMjI6MDE6MjM6NDUsIDAwOmEyOmdjOjAxOjJkOjMzLCAwMDphMjphYzo6MDE6MmQ6MzM="
            }
        )
        expected = {Output.MAC_ADDRS: []}
        self.assertEqual(actual, expected)
