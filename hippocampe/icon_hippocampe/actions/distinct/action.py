import komand
from .schema import DistinctInput, DistinctOutput
# Custom imports below


class Distinct(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='distinct',
                description='Return all distinct values that match the given intelligence types',
                input=DistinctInput(),
                output=DistinctOutput())

    def run(self, params={}):
        intelligence_types = params.get('intelligence_types')
        values = self.connection.api.distinct(intelligence_types)
        return {'values': values}
