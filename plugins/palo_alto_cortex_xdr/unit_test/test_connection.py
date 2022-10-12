import os
import sys
from unittest import TestCase

sys.path.append(os.path.abspath("../"))

from icon_palo_alto_cortex_xdr.connection import Connection


class TestConnection(TestCase):
    def test_can_clean_fqdn(self):
        test_connection = Connection()

        test_fqdn = "www.google.com"
        actual = test_connection.clean_up_fqdn(test_fqdn)

        expected = "https://www.google.com/"
        self.assertEqual(expected, actual)

        test_fqdn = "https://www.google.com"
        actual = test_connection.clean_up_fqdn(test_fqdn)
        expected = "https://www.google.com/"

        self.assertEqual(expected, actual)

        test_fqdn = "https://www.google.com/"
        actual = test_connection.clean_up_fqdn(test_fqdn)
        expected = "https://www.google.com/"

        self.assertEqual(expected, actual)

        test_fqdn = "http://www.google.com"
        actual = test_connection.clean_up_fqdn(test_fqdn)
        expected = "http://www.google.com/"

        self.assertEqual(expected, actual)
