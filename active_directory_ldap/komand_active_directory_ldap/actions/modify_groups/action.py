import komand
from .schema import ModifyGroupsInput, ModifyGroupsOutput
# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import extend
from ldap3.core.exceptions import *


class ModifyGroups(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_groups',
                description='Add or remove a user from AD groups',
                input=ModifyGroupsInput(),
                output=ModifyGroupsOutput())

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        group_dn = params.get('group_dn')
        add_remove = params.get('add_remove')

        # Normalize dn
        dn, search_base = formatter.format_dn(dn)
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f'Escaped DN {dn}')
        # Normalize group dn
        group_dn = formatter.format_dn(group_dn)[0]
        group_dn = formatter.unescape_asterisk(group_dn)
        self.logger.info(f'Escaped group DN {group_dn}')

        # Check that dn exists in AD
        self.check_that_user_dn_is_valid(conn, dn, search_base)

        if add_remove == 'add':
            try:
                group = extend.ad_add_members_to_groups(conn, dn, group_dn)
            except LDAPInvalidDnError as e:
                raise PluginException(cause='Either the user or group distinguished name was not found.',
                                      assistance='Please check that the distinguished names are correct',
                                      data=e)
        else:
            try:
                group = extend.ad_remove_members_from_groups(conn, dn, group_dn, fix=True)
            except LDAPInvalidDnError as e:
                raise PluginException(cause='Either the user or group distinguished name was not found.',
                                      assistance='Please check that the distinguished names are correct',
                                      data=e)

        if group is False:
            self.logger.error('ModifyGroups: Unexpected result for group. Group was ' + str(group))
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        return {'success': group}

    def check_that_user_dn_is_valid(self, conn, user_dn: str, search_base: str) -> None:
        formatter = ADUtils()
        pairs = formatter.find_parentheses_pairs(user_dn)
        # replace ( and ) when they are part of a name rather than a search parameter
        if pairs:
            user_dn = formatter.escape_brackets_for_query(user_dn, pairs)

        conn.search(search_base=search_base,
                    search_filter=f'(distinguishedName={user_dn})',
                    attributes=['userAccountControl']
                    )
        results = conn.response
        dn_test = [d['dn'] for d in results if 'dn' in d]
        try:
            dn_test[0]
        except Exception as ex:
            self.logger.error('The DN ' + user_dn + ' was not found')
            raise PluginException(cause='The DN was not found',
                                  assistance='The DN ' + user_dn + ' was not found') from ex