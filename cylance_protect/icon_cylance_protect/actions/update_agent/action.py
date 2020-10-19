import insightconnect_plugin_runtime
from .schema import UpdateAgentInput, UpdateAgentOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from icon_cylance_protect.util.find_helpers import find_agent_by_ip
import validators


class UpdateAgent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_agent',
                description=Component.DESCRIPTION,
                input=UpdateAgentInput(),
                output=UpdateAgentOutput())

    def run(self, params={}):
        # If IPv4, attempt to find its ID first
        agent = params.get(Input.AGENT)
        if validators.ipv4(agent):
            agent = find_agent_by_ip(self.connection, agent)

        agent = self.connection.client.get_agent_details(agent)
        policy = params.get(Input.POLICY)

        if policy == "":
            policy = self._find_default_policy_id()

        errors = self.connection.client.update_agent(
            agent.get('id'),
            {
                "add_zone_ids": params.get(Input.ADD_ZONES, None),
                "name": agent.get('name'),
                "policy_id": policy,
                "remove_zone_ids": params.get(Input.REMOVE_ZONES, None)
            }
        )

        if len(errors) != 0:
            raise PluginException(cause='The response from the CylancePROTECT API was not in the correct format.',
                                  assistance='Contact support for help. See log for more details',
                                  data=errors)

        return {
            Output.SUCCESS: True
        }
    
    def _find_default_policy_id(self) -> str:
        i = 1
        while i < 9999:
            response = self.connection.client.get_policies(i)
            if i > response.get('total_pages'):
                break
            for policy in response.get('page_items'):
                if policy.get('name') == 'Default':
                    return policy.get('id')
            i += 1

        raise PluginException(
            cause='Default policy not found.',
            assistance='Please specify a valid policy ID to update on this agent'
        )
