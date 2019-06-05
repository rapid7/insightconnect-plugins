import komand
from .schema import GetAgentDetailsInput, GetAgentDetailsOutput
# Custom imports below


class GetAgentDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent_details',
                description='Fetches details for the agent with the given ID',
                input=GetAgentDetailsInput(),
                output=GetAgentDetailsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        agent_id = params.get('agent_id')

        agent = self.connection.api.get_agent_details(app_id, agent_id)

        return {'agent': agent}

    def test(self):
        return {}
