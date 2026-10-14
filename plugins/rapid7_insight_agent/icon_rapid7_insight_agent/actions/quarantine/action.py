import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_rapid7_insight_agent.util.graphql_api.api_connection import ONLINE, STALE


class Quarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine",
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput(),
        )

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        advertisement_period = params.get(Input.INTERVAL)
        quarantine_state = params.get(Input.QUARANTINE_STATE)

        agent_id_stripped = agent_id.replace("-", "")

        agent_status = (self.connection.api.get_agent_state(agent_id_stripped) or {}).get("agentStatus")
        # The platform accepts a quarantine request for a stale agent and reports success, but nothing is isolated.
        # Unquarantine is not blocked: the platform keeps the request until the agent comes back online.
        if quarantine_state and agent_status == STALE:
            raise PluginException(
                cause=f"Agent {agent_id} is stale.",
                assistance="The agent has not checked in for a long time and will not receive a quarantine request. "
                "If the device was reinstalled, use the ID of its current agent.",
            )

        if quarantine_state:
            success = self.connection.api.quarantine(advertisement_period, agent_id_stripped)
        else:
            success = self.connection.api.unquarantine(agent_id_stripped)

        return {Output.SUCCESS: success, Output.IS_ASSET_ONLINE: agent_status == ONLINE}
