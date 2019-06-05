import komand
from .schema import AddActorIdentifierInput, AddActorIdentifierOutput
# Custom imports below
from komand_crits.util import utils


class AddActorIdentifier(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_actor_identifier',
                description='Creates a new actor identifier',
                input=AddActorIdentifierInput(),
                output=AddActorIdentifierOutput())

    def run(self, params={}):
        """TODO: Run action"""
        response = self.connection.crits.add_actor_identifier(
            id_type=params['id_type'],
            id_=params['id'],
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
