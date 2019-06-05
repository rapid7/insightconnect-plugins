import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils


class Delete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Deletes the LDAP object specified',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        dn = ADUtils.dn_normalize(dn)
        temp_list = ADUtils.dn_escape_and_split(dn)
        dn = ','.join(temp_list)
        conn.delete(dn)
        result = conn.result
        output = result['description']

        if result['result'] == 0:
            return {'success': True}

        self.logger.error('failed: error message %s' % output)
        raise Exception('failed: error message %s' % output)
