import komand
from .schema import SplitToListInput, SplitToListOutput
# Custom imports below
from komand.exceptions import PluginException


class SplitToList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='split_to_list',
                description='Converts a string to a list of strings',
                input=SplitToListInput(),
                output=SplitToListOutput())

    def run(self, params={}):
        string = params.get('string')
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        delimiter = params.get('delimiter')
        if delimiter == "":
            self.logger.info('User did not supply a string delimiter. '
                             'Defaulting to a newline character.')
            delimiter = "\n"

        return {'list': string.split(delimiter)}
