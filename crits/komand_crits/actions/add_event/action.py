import komand
from .schema import AddEventInput, AddEventOutput
# Custom imports below
from komand_crits.util import utils


class AddEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_event',
                description='Creates a new event',
                input=AddEventInput(),
                output=AddEventOutput())

    def run(self, params={}):
        response = self.connection.crits.add_event(
            type_=params['type'],
            title=params['title'],
            description=params['description'],
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
