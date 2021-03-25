import komand
from .schema import ForcePasswordResetInput, ForcePasswordResetOutput
from komand.exceptions import PluginException
# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3.core.exceptions import LDAPException


class ForcePasswordReset(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="force_password_reset",
            description="Force a user to reset their password on next login",
            input=ForcePasswordResetInput(),
            output=ForcePasswordResetOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get("distinguished_name")
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f"Escaped DN {dn}")

        password_expire = {"pwdLastSet": ("MODIFY_REPLACE", [0])}

        try:
            conn.raise_exceptions = True
            conn.modify(dn=dn, changes=password_expire)
        except LDAPException as e:
            raise PluginException(cause="LDAP returned an error.",
                                  assistance="Error was returned when trying to force password reset for this user.",
                                  data=e)

        return {"success": True}
