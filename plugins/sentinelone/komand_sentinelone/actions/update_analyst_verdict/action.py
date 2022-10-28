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
        incident = params.get(Input.THREAT_ID)
        self.connection.check_if_incident_exist(incident, incident_type)
        self.connection.validate_incident_state(incident, incident_type, analyst_verdict, "analystVerdict")
        response = self.connection.update_analyst_verdict(incident, analyst_verdict, incident_type)
        affected = response.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}
