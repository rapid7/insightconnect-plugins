import komand
from .schema import GetAgentInput, GetAgentOutput
# Custom imports below


class GetAgent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agent',
                description='Get agent data',
                input=GetAgentInput(),
                output=GetAgentOutput())

    def run(self, params={}):
        agent = self.connection.client.agents.get(params.get('agent_id'))
        return {'agent': agent}

    def test(self):
        '''Test action'''
        self.logger.info('Unable to test request, proceeding with example output')
        return { 'agent': {} }
