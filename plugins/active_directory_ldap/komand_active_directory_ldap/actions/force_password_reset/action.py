import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        distinguished_name = ADUtils.format_dn(distinguished_name)[0]
        distinguished_name = ADUtils.unescape_asterisk(distinguished_name)
        self.logger.info(f"Escaped DN {distinguished_name}")
        password_expire = {"pwdLastSet": ("MODIFY_REPLACE", [0])}

        try:
            return {
                Output.SUCCESS: self.connection.client.force_password_reset(
                    distinguished_name, password_expire
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.force_password_reset(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    password_expire,
                )
            }
