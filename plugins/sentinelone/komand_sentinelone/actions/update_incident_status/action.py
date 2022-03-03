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
        incidents = self.connection.remove_non_existing_incidents(
            list(set(params.get(Input.INCIDENT_IDS))), incident_type
        )
        incidents = self.connection.validate_incident_state(incidents, incident_type, incident_status, "incidentStatus")
        if not incidents:
            raise PluginException(
                cause=f"No {incident_type} to update in SentinelOne.",
                assistance=f"Please verify the log, the {incident_type} are already set to the new incident status"
                " or do not exist in SentinelOne.",
            )

        response = self.connection.update_incident_status(incidents, incident_status, incident_type)
        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}
