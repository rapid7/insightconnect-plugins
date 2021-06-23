from unittest import TestCase
from icon_extractit.actions.sha1_extractor import Sha1Extractor
from icon_extractit.actions.sha1_extractor.schema import Input, Output


class TestSha1Extractor(TestCase):
    def test_extract_sha1_from_string(self):
        action = Sha1Extractor()
        actual = action.run(
            {
                Input.STR: "3395856ce81f2b7382dee72602f798b642f14140 and 3395856CE81F2B7382DEE72602F798B642F14140 are example SHA1 hashes"
            }
        )
        expected = {
            Output.SHA1: ["3395856ce81f2b7382dee72602f798b642f14140", "3395856CE81F2B7382DEE72602F798B642F14140"]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha1_from_file(self):
        action = Sha1Extractor()
        actual = action.run(
            {
                Input.FILE: "MzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MmYxNDE0MCBhbmQgMzM5NTg1NkNFODFGMkI3MzgyREVFNzI2MDJGNzk4QjY0MkYxNDE0MCBhcmUgZXhhbXBsZSBTSEExIGhhc2hlcw==",
            }
        )
        expected = {
            Output.SHA1: ["3395856ce81f2b7382dee72602f798b642f14140", "3395856CE81F2B7382DEE72602F798B642F14140"]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha1_from_string_bad(self):
        action = Sha1Extractor()
        actual = action.run(
            {
                Input.STR: "3395856ce81f2b7382dee72602f798b642 and 3395856CE81F2B7382DEE72602F798B642F14140BDC622 are not example SHA1 hashes"
            }
        )
        expected = {Output.SHA1: []}
        self.assertEqual(actual, expected)

    def test_extract_sha1_from_file_bad(self):
        action = Sha1Extractor()
        actual = action.run(
            {
                Input.FILE: "MzM5NTg1NmNlODFmMmI3MzgyZGVlNzI2MDJmNzk4YjY0MiBhbmQgMzM5NTg1NkNFODFGMkI3MzgyREVFNzI2MDJGNzk4QjY0MkYxNDE0MEJEQzYyMiBhcmUgbm90IGV4YW1wbGUgU0hBMSBoYXNoZXM=",
            }
        )
        expected = {Output.SHA1: []}
        self.assertEqual(actual, expected)
