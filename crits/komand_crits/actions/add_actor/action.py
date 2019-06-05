import komand
from komand_crits.util import utils
from .schema import AddActorInput, AddActorOutput


class AddActor(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_actor',
                description='Creates a new actor',
                input=AddActorInput(),
                output=AddActorOutput())

    def run(self, params={}):
        response = self.connection.crits.add_actor(
            name=params['name'],
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
