import komand
from .schema import HipposcoreInput, HipposcoreOutput
# Custom imports below


class Hipposcore(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hipposcore',
                description='Return a score for each of the given observables. The score is ranged between 0 and -100 (0 = observable unknown, -100 = super evil observable)',
                input=HipposcoreInput(),
                output=HipposcoreOutput())

    def run(self, params={}):
        observables = params.get('observables')
        scores = self.connection.api.hipposcore(observables)
        return {'scores': scores}
