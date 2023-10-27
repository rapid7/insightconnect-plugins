import insightconnect_plugin_runtime
from .schema import QuarantineInput, QuarantineOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from typing import List


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
        whitelist = params.get(Input.WHITELIST)
        not_affected = 0
        agents = self.connection.client.search_agents(agent)

        if not self.__check_agents_found(agents):
            self.logger.info(f"No agents found using the host information: {agent}.")
            return {Output.AFFECTED: not_affected}

        agent_object = agents[0]
        payload = {"ids": [agent_object.get("id")]}

        if params.get(Input.QUARANTINESTATE):
            if self.__check_disconnected(agent_object):
                self.logger.info(f"Agent {agent} is already quarantined.")
                return {Output.AFFECTED: not_affected}
            if whitelist:
                self.__find_in_whitelist(agent_object, whitelist)
            return {
                Output.AFFECTED: self.connection.client.agents_action("disconnect", payload)
                .get("data", {})
                .get("affected", 0)
            }

        return {
            Output.AFFECTED: self.connection.client.agents_action("connect", payload).get("data", {}).get("affected", 0)
        }

    @staticmethod
    def __check_agents_found(agents: list) -> bool:
        if not agents:
            return False
        if len(agents) > 1:
            raise PluginException(
                cause="Multiple agents found.",
                assistance="Please provide a unique identifier for the agent to be quarantined.",
            )
        return True

    @staticmethod
    def __check_disconnected(agent_object: dict) -> bool:
        if agent_object.get("networkStatus") in ["disconnected", "disconnecting"]:
            return True
        return False

    def __find_in_whitelist(self, agent_object: dict, whitelist: list):
        for key, value in agent_object.items():
            if key in ["externalIp", "computerName", "id", "uuid"]:
                self.__raise_when_value_in_whitelist(value, whitelist)
            if key == "networkInterfaces":
                network_dict = value[0]
                for network_key, network_value in network_dict.items():
                    if network_key in ["inet", "inet6"]:
                        for ip_address in network_value:
                            self.__raise_when_value_in_whitelist(ip_address, whitelist)

    @staticmethod
    def __raise_when_value_in_whitelist(value: str, whitelist: List[str]):
        if value in whitelist:
            raise PluginException(
                cause="Agent found in the whitelist.",
                assistance=f"If you would like to block this host, remove {value} from the whitelist and try again.",
            )
