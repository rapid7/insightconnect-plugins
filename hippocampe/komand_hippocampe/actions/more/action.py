import komand
from .schema import MoreInput, MoreOutput
# Custom imports below


class More(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='more',
                description='Return intelligence about given observables',
                input=MoreInput(),
                output=MoreOutput())

    def run(self, params={}):
        observables = params.get('observables')
        results = self.connection.api.more(observables)
        return {'results': results}
