import insightconnect_plugin_runtime
from .schema import UpdateIncidentByNumberInput, UpdateIncidentByNumberOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import prepare_incident_payload


class UpdateIncidentByNumber(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="updateIncidentByNumber",
            description=Component.DESCRIPTION,
            input=UpdateIncidentByNumberInput(),
            output=UpdateIncidentByNumberOutput(),
        )

    def run(self, params={}):
        return {
            Output.INCIDENT: self.connection.api_client.update_incident_by_number(
                params.get(Input.NUMBER), prepare_incident_payload(params.copy())
            )
        }
