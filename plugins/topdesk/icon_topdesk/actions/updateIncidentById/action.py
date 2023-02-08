import insightconnect_plugin_runtime
from .schema import UpdateIncidentByIdInput, UpdateIncidentByIdOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import prepare_incident_payload


class UpdateIncidentById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updateIncidentById",
            description=Component.DESCRIPTION,
            input=UpdateIncidentByIdInput(),
            output=UpdateIncidentByIdOutput(),
        )

    def run(self, params={}):
        return {
            Output.INCIDENT: self.connection.api_client.update_incident_by_id(
                params.get(Input.ID), prepare_incident_payload(params.copy())
            )
        }
