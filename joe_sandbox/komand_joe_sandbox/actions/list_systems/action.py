import komand
from .schema import ListSystemsInput, ListSystemsOutput, Input, Output
# Custom imports below


class ListSystems(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_systems',
                description='Retrieve a list of systems on the server',
                input=ListSystemsInput(),
                output=ListSystemsOutput())

    def run(self, params={}):
        systems = self.connection.api.systems()
        return {'systems': systems}
