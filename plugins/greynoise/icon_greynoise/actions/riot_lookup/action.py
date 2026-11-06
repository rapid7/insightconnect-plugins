import insightconnect_plugin_runtime
from .schema import RiotLookupInput, RiotLookupOutput, Component

# Custom imports below
from icon_greynoise.actions.ip_lookup.action import IpLookup


class RiotLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="riot_lookup",
            description=Component.DESCRIPTION,
            input=RiotLookupInput(),
            output=RiotLookupOutput(),
        )

    def run(self, params={}):
        lookup = IpLookup()
        lookup.connection = self.connection
        lookup.logger = self.logger
        return lookup.run(params)
