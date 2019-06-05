import komand
from .schema import LowerInput, LowerOutput
# Custom imports below


class Lower(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lower',
                description='Converts uppercase letters to lowercase',
                input=LowerInput(),
                output=LowerOutput())

    def run(self, params={}):
        string = params.get('string')
        if not string:
            raise Exception('Action failed! Missing required user input. '
                            'Please provide the input string.')

        return {'lower': string.lower()}
