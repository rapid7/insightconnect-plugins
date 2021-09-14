from unittest import TestCase
from icon_extractit.actions.cve_extractor import CveExtractor
from icon_extractit.actions.cve_extractor.schema import Input, Output


class TestIocExtractor(TestCase):
    def test_extract_no_cve_from_string(self):
        action = CveExtractor()
        actual = action.run(
            {
                Input.STR: "user@example.com 198.51.100.100 44d88612fea8a8f36de82e1278abb02f http://example.com 10/10/2021 2001:db8:8:4::2 3395856ce81f2b7382dee72602f798b642f14140 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab 00:1B:44:11:3A:B7 /tmp/script",
            }
        )
        expected = {Output.CVES: []}
        self.assertEqual(actual, expected)

    def test_extract_no_cve_from_file(self):
        action = CveExtractor()
        actual = action.run(
            {
                Input.FILE: "dXNlckBleGFtcGxlLmNvbSAxOTguNTEuMTAwLjEwMCA0NGQ4ODYxMmZlYThhOGYzNmRlODJlMTI3OGFiYjAyZiBodHRwOi8vZXhhbXBsZS5jb20gMTAvMTAvMjAyMSAyMDAxOmRiODo4OjQ6OjIgMzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCAyNzVhMDIxYmJmYjY0ODllNTRkNDcxODk5ZjdkYjlkMTY2M2ZjNjk1ZWMyZmUyYTJjNDUzOGFhYmY2NTFmZDBmIGNjODA1ZDVmYWIxZmQ3MWE0YWIzNTJhOWM1MzNlNjVmYjJkNWI4ODU1MThmNGU1NjVlNjg4NDcyMjNiOGU2Yjg1Y2I0OGYzYWZhZDg0MjcyNmQ5OTIzOWM5ZTM2NTA1YzY0YjBkYzlhMDYxZDllNTA3ZDgzMzI3N2FkYTMzNmFiIDAwOjFCOjQ0OjExOjNBOkI3IC90bXAvc2NyaXB0",
            }
        )
        expected = {Output.CVES: []}
        self.assertEqual(actual, expected)

    def test_extract_cve_from_string(self):
        action = CveExtractor()
        actual = action.run(
            {
                Input.STR: "user@example.com 198.51.100.100 cve-1111-11111 cve-1111-111111 cve-1111-1111111 CVE-1111-11111 CVE-1111-111111 CVE-1111-1111111 /tmp/script",
            }
        )
        expected = {
            Output.CVES: [
                "cve-1111-11111",
                "cve-1111-111111",
                "cve-1111-1111111",
                "CVE-1111-11111",
                "CVE-1111-111111",
                "CVE-1111-1111111",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_cve_from_file(self):
        action = CveExtractor()
        actual = action.run(
            {
                Input.FILE: "dXNlckBleGFtcGxlLmNvbSAxOTguNTEuMTAwLjEwMCBjdmUtMTExMS0xMTExMSBjdmUtMTExMS0xMTExMTEgY3ZlLTExMTEtMTExMTExMSBDVkUtMTExMS0xMTExMSBDVkUtMTExMS0xMTExMTEgQ1ZFLTExMTEtMTExMTExMSAvdG1wL3NjcmlwdA==",
            }
        )
        expected = {
            Output.CVES: [
                "cve-1111-11111",
                "cve-1111-111111",
                "cve-1111-1111111",
                "CVE-1111-11111",
                "CVE-1111-111111",
                "CVE-1111-1111111",
            ]
        }
        self.assertEqual(actual, expected)
