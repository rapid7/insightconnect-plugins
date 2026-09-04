import logging
import os
from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

import gssapi
import ldap3
from ldap3.core.exceptions import LDAPBindError, LDAPSocketOpenError, LDAPException
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.api import ActiveDirectoryLdapAPI

DEFAULT_KDC = "10.0.1.11"
DEFAULT_DOMAIN = "example.com"
DEFAULT_HOST = "dc01.example.com"


def create_api(logger: logging.Logger, **overrides: Any) -> ActiveDirectoryLdapAPI:
    """Create an ActiveDirectoryLdapAPI instance with sensible defaults for Kerberos tests."""
    defaults = {
        "use_ssl": True,
        "host": DEFAULT_HOST,
        "port": 636,
        "referrals": True,
        "user_name": "EXAMPLE\\svc_account",
        "password": "SecureP@ss123",
        "use_channel_binding": False,
        "auth_type": "Kerberos",
        "kdc": DEFAULT_KDC,
        "domain_name": DEFAULT_DOMAIN,
    }
    defaults.update(overrides)
    return ActiveDirectoryLdapAPI(logger=logger, **defaults)


def mock_temp_file(path: str = "/tmp/krb5.conf") -> MagicMock:
    """Return a mock NamedTemporaryFile supporting the context manager protocol."""
    mock_file = MagicMock()
    mock_file.name = path
    mock_file.__enter__ = MagicMock(return_value=mock_file)
    mock_file.__exit__ = MagicMock(return_value=False)
    return mock_file


class TestKerberosConfiguration(TestCase):
    """Tests for Kerberos configuration and credential acquisition."""

    def setUp(self) -> None:
        self.logger = logging.getLogger("test_kerberos")
        self.api = create_api(self.logger)

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_writes_krb5_to_temp_file_and_sets_env(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """Verify krb5.conf is written to a temp file and KRB5_CONFIG env var is set."""
        mock_tempfile.return_value = mock_temp_file("/tmp/test_krb5.conf")

        self.api._configure_kerberos()

        mock_tempfile.assert_called_once_with(mode="w", suffix=".conf", delete=False, encoding="utf-8")
        written_content = mock_tempfile.return_value.__enter__().write.call_args[0][0]
        self.assertIn("EXAMPLE.COM", written_content)
        self.assertIn(DEFAULT_KDC, written_content)
        self.assertEqual(os.environ.get("KRB5_CONFIG"), "/tmp/test_krb5.conf")

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_acquires_credentials_via_gssapi(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """Verify gssapi acquire_cred_with_password is called with correct principal and password."""
        mock_tempfile.return_value = mock_temp_file()

        self.api._configure_kerberos()

        mock_acquire.assert_called_once()
        name_arg = mock_acquire.call_args[0][0]
        password_arg = mock_acquire.call_args[0][1]
        self.assertEqual(str(name_arg), "svc_account@EXAMPLE.COM")
        self.assertEqual(password_arg, b"SecureP@ss123")

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_strips_domain_prefix_from_username(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """Verify DOMAIN\\username has the prefix stripped for the Kerberos principal."""
        mock_tempfile.return_value = mock_temp_file()
        api = create_api(self.logger, user_name="EXAMPLE\\admin_user")

        api._configure_kerberos()

        name_arg = mock_acquire.call_args[0][0]
        self.assertEqual(str(name_arg), "admin_user@EXAMPLE.COM")

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_plain_username_used_directly(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """Verify plain username (no DOMAIN\\ prefix) is used as-is."""
        mock_tempfile.return_value = mock_temp_file()
        api = create_api(self.logger, user_name="admin_user")

        api._configure_kerberos()

        name_arg = mock_acquire.call_args[0][0]
        self.assertEqual(str(name_arg), "admin_user@EXAMPLE.COM")

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_gssapi_failure_raises_plugin_exception(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """Verify gssapi GSSError raises PluginException with helpful messaging."""
        mock_tempfile.return_value = mock_temp_file()
        mock_acquire.side_effect = gssapi.exceptions.GSSError(851968, 0)

        with self.assertRaises(PluginException) as context:
            self.api._configure_kerberos()

        self.assertIn("Failed to acquire Kerberos credentials", context.exception.cause)

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_uses_host_as_kdc_when_kdc_empty(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """When KDC is not provided, the host should be used as the KDC in krb5.conf."""
        mock_tempfile.return_value = mock_temp_file()
        api = create_api(self.logger, kdc="")

        api._configure_kerberos()

        written_content = mock_tempfile.return_value.__enter__().write.call_args[0][0]
        self.assertIn(DEFAULT_HOST, written_content)

    @patch("komand_active_directory_ldap.util.api.acquire_cred_with_password")
    @patch("komand_active_directory_ldap.util.api.tempfile.NamedTemporaryFile")
    def test_derives_domain_from_fqdn_host(self, mock_tempfile: MagicMock, mock_acquire: MagicMock) -> None:
        """When domain_name is empty but host is FQDN, domain is derived from host."""
        mock_tempfile.return_value = mock_temp_file()
        api = create_api(self.logger, host="dc01.corp.example.com", domain_name="")

        api._configure_kerberos()

        written_content = mock_tempfile.return_value.__enter__().write.call_args[0][0]
        self.assertIn("CORP.EXAMPLE.COM", written_content)


class TestKerberosDomainResolution(TestCase):
    """Tests for domain resolution logic including IP address detection."""

    def setUp(self) -> None:
        self.logger = logging.getLogger("test_kerberos_domain")

    def test_ip_address_host_without_domain_raises_exception(self) -> None:
        """An IP host with no domain_name raises a clear error."""
        api = create_api(self.logger, host="10.0.1.11", domain_name="")

        with self.assertRaises(PluginException) as context:
            api._resolve_kerberos_domain()

        self.assertIn("IP address", context.exception.cause)

    def test_non_fqdn_host_without_domain_raises_exception(self) -> None:
        """A bare hostname with no domain_name raises an error."""
        api = create_api(self.logger, host="dc01", domain_name="")

        with self.assertRaises(PluginException) as context:
            api._resolve_kerberos_domain()

        self.assertIn("Kerberos domain name is required", context.exception.cause)

    def test_explicit_domain_name_takes_precedence(self) -> None:
        """Explicit domain_name takes precedence over host derivation."""
        api = create_api(self.logger, host="10.0.1.11", domain_name="corp.example.com")

        domain = api._resolve_kerberos_domain()

        self.assertEqual(domain, "corp.example.com")

    def test_fqdn_host_derives_domain(self) -> None:
        """FQDN host correctly derives the domain portion."""
        api = create_api(self.logger, host="dc01.tatooine.lab", domain_name="")

        domain = api._resolve_kerberos_domain()

        self.assertEqual(domain, "tatooine.lab")


class TestKerberosEstablishConnection(TestCase):
    """Tests for establish_connection with different auth types."""

    def setUp(self) -> None:
        self.logger = logging.getLogger("test_kerberos_connection")

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection")
    @patch("ldap3.Server")
    def test_kerberos_auth_uses_sasl_gssapi(
        self, mock_server: MagicMock, mock_connection: MagicMock, mock_configure: MagicMock
    ) -> None:
        """Kerberos auth type creates a SASL/GSSAPI connection."""
        mock_connection.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com")

        api.establish_connection()

        mock_configure.assert_called_once()
        mock_connection.assert_called_once_with(
            server=mock_server.return_value,
            authentication=ldap3.SASL,
            sasl_mechanism=ldap3.KERBEROS,
            auto_bind=True,
            auto_referrals=True,
        )

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection")
    @patch("ldap3.Server")
    def test_ntlm_auth_does_not_configure_kerberos(
        self, mock_server: MagicMock, mock_connection: MagicMock, mock_configure: MagicMock
    ) -> None:
        """NTLM auth type does not call Kerberos configuration."""
        mock_connection.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="NTLM")

        api.establish_connection()

        mock_configure.assert_not_called()

    @patch.object(ActiveDirectoryLdapAPI, "_connect_with_kerberos")
    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_mode_tries_kerberos_first(
        self, mock_server: MagicMock, mock_ntlm: MagicMock, mock_kerb: MagicMock
    ) -> None:
        """Auto mode attempts Kerberos first when config is present."""
        mock_kerb.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto")

        api.establish_connection()

        mock_kerb.assert_called_once()
        mock_ntlm.assert_not_called()

    @patch.object(ActiveDirectoryLdapAPI, "_connect_with_kerberos")
    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_mode_falls_back_to_ntlm(
        self, mock_server: MagicMock, mock_ntlm: MagicMock, mock_kerb: MagicMock
    ) -> None:
        """Auto mode falls back to NTLM when Kerberos fails."""
        mock_kerb.side_effect = PluginException(cause="Kerberos failed.", assistance="Check config.")
        mock_ntlm.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto")

        api.establish_connection()

        mock_kerb.assert_called_once()
        self.assertTrue(mock_ntlm.called)

    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_mode_skips_kerberos_when_no_config(self, mock_server: MagicMock, mock_ntlm: MagicMock) -> None:
        """Auto mode goes straight to NTLM when no kerberos config provided."""
        mock_ntlm.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto", kdc="", domain_name="")

        api.establish_connection()

        mock_ntlm.assert_called()


class TestKerberosErrorHandling(TestCase):
    """Tests for error paths in Kerberos connection flow."""

    def setUp(self) -> None:
        self.logger = logging.getLogger("test_kerberos_errors")

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection", side_effect=LDAPBindError("bind failed"))
    @patch("ldap3.Server")
    def test_ldap_bind_error_raises_plugin_exception(
        self, mock_server: MagicMock, mock_conn: MagicMock, mock_configure: MagicMock
    ) -> None:
        """LDAPBindError during Kerberos bind raises PluginException."""
        api = create_api(self.logger, host="ldaps://dc01.example.com")

        with self.assertRaises(PluginException) as context:
            api._connect_with_kerberos(mock_server.return_value)

        self.assertIn("Kerberos LDAP bind failed", context.exception.cause)

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection", side_effect=LDAPSocketOpenError("refused"))
    @patch("ldap3.Server")
    def test_socket_error_raises_service_unavailable(
        self, mock_server: MagicMock, mock_conn: MagicMock, mock_configure: MagicMock
    ) -> None:
        """LDAPSocketOpenError raises SERVICE_UNAVAILABLE."""
        api = create_api(self.logger, host="ldaps://dc01.example.com")

        with self.assertRaises(PluginException) as context:
            api._connect_with_kerberos(mock_server.return_value)

        self.assertIn("unavailable", context.exception.cause.lower())

    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_ntlm_fallback_to_basic_auth(self, mock_server: MagicMock, mock_connect: MagicMock) -> None:
        """NTLM mode falls back to basic auth when NTLM fails."""
        mock_connect.side_effect = [LDAPException("NTLM not supported"), MagicMock()]
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="NTLM")

        api.establish_connection()

        self.assertEqual(mock_connect.call_count, 2)
