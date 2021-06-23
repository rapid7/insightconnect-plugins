from unittest import TestCase
from icon_extractit.actions.url_extractor import UrlExtractor
from icon_extractit.actions.url_extractor.schema import Input, Output


class TestUrlExtractor(TestCase):
    def test_extract_urls_from_string(self):
        action = UrlExtractor()
        actual = action.run(
            {
                Input.STR: "test http://userid:password@example.com:8080/ http://www.example.com/wpstyle/?p=364 http://www.example.com http://例子.测试 http://example.com/auth/?=UserID&amp;userid=user@example.com www.example.com/awdawd/ www.example.com example.com"
            }
        )
        expected = {
            Output.URLS: [
                "http://userid:password@example.com:8080/",
                "http://www.example.com/wpstyle/?p=364",
                "http://www.example.com",
                "http://例子.测试",
                "http://example.com/auth/?=UserID&amp;userid=user@example.com",
                "www.example.com/awdawd/",
                "www.example.com",
                "example.com",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_urls_from_file(self):
        action = UrlExtractor()
        actual = action.run(
            {
                Input.FILE: "dGVzdCBodHRwOi8vdXNlcmlkOnBhc3N3b3JkQGV4YW1wbGUuY29tOjgwODAvIGh0dHA6Ly93d3cuZXhhbXBsZS5jb20vd3BzdHlsZS8/cD0zNjQgaHR0cDovL3d3dy5leGFtcGxlLmNvbSBodHRwOi8v5L6L5a2QLua1i+ivlSBodHRwOi8vZXhhbXBsZS5jb20vYXV0aC8/PVVzZXJJRCZhbXA7dXNlcmlkPXVzZXJAZXhhbXBsZS5jb20gd3d3LmV4YW1wbGUuY29tL2F3ZGF3ZC8gd3d3LmV4YW1wbGUuY29tIGV4YW1wbGUuY29t",
            }
        )
        expected = {
            Output.URLS: [
                "http://userid:password@example.com:8080/",
                "http://www.example.com/wpstyle/?p=364",
                "http://www.example.com",
                "http://例子.测试",
                "http://example.com/auth/?=UserID&amp;userid=user@example.com",
                "www.example.com/awdawd/",
                "www.example.com",
                "example.com",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_urls_from_string_bad(self):
        action = UrlExtractor()
        actual = action.run({Input.STR: "http:// user@example.com 198.100.50.1"})
        expected = {Output.URLS: []}
        self.assertEqual(actual, expected)

    def test_extract_urls_from_file_bad(self):
        action = UrlExtractor()
        actual = action.run(
            {
                Input.FILE: "aHR0cDovLyB1c2VyQGV4YW1wbGUuY29tIDE5OC4xMDAuNTAuMQ==",
            }
        )
        expected = {Output.URLS: []}
        self.assertEqual(actual, expected)
