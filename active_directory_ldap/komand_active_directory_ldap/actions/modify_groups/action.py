import komand
from .schema import ModifyGroupsInput, ModifyGroupsOutput
# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import extend


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
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        dn = ','.join(temp_list)
        group_dn = params.get('group_dn')
        add_remove = params.get('add_remove')

        if add_remove == 'add':
            group = extend.ad_add_members_to_groups(conn, dn, group_dn)
        else:
            group = extend.ad_remove_members_from_groups(conn, dn, group_dn, fix=True)

        if group is False:
            self.logger.log("ModifyGroups: Unexpected result for group. Group was " + str(group))
            raise PluginException(PluginException.Preset.UNKNOWN)

        return {'success': group}
