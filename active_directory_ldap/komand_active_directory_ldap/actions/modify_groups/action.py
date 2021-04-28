import komand
from .schema import ModifyGroupsInput, ModifyGroupsOutput, Input, Output

# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import extend
from ldap3.core.exceptions import LDAPException


class ModifyGroups(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_groups",
            description="Add or remove a user from AD groups",
            input=ModifyGroupsInput(),
            output=ModifyGroupsOutput(),
        )

    def run(self, params={}):
        conn = self.connection.conn
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

        # Check that dn exists in AD
        if not ADUtils.check_user_dn_is_valid(conn, dn, search_base):
            self.logger.error(f"The DN {dn} was not found")
            raise PluginException(cause="The DN was not found.", assistance=f"The DN {dn} was not found.")

        try:
            if add_remove == "add":
                group = extend.ad_add_members_to_groups(conn, dn, group_dn, fix=True, raise_error=True)
            else:
                group = extend.ad_remove_members_from_groups(conn, dn, group_dn, fix=True, raise_error=True)
        except LDAPException as e:
            raise PluginException(
                cause="Either the user or group distinguished name was not found.",
                assistance="Please check that the distinguished names are correct",
                data=e,
            )

        if group is False:
            self.logger.error(f"ModifyGroups: Unexpected result for group. Group was {str(group)}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        return {Output.SUCCESS: group}
