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
        dn, search_base = formatter.format_dn(dn)
        self.logger.info(f"Escaped DN {dn}")

        pairs = formatter.find_parentheses_pairs(dn)
        # replace ( and ) when they are part of a name rather than a search parameter
        if pairs:
            dn = formatter.escape_brackets_for_query(dn, pairs)

        self.logger.info(dn)

        return {Output.SUCCESS: self.connection.client.modify_object(dn, search_base, attribute, attribute_value)}
