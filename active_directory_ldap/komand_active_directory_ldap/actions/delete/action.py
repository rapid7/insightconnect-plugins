import komand
from .schema import DeleteInput, DeleteOutput
# Custom imports below
from komand.exceptions import PluginException
from komand_active_directory_ldap.util.utils import ADUtils


class Delete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete',
                description='Deletes the LDAP object specified',
                input=DeleteInput(),
                output=DeleteOutput())

    def run(self, params={}):
        formatter = ADUtils()
        conn = self.connection.conn
        dn = params.get('distinguished_name')
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        conn.delete(dn)
        result = conn.result
        output = result['description']

        if result['result'] == 0:
            return {'success': True}

        self.logger.error('failed: error message %s' % output)
        raise PluginException(PluginException.Preset.UNKNOWN,
                              assistance='failed: error message %s' % output)
