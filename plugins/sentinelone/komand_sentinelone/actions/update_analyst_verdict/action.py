import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import UpdateAnalystVerdictInput, UpdateAnalystVerdictOutput, Input, Output, Component


class UpdateAnalystVerdict(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_analyst_verdict",
            description=Component.DESCRIPTION,
            input=UpdateAnalystVerdictInput(),
            output=UpdateAnalystVerdictOutput(),
        )

    def run(self, params={}):
        incident_type = params.get(Input.TYPE)
        analyst_verdict = params.get(Input.ANALYST_VERDICT).replace(" ", "_")
        incidents = self.connection.remove_non_existing_incidents(
            list(set(params.get(Input.INCIDENT_IDS))), incident_type
        )
        incidents = self.connection.validate_incident_state(incidents, incident_type, analyst_verdict, "analystVerdict")
        if not incidents:
            raise PluginException(
                cause=f"No {incident_type} to update in SentinelOne.",
                assistance=f"Please verify the log, the {incident_type} are already set to the new analyst verdict"
                " or do not exist in SentinelOne.",
            )

        response = self.connection.update_analyst_verdict(incidents, analyst_verdict, incident_type)
        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}
