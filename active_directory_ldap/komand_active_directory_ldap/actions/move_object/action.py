import komand
from .schema import MoveObjectInput, MoveObjectOutput
# Custom imports below
import re
from komand_active_directory_ldap.util.utils import ADUtils


class MoveObject(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='move_object',
                description='Move an Active Directory object from one organizational unit to another',
                input=MoveObjectInput(),
                output=MoveObjectOutput())

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        new_ou = params.get('new_ou')
        relative_dn = ''
        dn = formatter.format_dn(dn)[0]
        self.logger.info(f'Escaped DN {dn}')

        pattern = re.search(r'CN=[^,]*,', dn)
        self.logger.debug(pattern)
        if pattern:
            relative_dn = pattern.group()
            relative_dn = relative_dn[:-1]
            self.logger.debug(relative_dn)

        conn.modify_dn(dn, relative_dn, new_superior=new_ou)
        result = conn.result
        output = result['description']

        if result['result'] == 0:
            return {'success': True}

        self.logger.error('failed: error message %s' % output)
        return {'success': False}
