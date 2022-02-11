import insightconnect_plugin_runtime

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import DeleteInput, DeleteOutput, Output, Input


class Delete(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete",
            description="Deletes the LDAP object specified",
            input=DeleteInput(),
            output=DeleteOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        dn = params.get(Input.DISTINGUISHED_NAME)
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        return {Output.SUCCESS: self.connection.client.delete(dn)}
