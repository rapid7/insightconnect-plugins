# Custom imports below
import re

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_active_directory_ldap.util.utils import ADUtils
from .schema import MoveObjectInput, MoveObjectOutput, Output, Input


class MoveObject(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="move_object",
            description="Move an Active Directory object from one organizational unit to another",
            input=MoveObjectInput(),
            output=MoveObjectOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        distinguished_name = params.get(Input.DISTINGUISHED_NAME)
        new_ou = params.get(Input.NEW_OU)
        # END INPUT BINDING - DO NOT REMOVE

        relative_dn = ""
        distinguished_name = ADUtils.format_dn(distinguished_name)[0]
        distinguished_name = ADUtils.unescape_asterisk(distinguished_name)
        self.logger.info(f"Escaped DN {distinguished_name}")

        pattern = re.search(r"CN=[^,]*,", distinguished_name)
        self.logger.debug(pattern)
        if pattern:
            relative_dn = pattern.group()
            relative_dn = relative_dn[:-1]
            self.logger.debug(relative_dn)

        try:
            return {
                Output.SUCCESS: self.connection.client.move_object(
                    distinguished_name, relative_dn, new_ou
                )
            }
        except PluginException:
            self.logger.info("Escaping non-ascii characters...")
            return {
                Output.SUCCESS: self.connection.client.move_object(
                    ADUtils.escape_non_ascii_characters(distinguished_name),
                    relative_dn,
                    new_ou,
                )
            }
