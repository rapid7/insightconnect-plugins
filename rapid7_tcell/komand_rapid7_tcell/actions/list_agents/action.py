import komand
from .schema import ListAgentsInput, ListAgentsOutput
# Custom imports below


class ListAgents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_agents',
                description='Fetch details for all seen agents (optionally matching the provided criteria)',
                input=ListAgentsInput(),
                output=ListAgentsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        from_ = params.get('from')
        to = params.get('to')
        per_page = params.get('per_page', 10)
        page = params.get('page', 1)

        agents = self.connection.api.list_agents(
            app_id, from_, to, per_page, page
        )
        if agents is None:
            agents = {'total': 0, 'agents': []}

        return agents
