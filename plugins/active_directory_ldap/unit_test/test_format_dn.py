from unittest import TestCase

from komand_active_directory_ldap.util.utils import ADUtils
from parameterized import parameterized


class TestFormatDn(TestCase):
    @parameterized.expand(
        [
            ("CN=Jane Doe,OU=Users,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=Jane Doe,OU=Users,OU=NYDC,OU=Company,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=Jane Doe,OU=NYDC Admins,OU=NYDC,OU=Staff,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=Jane Doe,OU=DC Contractors,OU=Partners,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=Jane Doe,OU=Old DC servers,OU=Lab,DC=lab,DC=example,DC=com", "DC=lab,DC=example,DC=com"),
            ("CN=Doe\\, Jane,OU=NYDC,OU=Company,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=Jane Doe,OU=NYDC,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=JDCooper,OU=Users,DC=example,DC=com", "DC=example,DC=com"),
            ("CN=DC01,OU=Domain Controllers,DC=example,DC=com", "DC=example,DC=com"),
            # A "DC=" inside a value does not make the component a domain component
            ("CN=Jane Doe,OU=DC=Servers,OU=Company,DC=example,DC=com", "DC=example,DC=com"),
            ("cn=jane doe,ou=nydc,ou=company,dc=example,dc=com", "DC=example,DC=com"),
            # Attribute types are case-insensitive, and dn_normalize only uppercases an all-lowercase "dc="
            ("CN=Jane Doe,OU=Users,Dc=example,dC=com", "Dc=example,dC=com"),
        ]
    )
    def test_format_dn_search_base(self, dn: str, expected_search_base: str) -> None:
        _, search_base = ADUtils.format_dn(dn)
        self.assertEqual(expected_search_base, search_base)
