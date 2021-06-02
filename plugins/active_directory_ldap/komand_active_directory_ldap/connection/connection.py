import komand
from komand.exceptions import ConnectionTestException, PluginException
from .schema import ConnectionSchema, Input

# Custom imports below
import ldap3
from ldap3.core.exceptions import *


class Connection(komand.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.ssl = None
        self.conn = None

    def connect(self, params={}):
        """
        Connect to LDAP
        """
        self.ssl = params.get(Input.USE_SSL)
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)
        referrals = params.get(Input.CHASE_REFERRALS)
        user_name = params.get(Input.USERNAME_PASSWORD).get("username")
        password = params.get(Input.USERNAME_PASSWORD).get("password")

        if not host.startswith("ldap://") and not host.startswith("ldaps://"):
            if self.ssl:
                host = f"ldaps://{host}"
            else:
                host = f"ldap://{host}"

        host = self.host_formatter(host)
        self.logger.info(f"Connecting to {host}:{port}")

        server = ldap3.Server(
            host=host, port=port, use_ssl=self.ssl, allowed_referral_hosts=[("*", True)], get_info=ldap3.ALL
        )

        try:
            conn = ldap3.Connection(
                server=server,
                user=user_name,
                password=password,
                auto_bind=True,
                auto_referrals=referrals,
                authentication=ldap3.NTLM,
            )
        except LDAPBindError as e:
            raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=e)
        except LDAPAuthorizationDeniedResult as e:
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=e)
        except LDAPSocketOpenError as e:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=e)
        except LDAPException:
            # An exception here is likely caused because the ldap server dose use NTLM
            # A basic auth connection will be tried instead
            self.logger.info("Failed to connect to the server with NTLM, attempting to connect with basic auth")
            try:
                conn = ldap3.Connection(
                    server=server, user=user_name, password=password, auto_referrals=referrals, auto_bind=True
                )
            except LDAPBindError as e:
                raise PluginException(preset=PluginException.Preset.USERNAME_PASSWORD, data=e)
            except LDAPAuthorizationDeniedResult as e:
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=e)
            except LDAPSocketOpenError as e:
                raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE, data=e)

        self.logger.info("Connected!")
        self.conn = conn

    def host_formatter(self, host: str) -> str:
        """
        Formats The host as needed for the connection
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

    def test(self):
        try:
            self.conn.extend.standard.who_am_i()
        except LDAPExtensionError as e:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=e)

        return {"connection": "successful"}
