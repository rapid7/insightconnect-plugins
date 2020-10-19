import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input
# Custom imports below
import ldap3
from ldap3.core import exceptions


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Connect to LDAP
        """
        self.ssl = params.get(Input.USE_SSL)
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)
        user_name = params.get(Input.USERNAME_PASSWORD).get('username')
        password = params.get(Input.USERNAME_PASSWORD).get('password')

        host = self.host_formatter(host)
        self.logger.info(f'Connecting to {host}:{port}')

        server = ldap3.Server(
                host=host,
                port=port,
                use_ssl=self.ssl,
                get_info=ldap3.ALL)

        try:
            conn = ldap3.Connection(server=server,
                                    user=user_name,
                                    password=password,
                                    auto_encode=True,
                                    auto_escape=True,
                                    auto_bind=True,
                                    auto_referrals=False,
                                    authentication=ldap3.NTLM)
        except exceptions.LDAPBindError as e:
            self.logger.error(f'ldap3 returned the following error {e}')
            raise ConnectionTestException(preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
        except exceptions.LDAPAuthorizationDeniedResult as e:
            self.logger.error(f'ldap3 returned the following error {e}')
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        except exceptions.LDAPSocketOpenError as e:
            self.logger.error(f'ldap3 returned the following error {e}')
            raise ConnectionTestException(
                preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except:
            try:
                conn = ldap3.Connection(server=server,
                                        user=user_name,
                                        password=password,
                                        auto_referrals=False,
                                        auto_bind=True)
            except exceptions.LDAPBindError as e:
                self.logger.error(f'ldap3 returned the following error {e}')
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.USERNAME_PASSWORD)
            except exceptions.LDAPAuthorizationDeniedResult as e:
                self.logger.error(f'ldap3 returned the following error {e}')
                raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
            except exceptions.LDAPSocketOpenError as e:
                self.logger.error(f'ldap3 returned the following error {e}')
                raise ConnectionTestException(
                    preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)

        self.logger.info("Connected!")
        self.conn = conn

    def test(self):
        try:
            test = self.conn.extend.standard.who_am_i()
        except:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)

        return {'connection': 'successful'}

    def host_formatter(self, host: str) -> str:
        """
        Formats The host as needed for the connection
        """
        colons = host.count(':')
        if colons > 0:
            self.logger.info('Port was provided in hostname, using value from Port field instead')
            host = host.split(':')
            if colons == 1:
                host = host[0]
            elif colons == 2:
                host = f'{host[0]}:{host[1]}'
            else:
                raise ConnectionTestException(cause=f'There are too many colons ({colons}) in the host name ({host}).',
                                              assistance='Check that the host name is correct',
                                              data=host)
        return host
