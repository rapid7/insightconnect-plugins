import insightconnect_plugin_runtime

from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import Helper


class Quarantine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine",
            description=Component.DESCRIPTION,
            input=QuarantineInput(),
            output=QuarantineOutput(),
        )

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        case_sensitive = params.get(Input.CASE_SENSITIVE)
        whitelist = params.get(Input.WHITELIST, None)
        agents = self.connection.client.search_agents(agent, case_sensitive=case_sensitive, results_length=2)

        not_affected = {"data": {"affected": 0}}
        if not Helper.check_agents_found(agents):
            self.logger.info(f"No agents found using the host information: {agent}.")
            return {Output.RESPONSE: not_affected}

        agent_obj = agents[0]
        payload = {"ids": [agent_obj["id"]]}

        if params.get(Input.QUARANTINE_STATE):
            if Helper.check_disconnected(agent_obj):
                self.logger.info(f"Agent: {agent} is already quarantined")
                return {Output.RESPONSE: not_affected}
            if whitelist:
                Helper.find_in_whitelist(agent_obj, whitelist)
            return {Output.RESPONSE: self.connection.agents_action("disconnect", payload)}

        return {Output.RESPONSE: self.connection.agents_action("connect", payload)}
