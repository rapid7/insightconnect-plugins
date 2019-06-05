import komand
from .schema import GetCollectionInput, GetCollectionOutput
# Custom imports below
from komand_crits.util import utils


class GetCollection(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_collection',
                description='Fetches a collection',
                input=GetCollectionInput(),
                output=GetCollectionOutput())

    def run(self, params={}):
        collection = utils.slugify(params['collection'])
        func = getattr(self.connection.crits, collection)
        _params = params.get('params', {})
        total = params['total']
        objects = list(func(_params, total))
        return {'response': {'objects': objects}}

    def test(self):
        """TODO: Test action"""
        return {}
