import insightconnect_plugin_runtime
from .schema import BlacklistInput, BlacklistOutput, Input, Output, Component
# Custom imports below


class Blacklist(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='blacklist',
                description=Component.DESCRIPTION,
                input=BlacklistInput(),
                output=BlacklistOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
