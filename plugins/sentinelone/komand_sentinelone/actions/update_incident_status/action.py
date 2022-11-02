import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import UpdateIncidentStatusInput, UpdateIncidentStatusOutput, Input, Output, Component


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
        incident_status = params.get(Input.INCIDENT_STATUS).replace(" ", "_")
        incident = params.get(Input.THREAT_ID)
        self.connection.check_if_incident_exist(incident, incident_type)
        self.connection.validate_incident_state(incident, incident_type, incident_status, "incidentStatus")
        response = self.connection.update_incident_status(incident, incident_status, incident_type)
        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}
