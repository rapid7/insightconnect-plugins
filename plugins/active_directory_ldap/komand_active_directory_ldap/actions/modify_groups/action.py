import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import ModifyGroupsInput, ModifyGroupsOutput, Input, Output


class ModifyGroups(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_groups",
            description="Add or remove a user from AD groups",
            input=ModifyGroupsInput(),
            output=ModifyGroupsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        group_dn = params.get(Input.GROUP_DN)
        add_remove = params.get(Input.ADD_REMOVE)
        # END INPUT BINDING - DO NOT REMOVE

        # Normalize dn
        distinguished_name, search_base = ADUtils.format_dn(distinguished_name)
        distinguished_name = ADUtils.unescape_asterisk(distinguished_name)
        self.logger.info(f"Escaped DN {distinguished_name}")

        # Normalize group dn
        group_dn = ADUtils.format_dn(group_dn)[0]
        group_dn = ADUtils.unescape_asterisk(group_dn)
        self.logger.info(f"Escaped group DN {group_dn}")

        try:
            return {
                Output.SUCCESS: self.connection.client.modify_groups(
                    distinguished_name, search_base, add_remove, group_dn
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.modify_groups(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    search_base,
                    add_remove,
                    group_dn,
                )
            }
