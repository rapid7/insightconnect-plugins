import insightconnect_plugin_runtime
from .schema import ContextLookupInput, ContextLookupOutput, Component

# Custom imports below
from icon_greynoise.actions.ip_lookup.action import IpLookup


class ContextLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="context_lookup",
            description=Component.DESCRIPTION,
            input=ContextLookupInput(),
            output=ContextLookupOutput(),
        )

    def run(self, params={}):
        lookup = IpLookup()
        lookup.connection = self.connection
        lookup.logger = self.logger
        return lookup.run(params)
