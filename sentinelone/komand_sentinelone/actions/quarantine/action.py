import komand
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below


class Quarantine(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='quarantine',
                description=Component.DESCRIPTION,
                input=QuarantineInput(),
                output=QuarantineOutput())

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        agents = self.connection.client.search_agents(agent, 2)
        whitelist = params.get(Input.WHITELIST, None)

        not_affected = {"response": {"data": {"affected": 0}}}

        if self.__check_agents_found(agents):
            self.logger.info(f"No agents found using the host information: {agent}.")
            return {Output.RESPONSE: not_affected}

        agent_obj = agents[0]

        payload = {'ids': [agent_obj['id']]}

        if params.get(Input.QUARANTINE_STATE):
            if self.__check_disconnected(agent_obj):
                self.logger.info(f"Agent: {agent} is already quarantined")
                return {Output.RESPONSE: not_affected}
            if whitelist:
                self.__find_in_whitelist(agent_obj, whitelist)
            return {Output.RESPONSE: self.connection.agents_action("disconnect", payload)}

        return {Output.RESPONSE: self.connection.agents_action("connect", payload)}

    @staticmethod
    def __check_agents_found(agents: list) -> bool:
        if len(agents) > 1:
            raise PluginException(
                        cause="Multiple agents found.",
                        assistance="Please provide a unique identifier for the agent to be quarantined."
                    )
        if len(agents) == 0:
            return True
        return False

    @staticmethod
    def __check_disconnected(agent_obj: dict) -> bool:
        if agent_obj['networkStatus'] == "disconnected" or agent_obj['networkStatus'] == "disconnecting":
            return True
        return False

    @staticmethod
    def __find_in_whitelist(agent_obj: dict, whitelist: list):
        for key, value in agent_obj.items():
            if key == 'inet' or key == 'externalIp' or key == 'computerName' or key == 'id':
                if value in whitelist:
                    raise PluginException(
                        cause="Agent found in the whitelist.",
                        assistance=f"If you would like to block this host, remove {value} from the whitelist and try again."
                    )
        return
