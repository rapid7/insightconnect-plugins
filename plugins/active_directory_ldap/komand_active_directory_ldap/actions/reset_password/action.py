import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import ResetPasswordInput, ResetPasswordOutput, Output, Input


class ResetPassword(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="reset_password",
            description="Reset a users password",
            input=ResetPasswordInput(),
            output=ResetPasswordOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        dn = params.get(Input.DISTINGUISHED_NAME)
        new_password = params.get(Input.NEW_PASSWORD)
        use_ssl = self.connection.use_ssl
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f"Escaped DN {dn}")

        if use_ssl is False:
            raise PluginException(
                cause="SSL must be enabled", assistance="SSL must be enabled for the reset password action"
            )
        return {Output.SUCCESS: self.connection.client.reset_password(dn, new_password)}
