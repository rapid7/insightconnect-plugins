import komand
from komand.exceptions import ConnectionTestException
from .schema import ConnectionSchema
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
        self.ssl = params.get('use_ssl')
        self.logger.info("Connecting to %s:%d" % (params['host'], params['port']))

        params['port'] = params.get('port') or 389

        use_ssl = False
        if params.get('use_ssl'):
            use_ssl = True

        server = ldap3.Server(
                host=params['host'],
                port=params['port'],
                use_ssl=use_ssl,
                get_info=ldap3.ALL)

        try:
            conn = ldap3.Connection(server=server,
                                    user=params.get('username_password').get('username'),
                                    password=params.get('username_password').get('password'),
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
                                        user=params.get('username_password').get('username'),
                                        password=params.get('username_password').get('password'),
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
            self.logger.info(f'Accessing LDAP with user {test}')
        except:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
