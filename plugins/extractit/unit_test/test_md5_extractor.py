from unittest import TestCase
from icon_extractit.actions.md5_extractor import Md5Extractor
from icon_extractit.actions.md5_extractor.schema import Input, Output


class TestMd5Extractor(TestCase):
    def test_extract_md5_from_string(self):
        action = Md5Extractor()
        actual = action.run(
            {Input.STR: "44d88612fea8a8f36de82e1278abb02f and 44D88612FEA8A8F36DE82E1278ABB02F are example MD5 hashes"}
        )
        expected = {Output.MD5: ["44d88612fea8a8f36de82e1278abb02f", "44D88612FEA8A8F36DE82E1278ABB02F"]}
        self.assertEqual(actual, expected)

    def test_extract_md5_from_file(self):
        action = Md5Extractor()
        actual = action.run(
            {
                Input.FILE: "NDRkODg2MTJmZWE4YThmMzZkZTgyZTEyNzhhYmIwMmYgYW5kIDQ0RDg4NjEyRkVBOEE4RjM2REU4MkUxMjc4QUJCMDJGIGFyZSBleGFtcGxlIE1ENSBoYXNoZXM=",
            }
        )
        expected = {Output.MD5: ["44d88612fea8a8f36de82e1278abb02f", "44D88612FEA8A8F36DE82E1278ABB02F"]}
        self.assertEqual(actual, expected)

    def test_extract_md5_from_string_bad(self):
        action = Md5Extractor()
        actual = action.run(
            {
                Input.STR: "44d88612fea8a8f36de82e1278abb02 and 44D88612FEA8A8F36DE82E1278ABB02FA are not example MD5 hashes"
            }
        )
        expected = {Output.MD5: []}
        self.assertEqual(actual, expected)

    def test_extract_md5_from_file_bad(self):
        action = Md5Extractor()
        actual = action.run(
            {
                Input.FILE: "NDRkODg2MTJmZWE4YThmMzZkZTgyZTEyNzhhYmIwMiBhbmQgNDREODg2MTJGRUE4QThGMzZERTgyRTEyNzhBQkIwMkZBIGFyZSBub3QgZXhhbXBsZSBNRDUgaGFzaGVz",
            }
        )
        expected = {Output.MD5: []}
        self.assertEqual(actual, expected)
