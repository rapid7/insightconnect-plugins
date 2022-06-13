import insightconnect_plugin_runtime

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
        dn = params.get(Input.DISTINGUISHED_NAME)
        group_dn = params.get(Input.GROUP_DN)
        add_remove = params.get(Input.ADD_REMOVE)

        # Normalize dn
        dn, search_base = ADUtils.format_dn(dn)
        dn = ADUtils.unescape_asterisk(dn)
        self.logger.info(f"Escaped DN {dn}")
        # Normalize group dn
        group_dn = ADUtils.format_dn(group_dn)[0]
        group_dn = ADUtils.unescape_asterisk(group_dn)
        self.logger.info(f"Escaped group DN {group_dn}")

        return {Output.SUCCESS: self.connection.client.modify_groups(dn, search_base, add_remove, group_dn)}
