import komand
from .schema import TypeInput, TypeOutput
# Custom imports below


class Type(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='type',
                description='Return all the known types',
                input=TypeInput(),
                output=TypeOutput())

    def run(self, params={}):
        types = self.connection.api.type()
        return {'types': types}
