import insightconnect_plugin_runtime
from .schema import SearchIncidentInput, SearchIncidentOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class SearchIncident(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_incident",
            description=Component.DESCRIPTION,
            input=SearchIncidentInput(),
            output=SearchIncidentOutput(),
        )

    def run(self, params={}):
        url = self.connection.incident_url
        query = {"sysparm_query": params.get(Input.QUERY)}
        method = "get"

        response = self.connection.request.make_request(url, method, params=query)

        try:
            results = response["resource"].get("result")
            system_ids = [result.get("sys_id") for result in results if isinstance(result, dict)]
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {Output.SYSTEM_IDS: system_ids}
