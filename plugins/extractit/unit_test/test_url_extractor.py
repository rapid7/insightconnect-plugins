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

    def test_extract_urls_from_string2(self):
        action = UrlExtractor()
        actual = action.run(
            {
                Input.STR: "http://example1.com/test_1 http://example2.com/test_1/ http://example3.com/test1_test2_(test3) http://example4.com/test1_test2_(test3)_(test4) http://www.example1.com/wpstyle/?p=364 https://www.example2.com/test/?test=exam&ple=42&quux http://✪df.ws/123 http://userid:password@example-5.com:8080 http://userid:password@example-6.com:8080/ http://userid@example5.com http://userid@example6.com/ http://userid@example7.com:8080 http://userid@example8.com:8080/ http://userid:password@example9.com http://userid:password@example0.com/ http://142.42.1.1/ http://142.42.1.2:8080/ http://➡.ws/䨹 http://⌘.ws http://⌘2.ws/ http://foo1.com/blah_(test)#cite-1 http://foo2.com/blah_(test)_blah#cite-1 http://foo3.com/unicode_(✪)_in_parens http://foo4.com/(something)?after=parens http://☺.test.com/ http://code.test2.com/events/#&product=browser http://j.mp ftp://foo-1.bar/baz http://foo-2.bar/?q=Test%20URL-encoded%20stuff http://例子.测试 http://1234.net http://a.b-c.de http://223.255.255.254 https://foo-bar.example.com/ http://test.com/auth/?=UserID&amp;userid=user@example.com www.test1.com test2.com 0.0.0.0 255.255.255.255 198.51.100.100 198.51.100.101 198.51.100.102 1.2.3.4 2001:db8:8:4::2 2001:0db8:85a3:0000:0000:8a2e:0370:7334 1762:0:0:0:0:B03:1:AF18 FE80:0000:0000:0000:0202:B3FF:FE1E:8329 user@example.com user1@example.com example_user@example.com example.user@example.com example-user@example.com example_user-1.test@test3.com example_user-1.test@example.example.example.example.com www.example-domain.com:8080 100.24.21.0 100.37.12.101"
            }
        )
        expected = {
            Output.URLS: [
                "http://example1.com/test_1",
                "http://example2.com/test_1/",
                "http://example3.com/test1_test2_(test3)",
                "http://example4.com/test1_test2_(test3)_(test4)",
                "http://www.example1.com/wpstyle/?p=364",
                "https://www.example2.com/test/?test=exam&ple=42&quux",
                "http://✪df.ws/123",
                "http://userid:password@example-5.com:8080",
                "http://userid:password@example-6.com:8080/",
                "http://userid@example5.com",
                "http://userid@example6.com/",
                "http://userid@example7.com:8080",
                "http://userid@example8.com:8080/",
                "http://userid:password@example9.com",
                "http://userid:password@example0.com/",
                "http://142.42.1.1/",
                "http://142.42.1.2:8080/",
                "http://➡.ws/䨹",
                "http://⌘.ws",
                "http://⌘2.ws/",
                "http://foo1.com/blah_(test)#cite-1",
                "http://foo2.com/blah_(test)_blah#cite-1",
                "http://foo3.com/unicode_(✪)_in_parens",
                "http://foo4.com/(something)?after=parens",
                "http://☺.test.com/",
                "http://code.test2.com/events/#&product=browser",
                "http://j.mp",
                "ftp://foo-1.bar/baz",
                "http://foo-2.bar/?q=Test%20URL-encoded%20stuff",
                "http://例子.测试",
                "http://1234.net",
                "http://a.b-c.de",
                "http://223.255.255.25",
                "https://foo-bar.example.com/",
                "http://test.com/auth/?=UserID&amp;userid=user@example.com",
                "www.test1.com",
                "test2.com",
                "www.example-domain.com:8080",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_urls_from_file2(self):
        action = UrlExtractor()
        actual = action.run(
            {
                Input.FILE: "aHR0cDovL2V4YW1wbGUxLmNvbS90ZXN0XzEgaHR0cDovL2V4YW1wbGUyLmNvbS90ZXN0XzEvIGh0dHA6Ly9leGFtcGxlMy5jb20vdGVzdDFfdGVzdDJfKHRlc3QzKSBodHRwOi8vZXhhbXBsZTQuY29tL3Rlc3QxX3Rlc3QyXyh0ZXN0MylfKHRlc3Q0KSBodHRwOi8vd3d3LmV4YW1wbGUxLmNvbS93cHN0eWxlLz9wPTM2NCBodHRwczovL3d3dy5leGFtcGxlMi5jb20vdGVzdC8/dGVzdD1leGFtJnBsZT00MiZxdXV4IGh0dHA6Ly/inKpkZi53cy8xMjMgaHR0cDovL3VzZXJpZDpwYXNzd29yZEBleGFtcGxlLTUuY29tOjgwODAgaHR0cDovL3VzZXJpZDpwYXNzd29yZEBleGFtcGxlLTYuY29tOjgwODAvIGh0dHA6Ly91c2VyaWRAZXhhbXBsZTUuY29tIGh0dHA6Ly91c2VyaWRAZXhhbXBsZTYuY29tLyBodHRwOi8vdXNlcmlkQGV4YW1wbGU3LmNvbTo4MDgwIGh0dHA6Ly91c2VyaWRAZXhhbXBsZTguY29tOjgwODAvIGh0dHA6Ly91c2VyaWQ6cGFzc3dvcmRAZXhhbXBsZTkuY29tIGh0dHA6Ly91c2VyaWQ6cGFzc3dvcmRAZXhhbXBsZTAuY29tLyBodHRwOi8vMTQyLjQyLjEuMS8gaHR0cDovLzE0Mi40Mi4xLjI6ODA4MC8gaHR0cDovL+KeoS53cy/kqLkgaHR0cDovL+KMmC53cyBodHRwOi8v4oyYMi53cy8gaHR0cDovL2ZvbzEuY29tL2JsYWhfKHRlc3QpI2NpdGUtMSBodHRwOi8vZm9vMi5jb20vYmxhaF8odGVzdClfYmxhaCNjaXRlLTEgaHR0cDovL2ZvbzMuY29tL3VuaWNvZGVfKOKcqilfaW5fcGFyZW5zIGh0dHA6Ly9mb280LmNvbS8oc29tZXRoaW5nKT9hZnRlcj1wYXJlbnMgaHR0cDovL+KYui50ZXN0LmNvbS8gaHR0cDovL2NvZGUudGVzdDIuY29tL2V2ZW50cy8jJnByb2R1Y3Q9YnJvd3NlciBodHRwOi8vai5tcCBmdHA6Ly9mb28tMS5iYXIvYmF6IGh0dHA6Ly9mb28tMi5iYXIvP3E9VGVzdCUyMFVSTC1lbmNvZGVkJTIwc3R1ZmYgaHR0cDovL+S+i+WtkC7mtYvor5UgaHR0cDovLzEyMzQubmV0IGh0dHA6Ly9hLmItYy5kZSBodHRwOi8vMjIzLjI1NS4yNTUuMjU0IGh0dHBzOi8vZm9vLWJhci5leGFtcGxlLmNvbS8gaHR0cDovL3Rlc3QuY29tL2F1dGgvPz1Vc2VySUQmYW1wO3VzZXJpZD11c2VyQGV4YW1wbGUuY29tIHd3dy50ZXN0MS5jb20gdGVzdDIuY29tIDAuMC4wLjAgMjU1LjI1NS4yNTUuMjU1IDE5OC41MS4xMDAuMTAwIDE5OC41MS4xMDAuMTAxIDE5OC41MS4xMDAuMTAyIDEuMi4zLjQgMjAwMTpkYjg6ODo0OjoyIDIwMDE6MGRiODo4NWEzOjAwMDA6MDAwMDo4YTJlOjAzNzA6NzMzNCAxNzYyOjA6MDowOjA6QjAzOjE6QUYxOCBGRTgwOjAwMDA6MDAwMDowMDAwOjAyMDI6QjNGRjpGRTFFOjgzMjkgdXNlckBleGFtcGxlLmNvbSB1c2VyMUBleGFtcGxlLmNvbSBleGFtcGxlX3VzZXJAZXhhbXBsZS5jb20gZXhhbXBsZS51c2VyQGV4YW1wbGUuY29tIGV4YW1wbGUtdXNlckBleGFtcGxlLmNvbSBleGFtcGxlX3VzZXItMS50ZXN0QHRlc3QzLmNvbSBleGFtcGxlX3VzZXItMS50ZXN0QGV4YW1wbGUuZXhhbXBsZS5leGFtcGxlLmV4YW1wbGUuY29tIHd3dy5leGFtcGxlLWRvbWFpbi5jb206ODA4MCAxMDAuMjQuMjEuMCAxMDAuMzcuMTIuMTAx",
            }
        )
        expected = {
            Output.URLS: [
                "http://example1.com/test_1",
                "http://example2.com/test_1/",
                "http://example3.com/test1_test2_(test3)",
                "http://example4.com/test1_test2_(test3)_(test4)",
                "http://www.example1.com/wpstyle/?p=364",
                "https://www.example2.com/test/?test=exam&ple=42&quux",
                "http://✪df.ws/123",
                "http://userid:password@example-5.com:8080",
                "http://userid:password@example-6.com:8080/",
                "http://userid@example5.com",
                "http://userid@example6.com/",
                "http://userid@example7.com:8080",
                "http://userid@example8.com:8080/",
                "http://userid:password@example9.com",
                "http://userid:password@example0.com/",
                "http://142.42.1.1/",
                "http://142.42.1.2:8080/",
                "http://➡.ws/䨹",
                "http://⌘.ws",
                "http://⌘2.ws/",
                "http://foo1.com/blah_(test)#cite-1",
                "http://foo2.com/blah_(test)_blah#cite-1",
                "http://foo3.com/unicode_(✪)_in_parens",
                "http://foo4.com/(something)?after=parens",
                "http://☺.test.com/",
                "http://code.test2.com/events/#&product=browser",
                "http://j.mp",
                "ftp://foo-1.bar/baz",
                "http://foo-2.bar/?q=Test%20URL-encoded%20stuff",
                "http://例子.测试",
                "http://1234.net",
                "http://a.b-c.de",
                "http://223.255.255.25",
                "https://foo-bar.example.com/",
                "http://test.com/auth/?=UserID&amp;userid=user@example.com",
                "www.test1.com",
                "test2.com",
                "www.example-domain.com:8080",
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
