import insightconnect_plugin_runtime
from .schema import (
    UpdateAnalystVerdictInput,
    UpdateAnalystVerdictOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


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
        analyst_verdict = params.get(Input.ANALYSTVERDICT).replace(" ", "_")
        incidents = self.connection.client.validate_incidents(
            params.get(Input.INCIDENTIDS),
            incident_type,
            analyst_verdict,
            "analystVerdict",
        )
        return {
            Output.AFFECTED: self.connection.client.update_analyst_verdict(
                incident_type,
                {
                    "filter": {"ids": incidents},
                    "data": {"analystVerdict": analyst_verdict},
                },
            )
            .get("data", {})
            .get("affected", 0)
        }
