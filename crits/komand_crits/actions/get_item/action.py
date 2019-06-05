import komand
from .schema import GetItemInput, GetItemOutput
# Custom imports below
from komand_crits.util import utils


class GetItem(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_item',
                description='Fetches a single item',
                input=GetItemInput(),
                output=GetItemOutput())

    def run(self, params={}):
        collection = utils.slugify(params['type'])
        func = getattr(self.connection.crits, collection)
        _params = params.get('params', {})
        item_id = params['item_id']
        response = func(item_id, _params)
        return {'response': response}

    def test(self):
        """TODO: Test action"""
        return {}
