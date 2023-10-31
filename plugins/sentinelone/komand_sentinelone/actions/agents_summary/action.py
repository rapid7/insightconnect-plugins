import insightconnect_plugin_runtime
from .schema import AgentsSummaryInput, AgentsSummaryOutput, Input, Output, Component

# Custom imports below


class AgentsSummary(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="agents_summary",
            description=Component.DESCRIPTION,
            input=AgentsSummaryInput(),
            output=AgentsSummaryOutput(),
        )

    def run(self, params={}):
        site_ids = params.get(Input.SITEIDS, [])
        account_ids = params.get(Input.ACCOUNTIDS, [])
        response = self.connection.client.get_agents_summary(
            {
                "siteIds": ",".join(site_ids) if site_ids else None,
                "accountIds": ",".join(account_ids) if account_ids else None,
            }
        ).get("data", {})
        return {
            Output.DECOMMISSIONED: response.get("decommissioned", 0),
            Output.INFECTED: response.get("infected", 0),
            Output.OUTOFDATE: response.get("outOfDate", 0),
            Output.ONLINE: response.get("online", 0),
            Output.TOTAL: response.get("total", 0),
            Output.UPTODATE: response.get("upToDate", 0),
        }
