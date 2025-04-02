import insightconnect_plugin_runtime

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import DeleteInput, DeleteOutput, Output, Input


class Delete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete",
            description="Deletes the LDAP object specified",
            input=DeleteInput(),
            output=DeleteOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        # END INPUT BINDING - DO NOT REMOVE

        distinguished_name = ADUtils.format_dn(distinguished_name)[0]
        distinguished_name = ADUtils.unescape_asterisk(distinguished_name)

        try:
            return {Output.SUCCESS: self.connection.client.delete(distinguished_name)}
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.delete(
                    ADUtils.escape_non_ascii_characters(distinguished_name)
                )
            }
