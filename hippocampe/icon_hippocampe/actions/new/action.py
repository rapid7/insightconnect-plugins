import komand
from .schema import NewInput, NewOutput
# Custom imports below


class New(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new',
                description='Return all elements with Hippocampe/new type',
                input=NewInput(),
                output=NewOutput())

    def run(self, params={}):
        new_elements = self.connection.api.new()
        return {'new_elements': new_elements}
