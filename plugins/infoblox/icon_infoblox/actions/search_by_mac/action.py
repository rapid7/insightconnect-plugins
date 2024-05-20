import insightconnect_plugin_runtime
from .schema import SearchByMacInput, SearchByMacOutput, Input, Output, Component

# Custom imports below


class SearchByMac(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_by_mac",
            description=Component.DESCRIPTION,
            input=SearchByMacInput(),
            output=SearchByMacOutput(),
        )

    def run(self, params={}):
        mac = params.get(Input.MAC)

        return {Output.RESULT: self.connection.infoblox_connection.search_by_mac(mac)}
