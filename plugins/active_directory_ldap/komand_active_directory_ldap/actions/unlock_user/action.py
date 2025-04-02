import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.utils import UserAccountFlags, ADUtils
from .schema import UnlockUserInput, UnlockUserOutput, Input, Output, Component


class UnlockUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="unlock_user",
            description=Component.DESCRIPTION,
            input=UnlockUserInput(),
            output=UnlockUserOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {
                Output.SUCCESS: self.connection.client.unblock_user(
                    distinguished_name, UserAccountFlags.LOCKOUT
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.unblock_user(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    UserAccountFlags.LOCKOUT,
                )
            }
