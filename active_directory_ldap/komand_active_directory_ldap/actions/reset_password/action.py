import komand
from .schema import ResetPasswordInput, ResetPasswordOutput
# Custom imports below
from komand.exceptions import PluginException
from ldap3 import extend
from komand_active_directory_ldap.util.utils import ADUtils


class ResetPassword(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='reset_password',
                description='Reset a users password',
                input=ResetPasswordInput(),
                output=ResetPasswordOutput())

    def run(self, params={}):
        formatter = ADUtils()
        dn = params.get('distinguished_name')
        new_password = params.get('new_password')
        conn = self.connection.conn
        ssl = self.connection.ssl
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f'Escaped DN {dn}')

        if ssl is False:
            raise PluginException(cause='SSL must be enabled',
                                  assistance='SSL must be enabled for the reset password action')

        success = extend.ad_modify_password(conn, dn, new_password, old_password=None)
        result = conn.result

        if success is False:
            raise PluginException(PluginException.Preset.UNKNOWN,
                                  data=result)

        return {'success': success}
