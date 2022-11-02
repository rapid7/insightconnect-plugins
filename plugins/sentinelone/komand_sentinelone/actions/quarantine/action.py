import insightconnect_plugin_runtime
from typing import List

from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


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
        agents = self.connection.client.search_agents(agent, case_sensitive=case_sensitive, results_length=2)
        whitelist = params.get(Input.WHITELIST, None)

        not_affected = {"data": {"affected": 0}}

        if self.__check_agents_found(agents):
            self.logger.info(f"No agents found using the host information: {agent}.")
            return {Output.RESPONSE: not_affected}

        agent_obj = agents[0]

        payload = {"ids": [agent_obj["id"]]}

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
                assistance="Please provide a unique identifier for the agent to be quarantined.",
            )
        if len(agents) == 0:
            return True
        return False

    @staticmethod
    def __check_disconnected(agent_obj: dict) -> bool:
        if agent_obj["networkStatus"] == "disconnected" or agent_obj["networkStatus"] == "disconnecting":
            return True
        return False

    def __find_in_whitelist(self, agent_obj: dict, whitelist: list):
        for key, value in agent_obj.items():
            if key in ["externalIp", "computerName", "id", "uuid"]:
                self.__raise_when_value_in_whitelist(value, whitelist)
            if key == "networkInterfaces":
                network_dict = value[0]
                for network_key, network_val in network_dict.items():
                    if network_key in ["inet", "inet6"]:
                        for ip_address in network_val:
                            self.__raise_when_value_in_whitelist(ip_address, whitelist)

    def __raise_when_value_in_whitelist(self, value: str, whitelist: List[str]):
        if value in whitelist:
            raise PluginException(
                cause="Agent found in the whitelist.",
                assistance=f"If you would like to block this host, remove {value} from the whitelist and try again.",
            )
