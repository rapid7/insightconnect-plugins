import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SearchIncidentsInput, SearchIncidentsOutput, Input, Output, Component


class SearchIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_incidents",
            description=Component.DESCRIPTION,
            input=SearchIncidentsInput(),
            output=SearchIncidentsOutput(),
        )

    def run(self, params={}):
        response = self.connection.ivanti_service_manager_api.search_incident(params.get(Input.KEYWORD)).get("value")
        if not response:
            raise PluginException(cause="No incidents found.", assistance="Please try a different keyword")
        return {Output.DATA: response}
