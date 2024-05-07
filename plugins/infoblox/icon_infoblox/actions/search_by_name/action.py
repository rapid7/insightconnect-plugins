import insightconnect_plugin_runtime
from .schema import SearchByNameInput, SearchByNameOutput, Input, Output, Component

# Custom imports below


class SearchByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_by_name",
            description=Component.DESCRIPTION,
            input=SearchByNameInput(),
            output=SearchByNameOutput(),
        )

    def run(self, params={}):
        name_pattern = params.get(Input.NAME_PATTERN)

        hosts = self.connection.infoblox_connection.search_by_name(name_pattern)

        return {Output.RESULT: hosts}
