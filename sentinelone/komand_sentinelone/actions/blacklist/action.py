import komand
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below
import re


class Blacklist(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description=Component.DESCRIPTION,
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        if re.match(r'\b[0-9a-f]{40}\b', params.get(Input.HASH)) is None:
            raise PluginException(cause="An invalid hash was provided.",
                                  assistance="Please enter a SHA1 hash and try again.")

        blacklist_state = params.get(Input.BLACKLIST_STATE)
        if blacklist_state is True:
            errors = self.connection.create_blacklist_item(
                params.get(Input.HASH),
                params.get(Input.DESCRIPTION, "Hash Blacklisted from InsightConnect")
            )
        else:
            item_ids = self.connection.get_item_ids_by_hash(params.get(Input.HASH))
            errors = self.connection.delete_blacklist_item_by_hash(item_ids)

        if len(errors) == 0:
            success_result = True
        else:
            raise PluginException(cause='The response from SentinelOne was not in the correct format.',
                                  assistance='Contact support for help. See log for more details',
                                  data=errors)

        return {
            Output.SUCCESS: success_result
        }
