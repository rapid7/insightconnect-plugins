from unittest import TestCase
from icon_extractit.actions.uuid_extractor import UuidExtractor
from icon_extractit.actions.uuid_extractor.schema import Input, Output


class TestIocExtractor(TestCase):
    def test_extract_no_uuid_from_string(self):
        action = UuidExtractor()
        actual = action.run(
            {
                Input.STR: "user@example.com 198.51.100.100 aaaaaaaa-aaaa-ghij-aaaa-aaaaffffffff 44d88612fea8a8f36de82e1278abb02f http://example.com 10/10/2021 2001:db8:8:4::2 3395856ce81f2b7382dee72602f798b642f14140 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab 00:1B:44:11:3A:B7 /tmp/script",
            }
        )
        expected = {Output.UUIDS: []}
        self.assertEqual(actual, expected)

    def test_extract_no_uuid_from_file(self):
        action = UuidExtractor()
        actual = action.run(
            {
                Input.FILE: "dXNlckBleGFtcGxlLmNvbSAxOTguNTEuMTAwLjEwMCBhYWFhYWFhYS1hYWFhLWdoaWotYWFhYS1hYWFhZmZmZmZmZmYgNDRkODg2MTJmZWE4YThmMzZkZTgyZTEyNzhhYmIwMmYgaHR0cDovL2V4YW1wbGUuY29tIDEwLzEwLzIwMjEgMjAwMTpkYjg6ODo0OjoyIDMzOTU4NTZjZTgxZjJiNzM4MmRlZTcyNjAyZjc5OGI2NDJmMTQxNDAgMjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYWJmNjUxZmQwZiBjYzgwNWQ1ZmFiMWZkNzFhNGFiMzUyYTljNTMzZTY1ZmIyZDViODg1NTE4ZjRlNTY1ZTY4ODQ3MjIzYjhlNmI4NWNiNDhmM2FmYWQ4NDI3MjZkOTkyMzljOWUzNjUwNWM2NGIwZGM5YTA2MWQ5ZTUwN2Q4MzMyNzdhZGEzMzZhYiAwMDoxQjo0NDoxMTozQTpCNyAvdG1wL3NjcmlwdA==",
            }
        )
        expected = {Output.UUIDS: []}
        self.assertEqual(actual, expected)

    def test_extract_uuid_from_string(self):
        action = UuidExtractor()
        actual = action.run(
            {
                Input.STR: "user@example.com 198.51.100.100 11111111-1111-1111-1111-111111111111 1a2b3c4d-5e6f-7A8B-9C1D-2E3F4a5b6c7d aaaaaaaa-aaaa-aaaa-aaaa-aaaaffffffff aaaaaaaa-aaaa-ghij-aaaa-aaaaffffffff /tmp/script",
            }
        )
        expected = {
            Output.UUIDS: [
                "11111111-1111-1111-1111-111111111111",
                "1a2b3c4d-5e6f-7A8B-9C1D-2E3F4a5b6c7d",
                "aaaaaaaa-aaaa-aaaa-aaaa-aaaaffffffff",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_uuid_from_file(self):
        action = UuidExtractor()
        actual = action.run(
            {
                Input.FILE: "dXNlckBleGFtcGxlLmNvbSAxOTguNTEuMTAwLjEwMCAxMTExMTExMS0xMTExLTExMTEtMTExMS0xMTExMTExMTExMTEgMWEyYjNjNGQtNWU2Zi03QThCLTlDMUQtMkUzRjRhNWI2YzdkIGFhYWFhYWFhLWFhYWEtYWFhYS1hYWFhLWFhYWFmZmZmZmZmZiBhYWFhYWFhYS1hYWFhLWdoaWotYWFhYS1hYWFhZmZmZmZmZmYgL3RtcC9zY3JpcHQ=",
            }
        )
        expected = {
            Output.UUIDS: [
                "11111111-1111-1111-1111-111111111111",
                "1a2b3c4d-5e6f-7A8B-9C1D-2E3F4a5b6c7d",
                "aaaaaaaa-aaaa-aaaa-aaaa-aaaaffffffff",
            ]
        }
        self.assertEqual(actual, expected)
