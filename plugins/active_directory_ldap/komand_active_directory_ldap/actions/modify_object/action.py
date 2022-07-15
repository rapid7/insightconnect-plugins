import insightconnect_plugin_runtime

# Custom imports below
from komand_active_directory_ldap.util.utils import ADUtils
from .schema import ModifyObjectInput, ModifyObjectOutput, Input, Output, Component


class ModifyObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_object",
            description=Component.DESCRIPTION,
            input=ModifyObjectInput(),
            output=ModifyObjectOutput(),
        )

    def run(self, params={}):
        formatter = ADUtils()
        dn = params.get(Input.DISTINGUISHED_NAME)
        attribute = params.get(Input.ATTRIBUTE_TO_MODIFY)
        attribute_value = params.get(Input.ATTRIBUTE_VALUE)
        dn, _ = formatter.format_dn(dn)
        self.logger.info(f"Escaped DN {dn}")

        dn = formatter.escape_brackets_for_query(dn)
        self.logger.info(dn)

        return {Output.SUCCESS: self.connection.client.modify_object(dn, attribute, attribute_value)}
