import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import re


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description=Component.DESCRIPTION,
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        sha1_hash = params.get(Input.HASH)
        if params.get(Input.BLACKLIST_STATE) is True:
            errors = self.connection.client.create_blacklist_item({
                "sha256": sha1_hash,
                "list_type": "GlobalQuarantine",
                "category": "None",
                "reason": params.get(Input.DESCRIPTION)
            })
        else:
            errors = self.connection.client.delete_blacklist_item({
                "sha256": sha1_hash,
                "list_type": "GlobalQuarantine"
            })

        if len(errors) != 0:
            raise PluginException(cause='The response from Cylance API was not in the correct format.',
                                  assistance='Contact support for help. See log for more details',
                                  data=errors)

        return {
            Output.SUCCESS: True
        }
