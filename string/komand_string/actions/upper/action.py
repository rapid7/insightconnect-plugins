import komand
from .schema import UpperInput, UpperOutput
# Custom imports below


class Upper(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='upper',
                description='Converts lowercase letters to uppercase',
                input=UpperInput(),
                output=UpperOutput())

    def run(self, params={}):
        string = params.get('string')
        if not string:
            raise Exception('Action failed! Missing required user input. '
                            'Please provide the input string.')
        return {'upper': string.upper()}
