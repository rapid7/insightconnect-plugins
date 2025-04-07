import insightconnect_plugin_runtime
from .schema import (
    UpdateIncidentStatusInput,
    UpdateIncidentStatusOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


class UpdateIncidentStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_incident_status",
            description=Component.DESCRIPTION,
            input=UpdateIncidentStatusInput(),
            output=UpdateIncidentStatusOutput(),
        )

    def run(self, params={}):
        incident_type = params.get(Input.TYPE)
        incident_status = params.get(Input.INCIDENTSTATUS).replace(" ", "_")
        incidents = self.connection.client.validate_incidents(
            params.get(Input.INCIDENTIDS),
            incident_type,
            incident_status,
            "incidentStatus",
        )
        return {
            Output.AFFECTED: self.connection.client.update_incident_status(
                incident_type,
                {
                    "filter": {"ids": incidents},
                    "data": {"incidentStatus": incident_status},
                },
            )
            .get("data", {})
            .get("affected", 0)
        }
