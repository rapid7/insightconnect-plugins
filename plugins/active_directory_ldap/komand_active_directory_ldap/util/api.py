# pylint: disable=too-many-positional-arguments
import json
import subprocess  # noqa: B404
from functools import wraps
from json import loads
from typing import List

import ldap3
from ldap3 import MODIFY_REPLACE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
from ldap3 import extend
from ldap3.core.exceptions import LDAPBindError, LDAPAuthorizationDeniedResult, LDAPSocketOpenError, LDAPException
from ldap3.utils.log import set_library_log_detail_level, set_library_log_hide_sensitive_data, ERROR

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils


def with_connection(action):
    @wraps(action)
    def wrapper(self, *args, **kwargs):
        connection = None
        try:
            connection = self.establish_connection()
            result = action(self, connection, *args, **kwargs)
        finally:
            if connection:
                connection.unbind()
        return result

    return wrapper


class ActiveDirectoryLdapAPI:
    def __init__(
        self,
        logger=None,
        use_ssl=None,
        host=None,
        port=None,
        referrals=None,
        user_name=None,
        password=None,
        use_channel_binding=None,
        auth_type=None,
        kdc=None,
        domain_name=None,
    ):
        self.logger = logger
        self.use_ssl = use_ssl
        self.host = host
        self.port = port
        self.referrals = referrals
        self.user_name = user_name
        self.password = password
        self.use_channel_binding = use_channel_binding
        self.auth_type = auth_type or "Auto"
        self.kdc = kdc or ""
        self.domain_name = domain_name or ""

        set_library_log_detail_level(ERROR)
        set_library_log_hide_sensitive_data(True)

    def _resolve_kerberos_domain(self) -> str:
        """Resolve the Kerberos domain from connection settings or host FQDN."""
        if self.domain_name:
            return self.domain_name
        if "." in self.host:
            return self.host.split(".", 1)[1]
        raise PluginException(
            cause="Kerberos domain name is required.",
            assistance="Provide the domain name in the Kerberos connection settings "
            "(e.g., example.com) or ensure the host contains the full FQDN.",
        )

    def _write_krb5_config(self, upper_domain: str, kdc: str, domain: str):
        """Write /etc/krb5.conf with the Kerberos realm configuration."""
        krb5_config = (
            f"[libdefaults]\n"
            f"default_realm = {upper_domain}\n"
            f"forwardable = true\n"
            f"proxiable = true\n"
            f"dns_lookup_realm = false\n"
            f"dns_lookup_kdc = false\n"
            f"\n"
            f"[realms]\n"
            f"{upper_domain} = {{\n"
            f"kdc = {kdc}\n"
            f"admin_server = {kdc}\n"
            f"default_domain = {upper_domain}\n"
            f"}}\n"
            f"\n"
            f"[domain_realm]\n"
            f".{domain} = {upper_domain}\n"
            f"{domain} = {upper_domain}\n"
        )
        try:
            with open("/etc/krb5.conf", "w", encoding="utf-8") as krb5_file:
                krb5_file.write(krb5_config)
        except OSError as error:
            raise PluginException(
                cause="Failed to write Kerberos configuration.",
                assistance="Ensure the plugin container has write access to /etc/krb5.conf.",
                data=error,
            ) from error

    def _write_network_config(self, kdc: str, domain: str):
        """Write DNS and hosts configuration for Kerberos network resolution."""
        try:
            with open("/etc/resolv.conf", "w", encoding="utf-8") as resolv_file:
                resolv_file.write(f"search {domain}\nnameserver {kdc}\n")
        except OSError as error:
            raise PluginException(
                cause="Failed to write DNS configuration.",
                assistance="Ensure the plugin container has write access to /etc/resolv.conf.",
                data=error,
            ) from error

        try:
            with open("/etc/hosts", "a", encoding="utf-8") as hosts_file:
                hosts_file.write(f"\n{kdc} {self.host}\n")
        except OSError as error:
            self.logger.warning(f"Could not update /etc/hosts: {error}")

    def _acquire_kerberos_ticket(self, upper_domain: str, kdc: str, domain: str):
        """Acquire a Kerberos TGT via kinit using the provided credentials."""
        username = self.user_name
        if "\\" in username:
            username = username.split("\\", 1)[1]

        kinit_command = f"echo '{self.password}' | kinit {username}@{upper_domain}"
        with subprocess.Popen(
            kinit_command,
            shell=True,  # noqa: B602
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ) as process:
            stdout, stderr = process.communicate()

        if process.returncode != 0:
            self.logger.error(f"kinit failed - stdout: {stdout.decode('utf-8')}, stderr: {stderr.decode('utf-8')}")
            raise PluginException(
                cause="Failed to acquire Kerberos ticket.",
                assistance=f"Verify the KDC ({kdc}) is reachable and credentials are valid for domain {domain}. "
                f"Ensure the username does not include the domain prefix for Kerberos auth.",
                data=stderr.decode("utf-8"),
            )

    def _configure_kerberos(self):
        """
        Configure the container for Kerberos authentication at runtime.
        Writes /etc/krb5.conf, /etc/resolv.conf, and acquires a TGT via kinit.
        All configuration is derived from user-provided connection inputs.
        """
        domain = self._resolve_kerberos_domain()
        kdc = self.kdc if self.kdc else self.host
        upper_domain = domain.upper()

        self.logger.info(f"Configuring Kerberos: realm={upper_domain}, kdc={kdc}")

        self._write_krb5_config(upper_domain, kdc, domain)
        self._write_network_config(kdc, domain)
        self._acquire_kerberos_ticket(upper_domain, kdc, domain)

        self.logger.info("Kerberos ticket acquired successfully")

    def _connect_with_kerberos(self, server) -> ldap3.Connection:
        """
        Establish an LDAP connection using Kerberos (SASL GSSAPI) authentication.
        """
        self._configure_kerberos()
        try:
            conn = ldap3.Connection(
                server=server,
                authentication=ldap3.SASL,
                sasl_mechanism=ldap3.KERBEROS,
                auto_bind=True,
                auto_referrals=self.referrals,
            )
        except LDAPBindError as error:
            raise PluginException(
                cause="Kerberos LDAP bind failed.",
                assistance="Verify your Kerberos credentials and that the KDC is reachable.",
                data=error,
            ) from error
        except LDAPSocketOpenError as error:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=error) from error
        return conn

    def establish_connection(self) -> ldap3.Connection:
        """
        Connect to LDAP using the configured authentication method.
        """
        if not self.host.startswith("ldap://") and not self.host.startswith("ldaps://"):
            if self.use_ssl:
                self.host = f"ldaps://{self.host}"
            else:
                self.host = f"ldap://{self.host}"

        self.host = self.host_formatter(self.host)
        self.logger.info(f"Connecting to {self.host}:{self.port}")

        server = ldap3.Server(
            host=self.host,
            port=self.port,
            use_ssl=self.use_ssl,
            allowed_referral_hosts=[("*", True)],
            get_info=ldap3.ALL,
        )

        if self.auth_type == "Kerberos":
            conn = self._connect_with_kerberos(server)
        elif self.auth_type == "NTLM":
            conn = self._connect_with_ntlm_fallback(server)
        else:
            conn = self._connect_with_auto(server)

        self.logger.info("Connected!")
        return conn

    def _connect_with_ntlm_fallback(self, server) -> ldap3.Connection:
        """Attempt NTLM authentication, falling back to basic auth on failure."""
        try:
            return self.__connect_to_server(server, ldap3.NTLM)
        except LDAPException:
            self.logger.info("Failed to connect with NTLM, attempting basic auth")
            return self.__connect_to_server(server)

    def _connect_with_auto(self, server) -> ldap3.Connection:
        """Auto mode: try Kerberos first if configured, then fall back to NTLM."""
        if self.domain_name or self.kdc:
            try:
                conn = self._connect_with_kerberos(server)
                self.logger.info("Connected using Kerberos authentication")
                return conn
            except (PluginException, LDAPException) as error:
                self.logger.info(f"Kerberos authentication failed, falling back to NTLM: {error}")

        return self._connect_with_ntlm_fallback(server)

    def __connect_to_server(self, server, authentication=None) -> ldap3.Connection:
        try:
            connection_params = {
                "server": server,
                "user": self.user_name,
                "password": self.password,
                "auto_bind": True,
                "auto_referrals": self.referrals,
                "authentication": authentication,
            }

            if self.use_channel_binding and self.use_ssl:
                connection_params["channel_binding"] = ldap3.TLS_CHANNEL_BINDING

            conn = ldap3.Connection(**connection_params)
        except LDAPBindError as error:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=error)
        except LDAPAuthorizationDeniedResult as error:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=error)
        except LDAPSocketOpenError as error:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=error)
        return conn

    def host_formatter(self, host: str) -> str:
        """
        Formats the host as needed for the connection
        """
        colons = host.count(":")
        if colons > 0:
            host = host.split(":")
            if colons == 1:
                if host[1].find("//") != -1:
                    host = host[1][2:]
                else:
                    self.logger.info("Port was provided in hostname, using value from Port field instead")
                    host = host[0]
            elif colons == 2:
                self.logger.info("Port was provided in hostname, using value from Port field instead")
                host = host[1]
                if host.find("//") != -1:
                    host = host[2:]
            else:
                raise PluginException(
                    cause=f"There are too many colons ({colons}) in the host name ({host}).",
                    assistance="Check that the host name is correct",
                    data=host,
                )
        backslash = host.find("/")
        if backslash != -1:
            host = host[:backslash]
        return host

    @with_connection
    def add_user(self, conn, dn: str, user_account_control: int, ssl: bool, password: str, parameters: dict):
        try:
            conn.raise_exceptions = True
            conn.add(dn, ["person", "user"], parameters)
        except LDAPException as error:
            raise PluginException(
                cause="LDAP returned an error message.",
                assistance="Creating new user failed, error returned by LDAP.",
                data=error,
            )
        success = True

        if ssl:
            try:
                extend.ad_modify_password(conn, dn, password, None)
            except LDAPException:
                self.logger.error("User account created successfully, but unable to update the password.")
                success = False
        else:
            self.logger.info("Warning SSL is not enabled. User password can not be set. User account will be disabled")

        change_uac_attribute = {"userAccountControl": (MODIFY_REPLACE, [user_account_control])}
        conn.modify(dn, change_uac_attribute)
        self.logger.info(conn.result)

        return success

    @with_connection
    def delete(self, conn, dn: str):
        conn.delete(dn)
        result = conn.result
        output = result["description"]

        if result["result"] == 0:
            return True

        self.logger.error(f"failed: error message {output}")
        raise PluginException(
            cause=PluginException.causes[PluginException.Preset.UNKNOWN], assistance=f"failed: error message {output}"
        )

    @with_connection
    def manage_user(self, conn, dn: str, status: bool):
        return ADUtils.change_account_status(conn, dn, status, self.logger)

    @with_connection
    def manage_users(self, conn, dns: List[str], status: bool) -> dict:
        """
        manage_users handles disabling or enabling of a list of users, returning successes and failures.

        :param conn: Connection for LDAP
        :param dns: Distinguishes Names
        :param status: Whether user is enabled or disabled
        :return: Dictionary containing two lists, one for successfully modified Distinguishes Names and another for
        unsuccessfully modified Distinguishes Names and the cause of the failure
        """

        successes = []
        failures = []
        for dn in dns:
            try:
                ADUtils.change_account_status(conn, dn, status, self.logger)
                successes.append(dn)
            except Exception:
                try:
                    escaped_dn = ADUtils.escape_non_ascii_characters(dn)
                    ADUtils.change_account_status(conn, escaped_dn, status, self.logger)
                    successes.append(dn)
                except Exception as error:
                    failures.append({"dn": dn, "error": str(error)})
                    self.logger.error(f"Error: Failed to modify user {dn}")
        return {"successes": successes, "failures": failures}

    @with_connection
    def force_password_reset(self, conn, dn: str, password_expire: dict):
        try:
            conn.raise_exceptions = True
            conn.modify(dn=dn, changes=password_expire)
        except LDAPException as error:
            raise PluginException(
                cause="LDAP returned an error.",
                assistance="Error was returned when trying to force password reset for this user.",
                data=error,
            )

        return True

    @with_connection
    def modify_groups(self, conn, dn: str, search_base: str, add_remove: str, group_dn: tuple):
        # Check that dn exists in AD
        if not ADUtils.check_user_dn_is_valid(conn, dn, search_base):
            self.logger.error(f"The DN {dn} was not found")
            raise PluginException(
                cause="The DN was not found.",
                assistance=f"Please check that the specified DN {dn} is correct and try again.",
            )

        try:
            if add_remove == "add":
                group = extend.ad_add_members_to_groups(conn, dn, group_dn, fix=True, raise_error=True)
            else:
                group = extend.ad_remove_members_from_groups(conn, dn, group_dn, fix=True, raise_error=True)
        except LDAPException as error:
            raise PluginException(
                cause="Either the user or group distinguished name was not found.",
                assistance="Please check that the distinguished names are correct",
                data=error,
            )

        if group is False:
            self.logger.error(f"ModifyGroups: Unexpected result for group. Group was {str(group)}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        return group

    @with_connection
    def modify_object(self, conn, dn: str, attribute: str, attribute_value: str):
        conn.search(
            search_base=dn,
            search_filter="(objectClass=*)",
            attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES],
        )
        result = conn.response_to_json()
        result_list_object = loads(result)
        entries = result_list_object["entries"]

        dn_test = [d["dn"] for d in entries if "dn" in d]
        if len(dn_test) == 0:
            self.logger.error(f"The DN {dn} was not found")
            raise PluginException(
                cause="The DN was not found.",
                assistance=f"Please check that the specified DN {dn} is correct and try again.",
            )

        conn.modify(ADUtils().unescape_asterisk(dn), {attribute: [(MODIFY_REPLACE, [attribute_value])]})
        result = conn.result
        output = result["description"]

        if result["result"] == 0:
            return True

        self.logger.error(f"failed: error message {output}")
        return False

    @with_connection
    def move_object(self, conn, dn: str, relative_dn: str, new_ou: str):
        conn.modify_dn(dn, relative_dn, new_superior=new_ou)
        result = conn.result
        output = result["description"]

        if result["result"] == 0:
            return True

        self.logger.error(f"failed: error message {output}")
        return False

    @with_connection
    def query(self, conn, search_base: str, escaped_query: str, attributes):
        try:
            conn.extend.standard.paged_search(
                search_base=search_base,
                search_filter=escaped_query,
                attributes=attributes,
                paged_size=100,
                generator=False,
            )
            result_list_json = conn.response_to_json()
            result_list_object = json.loads(result_list_json)
            return result_list_object.get("entries")
        except Exception as error:
            raise PluginException(
                cause="Error occurred while running LDAP query",
                assistance="Check the error message for more information. If it's needed contact support for help.",
                data=str(error),
            )

    @with_connection
    def query_group_membership(self, conn, base: str, group_name: str, include_groups: str, expand_nested_groups: str):
        try:
            group = self.__search_data(conn, base=base, filter_query=f"(sAMAccountName={group_name})").get("entries")
            if group and isinstance(group, list):
                group_dn = group[0].get("dn")
            else:
                raise PluginException(
                    cause="The specified group was not found.",
                    assistance="Please check that the provided group name and search base are correct and try again.",
                )
            if include_groups and expand_nested_groups:
                query = f"(memberOf:1.2.840.113556.1.4.1941:={group_dn})"
            elif include_groups:
                query = f"(memberOf:={group_dn})"
            elif expand_nested_groups:
                query = f"(&(objectClass=user)(memberOf:1.2.840.113556.1.4.1941:={group_dn}))"
            else:
                query = f"(&(objectClass=user)(memberOf:={group_dn}))"
            entries = self.__search_data(conn, base=base, filter_query=query).get("entries")
            return entries
        except (AttributeError, IndexError) as error:
            raise PluginException(
                cause="LDAP returned unexpected response.",
                assistance="Check that the provided inputs are correct and try again. If the issue persists please "
                "contact support.",
                data=error,
            )

    def __search_data(self, conn, base: str, filter_query: str) -> dict:
        conn.extend.standard.paged_search(
            search_base=base,
            search_filter=filter_query,
            attributes=[ldap3.ALL_ATTRIBUTES, ldap3.ALL_OPERATIONAL_ATTRIBUTES],
            paged_size=100,
            generator=False,
        )
        return json.loads(conn.response_to_json())

    @with_connection
    def reset_password(self, conn, dn: str, new_password: str):
        try:
            conn.raise_exceptions = True
            success = extend.ad_modify_password(conn, dn, new_password, old_password=None)
        except LDAPException as error:
            raise PluginException(
                cause="LDAP returned an error in the response.",
                assistance="LDAP failed to reset the password for this user",
                data=error,
            )

        return success

    @with_connection
    def unblock_user(self, conn, dn: str, user_flag: int):
        return ADUtils.change_useraccountcontrol_property(conn, dn, True, user_flag, self.logger)

    @with_connection
    def who_am_i(self, conn):
        conn.extend.standard.who_am_i()
