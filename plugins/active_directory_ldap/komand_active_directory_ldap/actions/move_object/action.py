# Custom imports below
import re

import insightconnect_plugin_runtime

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
        formatter = ADUtils()
        dn = params.get(Input.DISTINGUISHED_NAME)
        new_ou = params.get(Input.NEW_OU)
        relative_dn = ""
        dn = formatter.format_dn(dn)[0]
        dn = formatter.unescape_asterisk(dn)
        self.logger.info(f"Escaped DN {dn}")

        pattern = re.search(r"CN=[^,]*,", dn)
        self.logger.debug(pattern)
        if pattern:
            relative_dn = pattern.group()
            relative_dn = relative_dn[:-1]
            self.logger.debug(relative_dn)
        return {Output.SUCCESS: self.connection.client.move_object(dn, relative_dn, new_ou)}
