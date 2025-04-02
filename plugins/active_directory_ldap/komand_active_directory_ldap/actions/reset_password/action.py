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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        new_password = params.get(Input.NEW_PASSWORD)
        # END INPUT BINDING - DO NOT REMOVE

        distinguished_name = ADUtils.format_dn(distinguished_name)[0]
        distinguished_name = ADUtils.unescape_asterisk(distinguished_name)
        self.logger.info(f"Escaped DN {distinguished_name}")

        if self.connection.use_ssl is False:
            raise PluginException(
                cause="SSL must be enabled",
                assistance="SSL must be enabled for the reset password action",
            )

        try:
            return {
                Output.SUCCESS: self.connection.client.reset_password(
                    distinguished_name, new_password
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.reset_password(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    new_password,
                )
            }
