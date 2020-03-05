import komand
from .schema import LastQueryInput, LastQueryOutput
# Custom imports below


class LastQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='last_query',
                description='Return the last query date for every source',
                input=LastQueryInput(),
                output=LastQueryOutput())

    def run(self, params={}):
        last_queries = self.connection.api.last_query()
        return {'last_queries': last_queries}
