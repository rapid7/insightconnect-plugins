import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import EnableUserInput, EnableUserOutput, Input, Output
from komand_active_directory_ldap.util.utils import ADUtils


class EnableUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="enable_user",
            description="Enable a account",
            input=EnableUserInput(),
            output=EnableUserOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            return {
                Output.SUCCESS: self.connection.client.manage_user(
                    distinguished_name, True
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.manage_user(
                    ADUtils.escape_non_ascii_characters(distinguished_name), True
                )
            }
