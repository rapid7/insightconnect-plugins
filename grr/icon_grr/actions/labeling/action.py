import komand
from .schema import LabelingInput, LabelingOutput


# Custom imports below


class Labeling(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='labeling',
            description='Looks for exposed secrets in the git commit history and branches',
            input=LabelingInput(),
            output=LabelingOutput())
        self.grrapi = None

    def run(self, params={}):
        self.grrapi = self.connection.grrapi
        query = params.get('query')
        label = params.get('label')
        label = [str(x) for x in label]
        search_results = self.grrapi.SearchClients(query)
        try:
            for client in search_results:
                type_client = type(client)
                if type(client) is not type_client:
                    return {'result': "No clients found with the given query"}
                client.AddLabels(label)
        except Exception as e:
            self.logger.error(e)
        return {'results': 'All clients have been labeled'}

    def test(self):
        self.grrapi = self.connection.grrapi
        if self.grrapi:
            return {'results': 'Ready to label'}
        if not self.grrapi:
            return {'results': 'Not ready. Please check your connection with the GRR Client'}
