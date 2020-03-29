import komand
from .schema import SplitToListInput, SplitToListOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class SplitToList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='split_to_list',
            description=Component.DESCRIPTION,
            input=SplitToListInput(),
            output=SplitToListOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        delimiter = params.get(Input.DELIMITER)
        if delimiter == "":
            self.logger.info('User did not supply a string delimiter. '
                             'Defaulting to a newline character.')
            delimiter = "\n"

        return {Output.LIST: string.split(delimiter)}
