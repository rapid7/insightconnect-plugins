import komand
from .schema import EnableUserInput, EnableUserOutput
# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import MODIFY_REPLACE


class EnableUser(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='enable_user',
                description='Enable a account',
                input=EnableUserInput(),
                output=EnableUserOutput())

    def run(self, params={}):
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        dc_list = [s for s in temp_list if 'DC' in s]
        dc = ','.join(dc_list)
        escaped_dn = ','.join(temp_list)

        pairs = ADUtils.find_parentheses_pairs(escaped_dn)
        # replace ( and ) when they are part of a name rather than a search parameter
        if pairs:
            for key, value in pairs.items():
                tempstring = escaped_dn
                if tempstring.find('=', key, value) == -1:
                    escaped_dn = escaped_dn[:value] + '\\29' + escaped_dn[value + 1:]
                    escaped_dn = escaped_dn[:key] + '\\28' + escaped_dn[key + 1:]

        self.logger.info(escaped_dn)

        conn.search(search_base=dc,
                    search_filter=f'(distinguishedName={escaped_dn})',
                    attributes=['userAccountControl']
                    )
        results = conn.response
        dn_test = [d['dn'] for d in results if 'dn' in d]
        try:
            dn_test[0]
        except Exception as ex:
            self.logger.error('The DN ' + dn + ' was not found')
            raise PluginException(cause='The DN was not found',
                                  assistance='The DN ' + dn + ' was not found') from ex
        user_list = [d["attributes"] for d in results if "attributes" in d]
        user_control = user_list[0]
        try:
            account_status = user_control['userAccountControl']
        except Exception as ex:
            self.logger.error('The DN ' + dn + ' is not a user')
            raise PluginException(cause='The DN is not a user',
                                  assistance='The DN ' + dn + ' is not a user') from ex
        user_account_flag = 2
        account_status = account_status & ~user_account_flag

        conn.modify(escaped_dn, {'userAccountControl': [(MODIFY_REPLACE, [account_status])]})
        result = conn.result
        output = result['description']

        if result['result'] == 0:
            return {'success': True}

        self.logger.error('failed: error message %s' % output)
        return {'success': False}
