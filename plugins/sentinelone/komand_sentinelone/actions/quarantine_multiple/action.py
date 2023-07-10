import insightconnect_plugin_runtime
from .schema import QuarantineMultipleInput, QuarantineMultipleOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import HTTPError
from komand_sentinelone.util.helper import Helper


class QuarantineMultiple(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="quarantine_multiple",
            description=Component.DESCRIPTION,
            input=QuarantineMultipleInput(),
            output=QuarantineMultipleOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agents = params.get(Input.AGENTS, [])
        whitelist = params.get(Input.WHITELIST, None)
        quarantine_state = params.get(Input.QUARANTINE_STATE)
        # END INPUT BINDING - DO NOT REMOVE

        completed = []
        failures = []
        for agent in agents:
            agents_found = self.connection.client.search_agents(agent, results_length=2)

            if not Helper.check_agents_found(agents_found):
                error = f"No agents found using the host information: {agent}."
                self.logger.info(error)
                failures.append(Helper.return_failure_details(agent, error))
                continue

            agent_obj = agents_found[0]
            payload = {"ids": [agent_obj["id"]]}

            try:
                action_type = "connect"
                agent_disconnected = Helper.check_disconnected(agent_obj)
                if quarantine_state:
                    if agent_disconnected:
                        self.logger.info(f"Agent: {agent} is already quarantined")
                    if whitelist:
                        Helper.find_in_whitelist(agent_obj, whitelist)
                    action_type = "disconnect"
                if not agent_disconnected:
                    self.logger.info(f"Agent: {agent} is already unquarantined")
                self.connection.agents_action(action_type, payload)
                completed.append(agent)
            except (PluginException, HTTPError) as error:
                failures.append(Helper.return_failure_details(agent, str(error)))
        return {
            Output.COMPLETED: completed,
            Output.FAILURES: failures,
        }
