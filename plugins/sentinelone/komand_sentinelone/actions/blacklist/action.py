import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Component, Input, Output

# Custom imports below
import re
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import List
from komand_sentinelone.util.constants import BlacklistMessage


class Blacklist(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="blacklist",
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput(),
        )

    def run(self, params={}):
        provided_hash = params.get(Input.HASH)
        if not re.match(r"\b[0-9a-f]{40}\b", provided_hash):
            raise PluginException(
                cause="An invalid hash was provided.",
                assistance="Please enter a SHA1 hash and try again.",
            )

        blacklist_state = params.get(Input.BLACKLISTSTATE)
        if blacklist_state:
            success = self.connection.client.create_blacklist_item(
                provided_hash,
                params.get(Input.DESCRIPTION, "Hash blacklisted from InsightConnect"),
            )
            message = BlacklistMessage.blocked if success else BlacklistMessage.already_blocked
        else:
            item_ids = self.connection.client.get_item_ids_by_hash(provided_hash)
            success = self.connection.client.delete_blacklist_item_by_hash(item_ids) if item_ids else False
            message = self._get_message(item_ids)

        return {Output.SUCCESS: success, Output.MESSAGE: message}

    @staticmethod
    def _get_message(item_ids: List[str]) -> str:
        if len(item_ids) == 0:
            return BlacklistMessage.not_exists
        return BlacklistMessage.unblocked
