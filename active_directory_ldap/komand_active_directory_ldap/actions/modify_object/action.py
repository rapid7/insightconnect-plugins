import komand
from .schema import ModifyObjectInput, ModifyObjectOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils
from ldap3 import MODIFY_ADD, MODIFY_REPLACE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
from json import loads


class ModifyObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_object',
                description=Component.DESCRIPTION,
                input=ModifyObjectInput(),
                output=ModifyObjectOutput())

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get(Input.DISTINGUISHED_NAME)
        attribute = params.get(Input.ATTRIBUTE_TO_MODIFY)
        attribute_value = params.get(Input.ATTRIBUTE_VALUE)
        dn, search_base = formatter.format_dn(dn)
        self.logger.info(f'Escaped DN {dn}')

        pairs = formatter.find_parentheses_pairs(dn)
        # replace ( and ) when they are part of a name rather than a search parameter
        if pairs:
            dn = formatter.escape_brackets_for_query(dn)

        self.logger.info(dn)

        # Check that the distinguishedName is valid
        conn.search(search_base=search_base,
                    search_filter=f'(distinguishedName={dn})',
                    attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
        result = conn.response_to_json()
        result_list_object = loads(result)
        entries = result_list_object["entries"]

        dn_test = [d['dn'] for d in entries if 'dn' in d]
        if len(dn_test) == 0:
            self.logger.error('The DN ' + dn + ' was not found')
            raise PluginException(cause='The DN was not found.',
                                  assistance='The DN ' + dn + ' was not found')

        # Update attribute
        dn = formatter.unescape_asterisk(dn)
        conn.modify(dn, {attribute: [(MODIFY_REPLACE, [attribute_value])]})
        result = conn.result
        output = result['description']

        if result['result'] == 0:
            return {Output.SUCCESS: True}

        self.logger.error('failed: error message %s' % output)
        return {Output.SUCCESS: False}
