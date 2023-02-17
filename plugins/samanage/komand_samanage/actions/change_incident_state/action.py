import insightconnect_plugin_runtime
from .schema import ChangeIncidentStateInput, ChangeIncidentStateOutput

# Custom imports below


class ChangeIncidentState(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="change_incident_state",
            description="Update the state of an incident",
            input=ChangeIncidentStateInput(),
            output=ChangeIncidentStateOutput(),
        )

    def run(self, params={}):
        incident_id = params.get("incident_id")
        state = params.get("state")

        incident = self.connection.api.change_incident_state(incident_id, state)

        return {"incident": incident}
