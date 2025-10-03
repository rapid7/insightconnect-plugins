from unittest import TestCase

from komand_palo_alto_pan_os.util.ip_check import IpCheck


class TestIpCheck(TestCase):
    def test_determine_address_type(self) -> None:
        ip_check = IpCheck()

        type_ = ip_check.determine_address_type("google.com")
        self.assertEqual("fqdn", type_)

        type_ = ip_check.determine_address_type("1.1.1.1")
        self.assertEqual("ip_address", type_)

        type_ = ip_check.determine_address_type("1.1.1.1/24")
        self.assertEqual("ip_range", type_)

        type_ = ip_check.determine_address_type("!@#$!@#$")
        self.assertEqual("unknown", type_)

        type_ = ip_check.determine_address_type("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
        self.assertEqual("ip_address", type_)

        type_ = ip_check.determine_address_type("123.com")
        self.assertEqual("fqdn", type_)

    def test_check_ip_in_range(self) -> None:
        ip_check = IpCheck()

        self.assertTrue(ip_check.check_ip_in_range("1.1.1.1", "1.1.1.0/24"))
        self.assertTrue(ip_check.check_ip_in_range("1.1.1.1", "1.0.0.0/8"))
        self.assertTrue(ip_check.check_ip_in_range("1.1.1.1", "1.1.1.1"))
        self.assertFalse(ip_check.check_ip_in_range("5.5.5.5", "1.1.1.1"))
        self.assertFalse(ip_check.check_ip_in_range("5.5.5.5", "1.1.1.1/24"))

    def test_check_address_against_object(self) -> None:
        ip_check = IpCheck()

        self.assertTrue(ip_check.check_address_against_object("1.1.1.0/24", "1.1.1.1"))
        self.assertTrue(ip_check.check_address_against_object("google.com", "google.com"))
        self.assertTrue(ip_check.check_address_against_object("1.1.1.1", "1.1.1.1"))
        self.assertTrue(
            ip_check.check_address_against_object(
                "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
            )
        )

        self.assertFalse(ip_check.check_address_against_object("1.1.1.0/24", "3.1.1.1"))
        self.assertFalse(ip_check.check_address_against_object("www.google.com", "google.com"))
        self.assertFalse(ip_check.check_address_against_object("!@#$!@#$", "!@#$!@#$"))
