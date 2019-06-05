import komand
from .schema import ForcePasswordResetInput, ForcePasswordResetOutput
# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils


class ForcePasswordReset(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='force_password_reset',
                description='Force a user to reset their password on next login',
                input=ForcePasswordResetInput(),
                output=ForcePasswordResetOutput())

    def run(self, params={}):
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        escaped_dn = ','.join(temp_list)

        password_expire = {"pwdLastSet": ('MODIFY_REPLACE', [0])}
        success = conn.modify(dn=escaped_dn, changes=password_expire)
        return {'success': success}
