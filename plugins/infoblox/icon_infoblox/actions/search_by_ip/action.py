import insightconnect_plugin_runtime
from .schema import SearchByIpInput, SearchByIpOutput, Input, Output, Component

# Custom imports below


class SearchByIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_by_ip",
            description=Component.DESCRIPTION,
            input=SearchByIpInput(),
            output=SearchByIpOutput(),
        )

    def run(self, params={}):
        ip = params.get(Input.IP)
        objects = self.connection.infoblox_connection.search_by_ip(ip)

        result = []
        for o in objects:
            result.extend(o["objects"])

        return {Output.RESULT: result}
