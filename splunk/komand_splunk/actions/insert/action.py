import komand
from .schema import InsertInput, InsertOutput
# Custom imports below


class Insert(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='insert',
                description='Insert events into an index',
                input=InsertInput(),
                output=InsertOutput())

    def run(self, params={}):
        """Run insert action"""
        index_name = params.get('index')
        if not index_name:
            raise ValueError('index name is required')
        event = params.get('event').encode('utf-8')
        if not event:
            raise ValueError('event is required')

        index = None
        try:
            index = self.connection.client.indexes[index_name]
        except:
            index = self.connection.client.indexes.create(index_name)

        kwargs = {}
        if params.get('host'):
            kwargs['host'] = params.get('host')
        if params.get('source'):
            kwargs['source'] = params.get('source')
        if params.get('sourcetype'):
            kwargs['sourcetype'] = params.get('sourcetype')

        index.submit(event, **kwargs)
        return {}

    def test(self):
        return {}
