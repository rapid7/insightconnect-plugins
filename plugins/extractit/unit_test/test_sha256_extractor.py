from unittest import TestCase
from icon_extractit.actions.sha256_extractor import Sha256Extractor
from icon_extractit.actions.sha256_extractor.schema import Input, Output


class TestSha256Extractor(TestCase):
    def test_extract_sha256_from_string(self):
        action = Sha256Extractor()
        actual = action.run(
            {
                Input.STR: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f and 275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F are example SHA256 hashes"
            }
        )
        expected = {
            Output.SHA256: [
                "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha256_from_file(self):
        action = Sha256Extractor()
        actual = action.run(
            {
                Input.FILE: "Mjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYWJmNjUxZmQwZiBhbmQgMjc1QTAyMUJCRkI2NDg5RTU0RDQ3MTg5OUY3REI5RDE2NjNGQzY5NUVDMkZFMkEyQzQ1MzhBQUJGNjUxRkQwRiBhcmUgZXhhbXBsZSBTSEEyNTYgaGFzaGVz",
            }
        )
        expected = {
            Output.SHA256: [
                "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                "275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0F",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_sha256_from_string_bad(self):
        action = Sha256Extractor()
        actual = action.run(
            {
                Input.STR: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aa and 275A021BBFB6489E54D471899F7DB9D1663FC695EC2FE2A2C4538AABF651FD0FBF651FD0F are not example SHA256 hashes"
            }
        )
        expected = {Output.SHA256: []}
        self.assertEqual(actual, expected)

    def test_extract_sha256_from_file_bad(self):
        action = Sha256Extractor()
        actual = action.run(
            {
                Input.FILE: "Mjc1YTAyMWJiZmI2NDg5ZTU0ZDQ3MTg5OWY3ZGI5ZDE2NjNmYzY5NWVjMmZlMmEyYzQ1MzhhYSBhbmQgMjc1QTAyMUJCRkI2NDg5RTU0RDQ3MTg5OUY3REI5RDE2NjNGQzY5NUVDMkZFMkEyQzQ1MzhBQUJGNjUxRkQwRkJGNjUxRkQwRiBhcmUgbm90IGV4YW1wbGUgU0hBMjU2IGhhc2hlcw==",
            }
        )
        expected = {Output.SHA256: []}
        self.assertEqual(actual, expected)
