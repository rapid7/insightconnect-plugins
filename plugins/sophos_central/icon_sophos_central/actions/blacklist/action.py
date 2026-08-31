import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component

# Custom imports below
import validators
from insightconnect_plugin_runtime.exceptions import PluginException


class Blacklist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="blacklist",
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        hash_input = params.get(Input.HASH)
        blacklist_state = params.get(Input.BLACKLIST_STATE)
        description = params.get(Input.DESCRIPTION)
        # END INPUT BINDING - DO NOT REMOVE

        success = False
        if not validators.sha256(hash_input):
            raise PluginException(
                cause="An invalid hash was provided.",
                assistance="Please enter a SHA256 hash and try again.",
            )

        if blacklist_state:
            action = self.connection.client.blacklist(hash_input, description)
            success = action.get("id") is not None
        else:
            uuid = None
            for blocked_item in self.connection.client.iter_blacklist_items():
                if blocked_item.get("properties", {}).get("sha256") == hash_input:
                    uuid = blocked_item.get("id")
                    break

            if uuid is None:
                raise PluginException(
                    cause="Unable to unblacklist a hash that is not in the blacklist.",
                    assistance="Please provide a hash that is already blacklisted.",
                )

            action = self.connection.client.unblacklist(uuid)
            success = action.get("deleted") is not None

        return {Output.SUCCESS: success}
