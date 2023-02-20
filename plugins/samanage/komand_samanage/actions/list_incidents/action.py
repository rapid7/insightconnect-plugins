import insightconnect_plugin_runtime
from .schema import ListIncidentsInput, ListIncidentsOutput

# Custom imports below


class ListIncidents(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="list_incidents",
            description="List all incidents",
            input=ListIncidentsInput(),
            output=ListIncidentsOutput(),
        )

    def run(self, params={}):
        incidents = self.connection.api.list_incidents()
        return {"incidents": incidents}
