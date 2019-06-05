import komand
from .schema import AddIndicatorInput, AddIndicatorOutput
# Custom imports below
from komand_crits.util import utils


class AddIndicator(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_indicator',
                description='Creates a new indicator',
                input=AddIndicatorInput(),
                output=AddIndicatorOutput())

    def run(self, params={}):
        response = self.connection.crits.add_indicator(
            type_=params['type'],
            value=params['value'],
            source=params['source'],
            params=params['params']
        )
        return {'response': utils.make_response(response)}

    def test(self):
        """TODO: Test action"""
        return {}
