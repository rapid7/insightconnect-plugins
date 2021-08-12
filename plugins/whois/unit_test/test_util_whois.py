from unittest import TestCase
from komand_whois.util import whois


class TestQuery(TestCase):
    def test_query(self):
        result = whois.query("stuff.com.br", ignore_returncode=1)
        result1 = whois.query("google.com.br", ignore_returncode=1)
        result2 = whois.query("www.google.com", ignore_returncode=1)
        result3 = whois.query("example.com.org", ignore_returncode=1)
        result4 = whois.query("rapid7.com", ignore_returncode=1)
        result5 = whois.query("google.lv", ignore_returncode=1)

        self.assertIsNotNone(result)
        self.assertIsNotNone(result1)
        self.assertIsNotNone(result2)
        self.assertIsNotNone(result3)
        self.assertIsNotNone(result4)
        self.assertIsNotNone(result5)
