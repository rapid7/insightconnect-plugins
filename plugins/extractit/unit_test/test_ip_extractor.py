from unittest import TestCase
from icon_extractit.actions.ip_extractor import IpExtractor
from icon_extractit.actions.ip_extractor.schema import Input, Output


class TestIpExtractor(TestCase):
    def test_extract_ips_from_string(self):
        action = IpExtractor()
        actual = action.run(
            {
                Input.STR: "0.0.0.0 255.255.255.255 198.51.100.100, 198.51.100.101, 198.51.100.100, 198.51.100.102 1.2.3.4 and 2001:db8:8:4::2 2001:0db8:85a3:0000:0000:8a2e:0370:7334 1762:0:0:0:0:B03:1:AF18 FE80:0000:0000:0000:0202:B3FF:FE1E:8329 are sample IP addresses"
            }
        )
        expected = {
            Output.IP_ADDRESSES: [
                "0.0.0.0",
                "255.255.255.255",
                "198.51.100.100",
                "198.51.100.101",
                "198.51.100.102",
                "1.2.3.4",
                "2001:db8:8:4::2",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "1762:0:0:0:0:B03:1:AF18",
                "FE80:0000:0000:0000:0202:B3FF:FE1E:8329",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_ips_from_string_bad(self):
        action = IpExtractor()
        actual = action.run(
            {Input.STR: "777.777.777.777 192.00.1.1 256.256.256.256 2001:0db8:85a03:0000:0000:8a2e:0370:7334"}
        )
        expected = {Output.IP_ADDRESSES: []}
        self.assertEqual(actual, expected)

    def test_extract_ips_from_file(self):
        action = IpExtractor()
        actual = action.run(
            {
                Input.FILE: "MC4wLjAuMCAyNTUuMjU1LjI1NS4yNTUgMTk4LjUxLjEwMC4xMDAsIDE5OC41MS4xMDAuMTAxLCAxOTguNTEuMTAwLjEwMCwgMTk4LjUxLjEwMC4xMDIgMS4yLjMuNCBhbmQgMjAwMTpkYjg6ODo0OjoyIDIwMDE6MGRiODo4NWEzOjAwMDA6MDAwMDo4YTJlOjAzNzA6NzMzNCAxNzYyOjA6MDowOjA6QjAzOjE6QUYxOCBGRTgwOjAwMDA6MDAwMDowMDAwOjAyMDI6QjNGRjpGRTFFOjgzMjkgYXJlIHNhbXBsZSBJUCBhZGRyZXNzZXM=",
            }
        )
        expected = {
            Output.IP_ADDRESSES: [
                "0.0.0.0",
                "255.255.255.255",
                "198.51.100.100",
                "198.51.100.101",
                "198.51.100.102",
                "1.2.3.4",
                "2001:db8:8:4::2",
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
                "1762:0:0:0:0:B03:1:AF18",
                "FE80:0000:0000:0000:0202:B3FF:FE1E:8329",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_ips_from_file_bad(self):
        action = IpExtractor()
        actual = action.run(
            {
                Input.FILE: "Nzc3Ljc3Ny43NzcuNzc3IDE5Mi4wMC4xLjEgMjU2LjI1Ni4yNTYuMjU2IDIwMDE6MGRiODo4NWEwMzowMDAwOjAwMDA6OGEyZTowMzcwOjczMzQ=",
            }
        )
        expected = {Output.IP_ADDRESSES: []}
        self.assertEqual(actual, expected)
