import insightconnect_plugin_runtime

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import ForcePasswordResetInput, ForcePasswordResetOutput, Output, Input


class ForcePasswordReset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="force_password_reset",
            description="Force a user to reset their password on next login",
            input=ForcePasswordResetInput(),
            output=ForcePasswordResetOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        dn = params.get(Input.DISTINGUISHED_NAME)
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f"Escaped DN {dn}")
        password_expire = {"pwdLastSet": ("MODIFY_REPLACE", [0])}
        return {Output.SUCCESS: self.connection.client.force_password_reset(dn, password_expire)}
