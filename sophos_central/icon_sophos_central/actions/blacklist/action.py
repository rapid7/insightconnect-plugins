import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
# Custom imports below
import validators
from insightconnect_plugin_runtime.exceptions import PluginException


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='blacklist',
            description=Component.DESCRIPTION,
            input=BlacklistInput(),
            output=BlacklistOutput())

    def run(self, params={}):
        success = False
        hash_input = params.get(Input.HASH)
        if not validators.sha256(hash_input):
            raise PluginException(cause="An invalid hash was provided.",
                                  assistance="Please enter a SHA256 hash and try again.")

        if params.get(Input.BLACKLIST_STATE):
            action = self.connection.client.blacklist(hash_input, params.get(Input.DESCRIPTION))
            success = action.get("id") is not None
        else:
            for page in range(1, 9999):
                list_of_blacklist_item = self.connection.client.get_blacklists(page)

                uuid = None
                for e in list_of_blacklist_item.get("items", []):
                    if e.get("properties", {}).get("sha256") == hash_input:
                        uuid = e.get("id")
                        break

                if uuid is None:
                    raise PluginException(cause="Unable to unblacklist a hash that is not in the blacklist.",
                                          assistance="Please provide a hash that is already blacklisted.")

                action = self.connection.client.unblacklist(uuid)
                success = action.get("deleted") is not None

                if page + 1 > list_of_blacklist_item.get("pages", {}).get("total"):
                    break

        return {
            Output.SUCCESS: success
        }
