import insightconnect_plugin_runtime
from .schema import SearchIncidentsInput, SearchIncidentsOutput, Input, Output, Component


# Custom imports below

# Not Tested Yet
class SearchIncidents(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_incidents',
            description=Component.DESCRIPTION,
            input=SearchIncidentsInput(),
            output=SearchIncidentsOutput())

    def run(self, params={}):
        payload = {
            "Text": params.get(Input.TEXT),
            "ObjectType": params.get(Input.OBJECT_TYPE),
            "Top": params.get(Input.TOP),
            "Skip": params.get(Input.SKIP)
        }

        data = self.connection.ivanti_service_manager_api.search_incident(params.get(Input.TEXT), payload)
        return {Output.DATA: data}
