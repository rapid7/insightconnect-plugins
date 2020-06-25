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
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        group_dn = params.get('group_dn')
        add_remove = params.get('add_remove')

        # Normalize dn
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        dn = ','.join(temp_list)
        # Normalize group dn
        group_dn = ADUtils.dn_normalize(group_dn)
        temp_list = ADUtils.dn_escape_and_split(group_dn)
        group_dn = ','.join(temp_list)

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
