from unittest import TestCase
from icon_extractit.actions.domain_extractor import DomainExtractor
from icon_extractit.actions.domain_extractor.schema import Input, Output


class TestDomainExtractor(TestCase):
    def test_extract_domains_from_string(self):
        action = DomainExtractor()
        actual = action.run({Input.STR: "www.example.com", Input.SUBDOMAIN: False})
        expected = {Output.DOMAINS: ["example.com"]}
        self.assertEqual(actual, expected)

    def test_extract_domains_from_file(self):
        action = DomainExtractor()
        actual = action.run({Input.FILE: "ZXhhbXBsZS5jb20gaXMgYW4gZXhhbXBsZSBkb21haW4=", Input.SUBDOMAIN: False})
        expected = {Output.DOMAINS: ["example.com"]}
        self.assertEqual(actual, expected)

    def test_extract_domains_without_subdomains(self):
        action = DomainExtractor()
        actual = action.run(
            {
                Input.STR: "www.example.com, http://test.example.com, www.yahoo.co.uk user@example.com test-ąćęłńóśżź.pl",
                Input.SUBDOMAIN: False,
            }
        )
        expected = {Output.DOMAINS: ["example.com", "yahoo.co.uk", "test-ąćęłńóśżź.pl"]}
        self.assertEqual(actual, expected)

    def test_extract_domains_with_subdomains(self):
        action = DomainExtractor()
        actual = action.run(
            {
                Input.STR: "http://www.example.com/document.html, www.google.com, https://example.domain.co.uk/test user@example.com test-ąćęłńóśżź.pl",
                Input.SUBDOMAIN: True,
            }
        )
        expected = {
            Output.DOMAINS: [
                "www.example.com",
                "www.google.com",
                "example.domain.co.uk",
                "example.com",
                "test-ąćęłńóśżź.pl",
            ]
        }
        self.assertEqual(actual, expected)

    def test_extract_domains_from_string_bad(self):
        action = DomainExtractor()
        actual = action.run({Input.STR: "domain.c www.exam_ple.com http://example!.com", Input.SUBDOMAIN: False})
        expected = {Output.DOMAINS: []}
        self.assertEqual(actual, expected)

    def test_extract_domains_from_file_bad(self):
        action = DomainExtractor()
        actual = action.run(
            {Input.FILE: "ZG9tYWluLmMgd3d3LmV4YW1fcGxlLmNvbSBodHRwOi8vZXhhbXBsZSEuY29t", Input.SUBDOMAIN: False}
        )
        expected = {Output.DOMAINS: []}
        self.assertEqual(actual, expected)
