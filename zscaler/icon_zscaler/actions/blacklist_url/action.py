import insightconnect_plugin_runtime
from .schema import BlacklistUrlInput, BlacklistUrlOutput, Input, Output, Component
# Custom imports below


class BlacklistUrl(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist_url',
                description=Component.DESCRIPTION,
                input=BlacklistUrlInput(),
                output=BlacklistUrlOutput())

    def run(self, params={}):
        blacklist_state = params.get(Input.BLACKLIST_STATE, True)
        if blacklist_state:
            blacklist_step = "ADD_TO_LIST"
        else:
            blacklist_step = "REMOVE_FROM_LIST"

        return {
            Output.SUCCESS: self.connection.client.blacklist_url(blacklist_step, params.get(Input.URLS))
        }
