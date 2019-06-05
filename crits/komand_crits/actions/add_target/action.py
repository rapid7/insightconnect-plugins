import komand
from .schema import AddTargetInput, AddTargetOutput
# Custom imports below
from komand_crits.util import utils


class AddTarget(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_target',
                description='Creates a new target',
                input=AddTargetInput(),
                output=AddTargetOutput())

    def run(self, params={}):
        response = self.connection.crits.add_target(
            email=params['email']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
