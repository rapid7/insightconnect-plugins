import insightconnect_plugin_runtime
from .schema import UpdateAgentThreatInput, UpdateAgentThreatOutput, Input, Output, Component
# Custom imports below


class UpdateAgentThreat(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_agent_threat',
                description=Component.DESCRIPTION,
                input=UpdateAgentThreatInput(),
                output=UpdateAgentThreatOutput())

    def run(self, params={}):
        agent = params.get(Input.AGENT)
        threat = params.get(Input.THREAT_IDENTIFIER)
        quarantine = params.get(Input.QUARANTINE_STATE)

        # TODO check api.py get agent details. 

        return {}
