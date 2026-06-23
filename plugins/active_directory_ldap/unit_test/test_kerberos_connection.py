import logging
from unittest import TestCase, mock
from unittest.mock import MagicMock, mock_open, patch, call

import ldap3
from ldap3.core.exceptions import LDAPBindError, LDAPSocketOpenError, LDAPException
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.api import ActiveDirectoryLdapAPI

from common import MockConnection, MockServer

DEFAULT_KDC = "10.0.1.11"
DEFAULT_DOMAIN = "example.com"
DEFAULT_HOST = "dc01.example.com"


def create_api(logger, **overrides):
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


def mock_successful_kinit():
    """Return a mock Popen that simulates successful kinit execution."""
    mock_process = MagicMock()
    mock_process.communicate.return_value = (b"", b"")
    mock_process.returncode = 0
    mock_process.__enter__ = MagicMock(return_value=mock_process)
    mock_process.__exit__ = MagicMock(return_value=False)
    return mock_process


class TestKerberosConfiguration(TestCase):
    """Tests for Kerberos authentication configuration in the AD LDAP plugin."""

    def setUp(self):
        self.logger = logging.getLogger("test_kerberos")
        self.api = create_api(self.logger)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_writes_krb5_conf(self, mock_file, mock_popen):
        """Verify that _configure_kerberos writes a valid /etc/krb5.conf."""
        mock_popen.return_value = mock_successful_kinit()

        self.api._configure_kerberos()

        krb5_call = call("/etc/krb5.conf", "w", encoding="utf-8")
        self.assertIn(krb5_call, mock_file.call_args_list)

        written_content = "".join(call_args[0][0] for call_args in mock_file().write.call_args_list if call_args[0])
        self.assertIn("EXAMPLE.COM", written_content)
        self.assertIn(DEFAULT_KDC, written_content)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_writes_resolv_conf(self, mock_file, mock_popen):
        """Verify that _configure_kerberos writes DNS config pointing to the KDC."""
        mock_popen.return_value = mock_successful_kinit()

        self.api._configure_kerberos()

        resolv_call = call("/etc/resolv.conf", "w", encoding="utf-8")
        self.assertIn(resolv_call, mock_file.call_args_list)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_runs_kinit_with_correct_principal(self, mock_file, mock_popen):
        """Verify kinit is called with the correct username@REALM format, stripping DOMAIN\\ prefix."""
        mock_popen.return_value = mock_successful_kinit()

        self.api._configure_kerberos()

        kinit_command = mock_popen.call_args[0][0]
        self.assertIn("kinit svc_account@EXAMPLE.COM", kinit_command)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_kinit_failure_raises_plugin_exception(self, mock_file, mock_popen):
        """Verify that a kinit failure raises a PluginException with helpful messaging."""
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b"", b"kinit: Cannot contact any KDC for realm 'EXAMPLE.COM'")
        mock_process.returncode = 1
        mock_process.__enter__ = MagicMock(return_value=mock_process)
        mock_process.__exit__ = MagicMock(return_value=False)
        mock_popen.return_value = mock_process

        with self.assertRaises(PluginException) as context:
            self.api._configure_kerberos()

        self.assertIn("Failed to acquire Kerberos ticket", context.exception.cause)
        self.assertIn(DEFAULT_KDC, context.exception.assistance)

    def test_configure_kerberos_missing_domain_raises_exception(self):
        """Verify that missing domain and non-FQDN host raises a clear error."""
        api_no_domain = create_api(self.logger, host="dc01", domain_name="")

        with self.assertRaises(PluginException) as context:
            api_no_domain._configure_kerberos()

        self.assertIn("Kerberos domain name is required", context.exception.cause)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_derives_domain_from_host(self, mock_file, mock_popen):
        """When domain_name is empty but host is FQDN, domain should be derived from host."""
        mock_popen.return_value = mock_successful_kinit()

        api_derived = create_api(self.logger, host="dc01.corp.example.com", domain_name="", user_name="svc_account")
        api_derived._configure_kerberos()

        kinit_command = mock_popen.call_args[0][0]
        self.assertIn("kinit svc_account@CORP.EXAMPLE.COM", kinit_command)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_configure_kerberos_uses_host_as_kdc_when_kdc_not_provided(self, mock_file, mock_popen):
        """When KDC is not provided, the host should be used as the KDC."""
        mock_popen.return_value = mock_successful_kinit()

        api_no_kdc = create_api(self.logger, kdc="", user_name="svc_account")
        api_no_kdc._configure_kerberos()

        written_content = "".join(call_args[0][0] for call_args in mock_file().write.call_args_list if call_args[0])
        self.assertIn(DEFAULT_HOST, written_content)


class TestKerberosEstablishConnection(TestCase):
    """Tests for the establish_connection method with Kerberos auth type."""

    def setUp(self):
        self.logger = logging.getLogger("test_kerberos_connection")

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection")
    @patch("ldap3.Server")
    def test_kerberos_auth_type_uses_sasl_gssapi(self, mock_server, mock_connection, mock_configure):
        """Verify that Kerberos auth type creates a SASL/GSSAPI connection."""
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
    def test_ntlm_auth_type_does_not_configure_kerberos(self, mock_server, mock_connection, mock_configure):
        """Verify that NTLM auth type does not call Kerberos configuration."""
        mock_connection.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="NTLM")

        api.establish_connection()

        mock_configure.assert_not_called()

    @patch.object(ActiveDirectoryLdapAPI, "_connect_with_kerberos")
    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_auth_tries_kerberos_first_when_config_provided(self, mock_server, mock_ntlm_connect, mock_kerb):
        """Verify Auto mode attempts Kerberos first when kerberos config is present."""
        mock_kerb.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto")

        api.establish_connection()

        mock_kerb.assert_called_once()
        mock_ntlm_connect.assert_not_called()

    @patch.object(ActiveDirectoryLdapAPI, "_connect_with_kerberos")
    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_auth_falls_back_to_ntlm_on_kerberos_failure(self, mock_server, mock_ntlm_connect, mock_kerb):
        """Verify Auto mode falls back to NTLM when Kerberos fails."""
        mock_kerb.side_effect = PluginException(
            cause="Failed to acquire Kerberos ticket.", assistance="KDC unreachable."
        )
        mock_ntlm_connect.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto")

        api.establish_connection()

        mock_kerb.assert_called_once()
        self.assertTrue(mock_ntlm_connect.called)

    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_auto_auth_skips_kerberos_when_no_config(self, mock_server, mock_ntlm_connect):
        """Verify Auto mode skips Kerberos and goes straight to NTLM when no kerberos config."""
        mock_ntlm_connect.return_value = MagicMock()
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="Auto", kdc="", domain_name="")

        api.establish_connection()

        mock_ntlm_connect.assert_called()


class TestKerberosUsernameHandling(TestCase):
    """Tests for handling of username formats in Kerberos auth."""

    def setUp(self):
        self.logger = logging.getLogger("test_kerberos_username")

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_domain_backslash_prefix_stripped(self, mock_file, mock_popen):
        """Verify DOMAIN\\username format has the DOMAIN\\ stripped for kinit."""
        mock_popen.return_value = mock_successful_kinit()
        api = create_api(self.logger, user_name="EXAMPLE\\admin_user", password="password123")

        api._configure_kerberos()

        kinit_command = mock_popen.call_args[0][0]
        self.assertIn("kinit admin_user@EXAMPLE.COM", kinit_command)
        self.assertNotIn("EXAMPLE\\\\", kinit_command)

    @patch("subprocess.Popen")
    @patch("builtins.open", new_callable=mock_open)
    def test_plain_username_used_as_is(self, mock_file, mock_popen):
        """Verify plain username (no DOMAIN\\ prefix) is used directly."""
        mock_popen.return_value = mock_successful_kinit()
        api = create_api(self.logger, user_name="admin_user", password="password123")

        api._configure_kerberos()

        kinit_command = mock_popen.call_args[0][0]
        self.assertIn("kinit admin_user@EXAMPLE.COM", kinit_command)


class TestKerberosErrorHandling(TestCase):
    """Tests for error handling in Kerberos configuration and connection."""

    def setUp(self):
        self.logger = logging.getLogger("test_kerberos_errors")

    @patch("subprocess.Popen")
    @patch("builtins.open", side_effect=OSError("Permission denied"))
    def test_krb5_conf_write_failure_raises_plugin_exception(self, mock_file, mock_popen):
        """Verify OSError writing krb5.conf raises PluginException."""
        api = create_api(self.logger)

        with self.assertRaises(PluginException) as context:
            api._write_krb5_config("EXAMPLE.COM", DEFAULT_KDC, DEFAULT_DOMAIN)

        self.assertIn("Failed to write Kerberos configuration", context.exception.cause)

    @patch("builtins.open", side_effect=OSError("Permission denied"))
    def test_resolv_conf_write_failure_raises_plugin_exception(self, mock_file):
        """Verify OSError writing resolv.conf raises PluginException."""
        api = create_api(self.logger)

        with self.assertRaises(PluginException) as context:
            api._write_network_config(DEFAULT_KDC, DEFAULT_DOMAIN)

        self.assertIn("Failed to write DNS configuration", context.exception.cause)

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection", side_effect=LDAPBindError("Kerberos bind failed"))
    @patch("ldap3.Server")
    def test_kerberos_bind_error_raises_plugin_exception(self, mock_server, mock_conn, mock_configure):
        """Verify LDAPBindError during Kerberos connection raises PluginException."""
        api = create_api(self.logger, host="ldaps://dc01.example.com")

        with self.assertRaises(PluginException) as context:
            api._connect_with_kerberos(mock_server.return_value)

        self.assertIn("Kerberos LDAP bind failed", context.exception.cause)

    @patch.object(ActiveDirectoryLdapAPI, "_configure_kerberos")
    @patch("ldap3.Connection", side_effect=LDAPSocketOpenError("Connection refused"))
    @patch("ldap3.Server")
    def test_kerberos_socket_error_raises_service_unavailable(self, mock_server, mock_conn, mock_configure):
        """Verify LDAPSocketOpenError during Kerberos connection raises SERVICE_UNAVAILABLE."""
        api = create_api(self.logger, host="ldaps://dc01.example.com")

        with self.assertRaises(PluginException) as context:
            api._connect_with_kerberos(mock_server.return_value)

        self.assertIn("unavailable", context.exception.cause.lower())

    @patch.object(ActiveDirectoryLdapAPI, "_ActiveDirectoryLdapAPI__connect_to_server")
    @patch("ldap3.Server")
    def test_ntlm_fallback_to_basic_auth(self, mock_server, mock_connect):
        """Verify NTLM mode falls back to basic auth when NTLM fails."""
        mock_connect.side_effect = [LDAPException("NTLM not supported"), MagicMock()]
        api = create_api(self.logger, host="ldaps://dc01.example.com", auth_type="NTLM")

        api.establish_connection()

        self.assertEqual(mock_connect.call_count, 2)
