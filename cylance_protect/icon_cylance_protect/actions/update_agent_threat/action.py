import insightconnect_plugin_runtime
from .schema import UpdateAgentThreatInput, UpdateAgentThreatOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
from icon_cylance_protect.util.find_helpers import find_in_whitelist, find_agent_by_ip
import validators


class UpdateAgentThreat(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_agent_threat',
                description=Component.DESCRIPTION,
                input=UpdateAgentThreatInput(),
                output=UpdateAgentThreatOutput())

    def run(self, params={}):
        threat_identifier = params.get(Input.THREAT_IDENTIFIER)
        threats = self.connection.client.search_threats([threat_identifier])

        if len(threats) > 1:
            self.logger.info(
                f"Multiple threats found that matched the query: {threat_identifier}."
                "We will only act upon the first match"
            )

        payload = {
            "threat_id": threats[0].get('sha256')
        }

        if params.get(Input.QUARANTINE_STATE):
            payload["event"] = "Quarantine"
        else:
            payload["event"] = "Waive"

        # If IPv4, attempt to find its ID
        agent = params.get(Input.AGENT)
        if validators.ipv4(agent):
            agent = find_agent_by_ip(self.connection, agent)

        errors = self.connection.client.update_agent_threat(
            self.connection.client.get_agent_details(agent).get('id'),
            payload
        )

        if len(errors) != 0:
            raise PluginException(cause='The response from the CylancePROTECT API was not in the correct format.',
                                  assistance='Contact support for help. See log for more details',
                                  data=errors)

        return {
            Output.SUCCESS: True
        }
