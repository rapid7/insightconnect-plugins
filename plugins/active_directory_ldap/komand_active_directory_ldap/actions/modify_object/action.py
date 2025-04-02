import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import ModifyObjectInput, ModifyObjectOutput, Input, Output, Component


class ModifyObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_object",
            description=Component.DESCRIPTION,
            input=ModifyObjectInput(),
            output=ModifyObjectOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        attribute = params.get(Input.ATTRIBUTE_TO_MODIFY)
        attribute_value = params.get(Input.ATTRIBUTE_VALUE)
        # END INPUT BINDING - DO NOT REMOVE

        distinguished_name, _ = ADUtils.format_dn(distinguished_name)
        self.logger.info(f"Escaped DN {distinguished_name}")

        distinguished_name = ADUtils.escape_brackets_for_query(distinguished_name)
        self.logger.info(distinguished_name)

        try:
            return {
                Output.SUCCESS: self.connection.client.modify_object(
                    distinguished_name, attribute, attribute_value
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.modify_object(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    attribute,
                    attribute_value,
                )
            }
