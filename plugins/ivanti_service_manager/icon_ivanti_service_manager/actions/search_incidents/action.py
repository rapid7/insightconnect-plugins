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
        object_type = params.get(Input.OBJECT_TYPE)
        text = params.get(Input.TEXT)
        top = params.get(Input.TOP)
        skip = params.get(Input.SKIP)

        payload = {
            "Text": text,
            "ObjectType": object_type,
            "Top": top,
            "Skip": skip
        }

        data = self.connection.ivanti_service_manager_api.search_incident(text, payload)
        return {Output.DATA: data}
