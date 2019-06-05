import komand
from .schema import GetAgentsInput, GetAgentsOutput
# Custom imports below


class GetAgents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_agents',
                description='Get agent data',
                input=GetAgentsInput(),
                output=GetAgentsOutput())

    def run(self, params={}):
        agents = self.connection.client.agents.list(**params)
        agent_list = []

        # NOTE: The Threat Stack module is inconsistent as a result of the web
        # API being inconsistent.  We check if the generator is not iteratable
        # and then check again if the list is empty.
        while True:
            try:
                agent = next(agents)
                agent_list.append(agent)
            except TypeError:
                # Nothing found.
                # Not necessarily an error; could be failed search.
                break
            except StopIteration:
                break

        return {'agents': agent_list, 'count': len(agent_list)}

    def test(self):
        '''Test action'''
        return self.run()
